from __future__ import annotations

import importlib.machinery
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
DBIBACKEND = ROOT / "dbibackend"


def load_dbibackend():
    loader = importlib.machinery.SourceFileLoader("dbibackend_under_test", str(DBIBACKEND))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    module.file_list.clear()
    module.text1 = None
    module.root = None
    return module


class DbiBackendTests(unittest.TestCase):
    def test_adds_single_file(self) -> None:
        backend = load_dbibackend()
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "game.nsp"
            file_path.write_bytes(b"demo")

            added = backend.add_path_to_file_list(file_path)

        self.assertEqual(added, 1)
        self.assertEqual(list(backend.file_list), ["game.nsp"])

    def test_filters_installer_extensions_case_insensitively(self) -> None:
        backend = load_dbibackend()
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / "base.NSP").write_bytes(b"nsp")
            (folder / "update.xcz").write_bytes(b"xcz")
            (folder / "notes.txt").write_text("ignore", encoding="utf-8")

            added = backend.add_path_to_file_list(
                folder,
                extensions={"nsp", "nsz", "xci", "xcz"},
            )

        self.assertEqual(added, 2)
        self.assertEqual(set(backend.file_list), {"base.NSP", "update.xcz"})

    def test_recursive_folder_scan(self) -> None:
        backend = load_dbibackend()
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            nested = folder / "nested"
            nested.mkdir()
            (folder / "root.nsp").write_bytes(b"root")
            (nested / "child.xci").write_bytes(b"child")

            added = backend.add_path_to_file_list(folder, recursive=True)

        self.assertEqual(added, 2)
        self.assertEqual(set(backend.file_list), {"root.nsp", "child.xci"})

    def test_duplicate_names_are_not_replaced(self) -> None:
        backend = load_dbibackend()
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            first = folder / "a"
            second = folder / "b"
            first.mkdir()
            second.mkdir()
            (first / "same.nsp").write_bytes(b"first")
            (second / "same.nsp").write_bytes(b"second")

            backend.add_path_to_file_list(first / "same.nsp")
            added = backend.add_path_to_file_list(second / "same.nsp")
            stored_path = backend.file_list["same.nsp"]

            self.assertEqual(added, 0)
            self.assertEqual(stored_path.read_bytes(), b"first")

    def test_no_gui_without_files_returns_error(self) -> None:
        backend = load_dbibackend()

        result = backend.main(["--no-gui"])

        self.assertEqual(result, 1)

    def test_no_gui_with_files_starts_server(self) -> None:
        backend = load_dbibackend()
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "game.nsp"
            file_path.write_bytes(b"demo")

            with mock.patch.object(backend, "start_server") as start_server:
                result = backend.main(["--no-gui", str(file_path)])

        self.assertEqual(result, 0)
        start_server.assert_called_once_with()
        self.assertEqual(list(backend.file_list), ["game.nsp"])


if __name__ == "__main__":
    unittest.main()
