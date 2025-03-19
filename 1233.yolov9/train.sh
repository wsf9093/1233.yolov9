#!/usr/bin/env bash

python train_dual.py --workers 8 --device 0 --batch-size 8 \
      --data data/coco.yaml --img 640 \
      --cfg models/detect/yolov9.yaml \
      --weights '' --name 1233 \
      --hyp data/hyps/hyp.scratch-high.yaml --epochs 140