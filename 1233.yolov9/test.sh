#!/usr/bin/env bash

python val_dual.py --data data/coco.yaml --img 640 --batch 8 \
      --conf 0.001 --iou 0.4 --device 0 \
      --weights runs/train/1233/weights/best.pt --name 1233.test \
      --task test