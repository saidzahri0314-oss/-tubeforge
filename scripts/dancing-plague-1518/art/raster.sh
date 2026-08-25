#!/usr/bin/env bash
# Raster the authored SVGs with Inkscape (headless). Hatch tiles -> textures/,
# finished plates -> plates/.
set -e
here="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$here/textures" "$here/plates"
for f in "$here"/svg/hatch_*.svg; do
  n=$(basename "$f" .svg)
  inkscape "$f" --export-type=png --export-width=1024 \
           --export-filename="$here/textures/$n.png" 2>/dev/null
  echo "texture: $n.png"
done
for f in "$here"/svg/[0-9]*.svg; do
  n=$(basename "$f" .svg)
  inkscape "$f" --export-type=png --export-width=1920 \
           --export-filename="$here/plates/$n.png" 2>/dev/null
  echo "plate:   $n.png"
done
