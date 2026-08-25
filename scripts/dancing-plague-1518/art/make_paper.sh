#!/usr/bin/env bash
# Generate the paper/ink-bleed overlay plate in GIMP, headless (Script-Fu).
# Stands in for the Krita-painted overlay in PIPELINE-krita-blender.md.
set -e
here="$(cd "$(dirname "$0")" && pwd)"
out="$here/textures/paper_fibre.png"
gimp -i --batch-interpreter=plug-in-script-fu-eval -b "
(let* ((w 1024) (h 1024)
       (img (car (gimp-image-new w h RGB)))
       (base (car (gimp-layer-new img w h RGB-IMAGE \"base\" 100 LAYER-MODE-NORMAL)))
       (fib  (car (gimp-layer-new img w h RGB-IMAGE \"fibre\" 55 LAYER-MODE-GRAIN-MERGE))))
  (gimp-image-insert-layer img base 0 -1)
  (gimp-context-set-foreground '(232 220 192))
  (gimp-drawable-fill base FILL-FOREGROUND)
  (gimp-image-insert-layer img fib 0 -1)
  (plug-in-solid-noise RUN-NONINTERACTIVE img fib 0 0 1518 2 4.0 4.0)
  (plug-in-rgb-noise RUN-NONINTERACTIVE img fib 1 0 0.09 0.09 0.09 0.0)
  (plug-in-gauss RUN-NONINTERACTIVE img fib 1.1 1.1 0)
  (let ((flat (car (gimp-image-flatten img))))
    (file-png-save RUN-NONINTERACTIVE img flat \"$out\" \"paper\" 0 9 1 1 1 1 1))
  (gimp-image-delete img))
" -b '(gimp-quit 0)' 2>&1 | grep -viE 'gegl|babl|warning|^$' | head -5
echo "paper: $out"
