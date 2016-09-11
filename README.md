# Video Caption with Neuraltalk2 
## General information 
This is a code release of captioning videos using Neuraltalk2. We provide a way to extract the deep image feature of VGG-16, and detect shot boundaries using the feature. We can also finetune the MS-COCO model, annotate the key frames, and return the captions to the video sequence. A sample output can be found 
[here](https://youtu.be/FmSsek5luHk).

## Steps to generate video cations
### Follow the instruction and install all required libraries.
- Caffe: https://github.com/BVLC/caffe
- neuraltalk2: https://github.com/karpathy/neuraltalk2
- ffmpeg: https://www.ffmpeg.org/

Below we show an example of generating captions from a test video sequence. You should be able to replicate the workflow with other videos.
### Extract the frames from the video.
We firstly extract the frames from the videos using ffmpeg. There are a few parameters you need to setup:
'-ss' denotes the starting time. '-t' indicates the duration of the video you want to process. '-i' gives the input video. You should replace the directory and the video name with your file. '-r' defines the frame rate, and here we use 5 ms. After that, you should define the name of the extracted image sequence in a new directory.
```
$ ffmpeg -ss 00:00:00 -t 00:00:30 -i YOUR_WORKING_DIRECTORY/data/  test.mp4 -r 5.0 YOUR_WORKING_DIRECTORY/data/santa/img/s%4d.jpg

```
