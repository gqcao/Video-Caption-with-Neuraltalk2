from numpy import *
import re
# load text one line at a time..
def loadstr(filename,converter=str):
    return [converter(c.strip()) for c in file(filename).readlines()]

# load text one line at a time, the numbers are comma separates per line..
def loadint(filename,converter=str):
    integers = [map(int, converter(c.strip()).split(',')) for c in file(filename).readlines()]
    return integers

# write text one line at a time..
# forming a template..
def writestr(filename,texts):
    with file(filename, 'w') as outfile:
        for i in range(len(texts)):
            line = str(texts[i]) + '\n'
            #line = re.sub('[!@#$]', '', line)
            #line.rstrip()
            #line = line + '\n'
            outfile.write(line)

def loadcsv(filename, skip):
    output = []
    with open(filename) as fr: 
        if skip == 1:
            next(fr)
        for line in fr: 
            output.append(map(float, line.split(',')))
    return array(output)
