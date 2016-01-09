#!/bin/bash

#ffmpeg -ss 00:00:00 -i ~/wrk/neuraltalk2/data/granada.mp4 -t 00:05:00 -vcodec copy -acodec copy ~/wrk/neuraltalk2/data/granada_s.mp4 
#ffmpeg -ss 00:00:00 -t 00:05:00 -i ~/wrk/neuraltalk2/data/santa.mp4 -r 5.0 ~/wrk/neuraltalk2/data/santa/img/s%4d.jpg
ffmpeg -i ~/wrk/neuraltalk2/data/santa.mp4 -vf subtitles=santa.srt out.mp4

#ffmpeg -i ~/wrk/neuraltalk2/data/granada_s.mp4 -vf subtitles=granada.srt ~/wrk/neuraltalk2/data/granada_ss.mp4

#cd /homeappl/home/gcao/local/scripts
#source gpu.sh

# Extract feature..
#cd /wrk/gcao/neuraltalk2/info/
#python caffe_feat.py

# Activate Torch
#. /homeappl/home/gcao/wrk/torch/install/bin/torch-activate

# Do caption generation
#cd /wrk/gcao/neuraltalk2/ 
#th eval.lua -model /wrk/gcao/neuraltalk2/model/model_coco.t7 -image_folder /wrk/gcao/neuraltalk2/data/santa/key  -num_images -1

#srun ./crawl.py

# training
#th train.lua -input_h5 info/im2text.h5 -input_json info/im2text.json

# preprocessing
#python prepro.py --input_json /homeappl/home/gcao/nt/info/SBUcap.js --num_val 5000 --num_test 5000 --images_root /homeappl/home/gcao/Dataset2/im2text/images/ --word_count_threshold 5 --output_json /homeappl/home/gcao/nt/info/im2text.json --output_h5 /homeappl/home/gcao/nt/info/im2text.h5
