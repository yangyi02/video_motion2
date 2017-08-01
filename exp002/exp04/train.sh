#!/bin/bash

source ../../set_path.sh

CUDA_VISIBLE_DEVICES=1 python ../demo.py --train --data=mpii64 --batch_size=64 --image_size=64 --image_channel=1 --motion_range=2 --num_frame=3 --train_epoch=2000 --test_interval=200 --test_epoch=20 --learning_rate=0.001 2>&1 | tee train.log
