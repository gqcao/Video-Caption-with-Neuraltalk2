#! /usr/bin/env python
from numpy import *
import sys
from scipy import misc
from scipy import ndimage
import dist_metrics
from fileproc import loadstr, writestr

# Change the root path to your directory
#root_path = '/homeappl/home/gcao/tmp/Video-Caption/'

def processImg(img):
    img = misc.imread(img)
    rows = shape(img)[0]
    cols = shape(img)[1]*1.0
    #img = reshape(self.img, (3 * shape(self.img)[0] * shape(self.img)[1], 1)) # the order of img_ is RGBRGB.., and goes along each row firstly..
    img = img.astype(double)
    R = img[:,:,0]; G = img[:,:,1]; B = img[:,:,2]
    histR = list(ndimage.measurements.histogram(R, 0, 255, 20))
    histG = list(ndimage.measurements.histogram(G, 0, 255, 20))
    histB = list(ndimage.measurements.histogram(B, 0, 255, 20))
    hist = mat(histR + histG + histB) / (rows * cols)
    return hist 
 
def genKeyframes():
    Thresh = .2 # We pre-define the threhold to differentiate the key frames.
    dataDir = root_path + 'data/santa/img/' 
    # Get all image frames
    from os import listdir
    from os.path import isfile, join
    img_files = [f for f in listdir(dataDir) if isfile(join(dataDir, f))]
    img_files = sorted(img_files)
    keyFrames = []
    hist_ref = processImg(dataDir + img_files[0])
    keyFrames.append(img_files[0])
    for f in img_files:
        print f
        hist = processImg(dataDir + f)
        if dist_metrics.eucl_dist(hist_ref, hist) > Thresh:
            keyFrames.append(f)
            hist_ref = hist # Use the first frame of a shot as ref..
    print shape(keyFrames)
    writestr(root_path + 'keyframes_santa.list', keyFrames)

def copyKeyframes():
    from shutil import copyfile
    keys = loadstr(root_path + 'keyframes_santa.list')
    for k in keys:
        copyfile(root_path + 'data/santa/img/'+k, root_path + 'data/santa/key/'+k)

def parseOutput():
    srt_dict = {}
    lst = loadstr(root_path + 'caplog.txt')
    for l in lst:
        if '.jpg' in l:
            img_orig = l.split()[1][1:-1]
        elif ':' in l:
            srt = l.split(':')[1][1:]
            srt_dict[img_orig] = srt
    return srt_dict

def genSrt(srt_dict):
    keys = loadstr(root_path + 'keyframes_santa.list')
    lines = []
    lines.append(1)
    num = double(keys[0][1:5]) -1 
    hour = '00'
    minute = str(int(num/5/60)).zfill(2)
    second = str(num/5.0%60).replace('.',',').zfill(4)
    start_t = hour + ':' + minute + ':' + second + '00'
    srt = srt_dict[root_path + 'data/santa/key/' + keys[0]]
    for k,i in zip(keys[1:], range(1,len(keys))):
        num = double(k[1:5]) 
        minute = str(int(num/5/60)).zfill(2)
        second = str(num/5.0%60).replace('.',',').zfill(4)
        end_t = hour + ':' + minute + ':' + second + '00'
        lines.append(start_t + ' --> ' + end_t)
        lines.append(srt)
        lines.append('')
        start_t = hour + ':' + minute + ':' + second + '25'
        srt = srt_dict[root_path + 'data/santa/key/' + k]
        lines.append(int(i)+1)
    end_t = hour + ':' + minute + ':' + second + '25'
    lines.append(start_t + ' --> ' + end_t)
    lines.append(srt)
    writestr(root_path + 'santa.srt', lines)
    
def main():
    global root_path
    root_path = sys.argv[1]
    task = sys.argv[2]
    if task == 'genKeyframes': 
        genKeyframes()
        copyKeyframes()
    elif task == 'genSrt':
        srt_dict = parseOutput()
        genSrt(srt_dict)

if __name__=='__main__':
    main()
