# Video Caption with Neuraltalk2 
### General introduction
This is a code release of captioning videos using Neuraltalk2. We provide a way to extract the deep image feature of VGG-16, and detect shot boundaries using the feature. We can also finetune the MS-COCO model, annotate the key frames, and return the captions to the video sequence. A sample output can be found at 
<a href="https://youtu.be/FmSsek5luHk" target="_blank"><img src="https://youtu.be/FmSsek5luHk/0.jpg" alt="Test captioning video by Neuraltalk2" width="240" height="180" border="10" /></a>

### Required libraries:
- Caffe: https://github.com/BVLC/caffe
- neuraltalk2: https://github.com/karpathy/neuraltalk2
- ffmpeg: https://www.ffmpeg.org/

### Steps to generate video cations
#### Follow the instruction and install all required libraries.
#### Extract the keyframes from the video
Open the python file ''
