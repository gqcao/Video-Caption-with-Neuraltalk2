#! /usr/bin/env python
from numpy import *
import sys
sys.path.insert(0, '/homeappl/home/gcao/tmp/Video-Caption/')
from fileproc import loadstr
import subprocess

def remove():
    lst = loadstr('status.txt')
    for l in lst:
        if 'deleted' in l:
            command = 'git rm' + l.split(':')[1]
            subprocess.call(command, shell=True)

if __name__=='__main__':
    remove()
