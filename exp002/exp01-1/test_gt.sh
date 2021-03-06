#!/bin/bash

source ../../set_path.sh

python ../demo.py --test_gt --data=box_complex --batch_size=64 --image_size=32 --image_channel=1 --motion_range=2 --num_frame=3 --bg_move --test_epoch=20 --display --save_display --save_display_dir=./ 2>&1 | tee test_gt.log

sh trim.sh
