####Note. Due to the maintenance of my computer, the update of the project has not been finished. 
# Video Caption with Neuraltalk2 
## General information 
This is a code release of captioning videos using Neuraltalk2. We provide a way to extract the deep image feature of VGG-16, and detect shot boundaries using the feature. We can also finetune the MS-COCO model, annotate the key frames, and return the captions to the video sequence. A sample output can be found 
[here](https://youtu.be/FmSsek5luHk).

## Steps to generate video captions
### Follow the instruction and install all required libraries.
- Caffe: https://github.com/BVLC/caffe
- neuraltalk2: https://github.com/karpathy/neuraltalk2
- ffmpeg: https://www.ffmpeg.org/

Below we show an example of generating captions from a test video sequence. (The test video is part of the 'santa' video which we show on Youtube.) You should be able to replicate the workflow with your video.

### Extract frames from the video.
We firstly extract the frames from the videos using ffmpeg. There are a few parameters you need to setup:
'-ss' denotes the starting time. '-t' indicates the duration of the video you want to process. '-i' gives the input video. You should replace the directory and the video name with your file. '-r' defines the frame rate, and here we use 5 ms. After that, you should define the name of the extracted image sequence in a new directory.
```
$ ffmpeg -ss 00:00:00 -t 00:00:30 -i YOUR_WORKING_DIRECTORY/data/test.mp4 -r 5.0 YOUR_WORKING_DIRECTORY/data/santa/img/s%4d.jpg
```

### Extract deep features (VGG-16) from the video frames that you just generated.
Besides the [caffe](http://caffe.berkeleyvision.org/) package, we use one the pre-trained model called [VGG-16](http://www.robots.ox.ac.uk/~vgg/research/very_deep/). Essentially, it is a topology including a very deep network with 16 layers. 
You should download the [weights](http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel) and [layer configuration](https://gist.githubusercontent.com/ksimonyan/211839e770f7b538e2d8/raw/0067c9b32f60362c74f4c445a080beed06b07eb3/VGG_ILSVRC_16_layers_deploy.prototxt) under your Caffe directory.

Now, you can extract the visual feature from the video frames. We provide a code called 'caffe_feat.py' for that. You need to open the file and the 'caffe_root' and 'input_path' to your own directory.
