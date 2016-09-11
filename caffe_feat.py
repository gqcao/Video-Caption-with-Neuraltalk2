#! /usr/bin/env python
from numpy import *
import sys
import os
import pandas as pd
#------------------------------------------------#
# Make sure that caffe is on the python path:
caffe_root = '/wrk/gcao/caffe/'  # this file is expected to be in {caffe_root}/examples
# change the path below to the directory of your video frames.
input_path = '/homeappl/home/gcao/tmp/Video-Caption/data/santa/'
#------------------------------------------------#
sys.path.insert(0, caffe_root + 'python')
import caffe
#sys.path.insert(0, '/homeappl/home/gcao/fa/misc/')
from fileproc import loadstr, writestr 

def setup():
    #caffe.set_mode_cpu()
    net = caffe.Net(caffe_root + 'models/VGG_ILSVRC_16_layers/VGG_ILSVRC_16_layers_deploy.prototxt', caffe_root + 'models/VGG_ILSVRC_16_layers/VGG_ILSVRC_16_layers.caffemodel', caffe.TEST)
    # input preprocessing: 'data' is the name of the input blob == net.inputs[0]
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    transformer.set_mean('data', load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1)) # mean pixel
    transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
    transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB

    # net.blobs['data'].reshape(1,3,227,227)
    net.blobs['data'].reshape(1,3,224,224)
    return net, transformer

def extract(filenames, net, transformer):
    feats = []
    for i in xrange(len(filenames)):
        filename = filenames[i]
        net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(img_path + filename))
        out = net.forward()
        print("Predicted class is #{}.".format(out['prob'].argmax()))
        feat = net.blobs['fc8'].data[0]
        feats.append(feat.copy())
    return feats

def writeFV(img_files, feats):
    out_filename = input_path + 'feat.txt' 
    with file(out_filename, 'w') as outfile:
        for idx,x in enumerate(feats):
            indexes	= x.nonzero()[0]
            values	= x[indexes]
            
            label = '+1' # We set the label as 1 by default
            pairs = ['%i:%f'%(indexes[i]+1,values[i]) for i in xrange(len(indexes))]
            sep_line = [label]
            sep_line.extend(pairs)
            sep_line.extend(['#' + str(img_files[idx])])
            sep_line.extend(['\n'])

            line = ' '.join(sep_line)
            outfile.write(line)

# It contains 1135 images in santa folder, which takes around 15 min to compute its feature
def loadFiles():
    global img_path
    img_path = input_path + 'img/'
    # List all files in the directory..
    from os import listdir
    from os.path import isfile, join
    img_files = [ f for f in listdir(img_path) if isfile(join(img_path, f)) and '.jpg' in f]
    print shape(img_files)
    return sorted(img_files)

def main():
    img_files = loadFiles()
    net, transformer = setup()
    feats = extract(img_files, net, transformer)
    writeFV(img_files, feats)

if __name__=="__main__":
    main()
