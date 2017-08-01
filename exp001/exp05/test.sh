#!/bin/bash

source ../../set_path.sh

python ../demo.py --test --data=nyuv2 --init_model=./model.pth --batch_size=64 --image_size=64 --image_channel=1 --motion_range=2 --num_frame=2 --test_epoch=20 --display --save_display --save_display_dir=./ 2>&1 | tee test.log

sh trim.sh
