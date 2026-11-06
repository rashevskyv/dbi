# Community translations / Traducciones comunitarias

## English

[DBIPatcher](https://github.com/rashevskyv/DBIPatcher) provides community
translations through an external `translation.bin` file. Its language
dictionaries include English (`en`) and Latin American Spanish (`es419`).

The original Russian DBI executable does not load this file. Use a compatible
DBIPatcher-patched executable. A translated interface is not an official
English or Spanish DBI release.

1. Obtain a patched executable compatible with your DBI version and the
   translation format. Do not mix files from unrelated releases.
2. Place the patched executable at `sdmc:/switch/DBI/DBI.nro`.
3. Place the selected translation at `sdmc:/switch/DBI/translation.bin`.
   Keep that exact path and filename; the runtime patch uses this fixed path.
4. Fully close DBI and reopen it to load the translation.

To change the translation, close DBI, replace only `translation.bin`, and
reopen DBI. No language selector or additional launcher is required. To
return to the original Russian release, restore the original `DBI.nro`.

Keep existing `dbi.config` settings when replacing the executable. Avoid
leaving duplicate DBI launch entries that could open an older executable.
Translation dictionary improvements can be contributed to
[DBIPatcher's CSV files](https://github.com/rashevskyv/DBIPatcher/tree/master/translations).

### Additional remote category labels

The supplementary [English](translations/server-categories/en.csv) and
[Latin American Spanish](translations/server-categories/es419.csv) CSV files
cover seven remote directory categories observed with DBI 912. Each has
14 entries: the labels with and without their numbered prefixes. They retain
the original capitalization needed for exact dictionary matching.

These files are **dictionary additions, not complete translations**. Merge
their `original,translation` rows into the corresponding DBIPatcher language
CSV, checking for duplicate originals, then rebuild with DBIPatcher's
`scripts/build_translation_bin.py`. Copy the resulting complete table to
`sdmc:/switch/DBI/translation.bin` and restart DBI. The existing compatible
patched NRO can stay in place.

The additions were built against DBIPatcher commit
`65cc1ccdf8bc2552090e69df9c3d06543e740178` and tested with a patched DBI 912.
Validation preserved all existing dictionary mappings and covered 84 new
label/path checks plus 452 sampled runtime regression cases per language in
ARM64 emulation. The Spanish console test covered translated categories,
opening the expected game list, downloading one item and completing its
installation. English passed automated checks but has not been tested on
hardware. This does not establish coverage of every DBI feature or future
server label. Embedded images and new remote text are not automatically
translated by the dictionary.

## Español latinoamericano

[DBIPatcher](https://github.com/rashevskyv/DBIPatcher) permite usar traducciones
comunitarias mediante el archivo externo `translation.bin`. Incluye inglés
(`en`) y español latinoamericano (`es419`).

El ejecutable ruso original de DBI no carga este archivo. Necesitas un
ejecutable compatible adaptado con DBIPatcher. Esto no equivale a una
versión oficial de DBI en inglés o español.

1. Obtén un ejecutable adaptado compatible con tu versión de DBI y el formato
   de traducción. No mezcles archivos de versiones diferentes.
2. Coloca el ejecutable adaptado en `sdmc:/switch/DBI/DBI.nro`.
3. Coloca la traducción elegida en `sdmc:/switch/DBI/translation.bin`.
   Conserva esa ruta y ese nombre exactos: el parche utiliza una ruta fija.
4. Cierra DBI por completo y vuelve a abrirlo para cargar la traducción.

Para cambiar la traducción, cierra DBI, reemplaza únicamente `translation.bin`
y vuelve a abrir DBI. No necesitas un selector de idioma ni otro lanzador.
Para volver a la versión rusa original, restaura el `DBI.nro` original.

Conserva tu configuración existente de `dbi.config` al reemplazar el
ejecutable. Evita dejar accesos duplicados que puedan abrir una versión
anterior de DBI. Las mejoras a los textos de la interfaz se pueden aportar
a los [archivos CSV de DBIPatcher](https://github.com/rashevskyv/DBIPatcher/tree/master/translations).

### Categorías remotas adicionales

Los CSV complementarios en [inglés](translations/server-categories/en.csv)
y [español latinoamericano](translations/server-categories/es419.csv) agregan
siete categorías observadas con DBI 912. Cada uno contiene 14 entradas:
las etiquetas con y sin numeración, respetando sus mayúsculas originales.

Son **entradas adicionales, no traducciones completas**. Integra las filas
`original,translation` en el CSV del idioma correspondiente de DBIPatcher,
comprueba que no haya originales duplicados y genera el archivo completo
con `scripts/build_translation_bin.py`. Colócalo en
`sdmc:/switch/DBI/translation.bin` y reinicia DBI. Puedes conservar el mismo
ejecutable adaptado compatible.

La prueba en español llegó desde las categorías traducidas y el listado
esperado hasta la descarga e instalación completa de un elemento. El inglés
pasó las comprobaciones automáticas, pero todavía no se probó en consola.
Esto no implica que se hayan probado todas las funciones de DBI. Las
imágenes y los textos nuevos que envíe un servidor no se traducen
automáticamente.
