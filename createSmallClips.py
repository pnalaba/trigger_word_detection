#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:03:15 2018

@author: pradeep
"""

import numpy as np
from pydub import AudioSegment
from pylab import *
from scipy.io import wavfile
import argparse
import os
#x = graph_spectrogram("samples/input1.wav")
#constants


SAMPLES_PER_SEC = 44100
TIME_PER_CLIP = 10
SAMPLES_PER_CLIP = SAMPLES_PER_SEC*TIME_PER_CLIP

#read args
parser = argparse.ArgumentParser()
parser.add_argument("-w","--wavefile", help='input wavefile to split')
args = parser.parse_args()
print('args',args,'type',type(args))


#read data


_, data = wavfile.read(args.wavefile)
l = len(data)
l = SAMPLES_PER_CLIP*(l//SAMPLES_PER_CLIP)
data = np.array(data[:l])
data = np.reshape(data,(l//SAMPLES_PER_CLIP,SAMPLES_PER_CLIP))

filename, extension = os.path.splitext(args.wavefile)

for i,clip in enumerate(data) :
    wavfile.write("%s-%02d%s"%(filename,i,extension),SAMPLES_PER_SEC,clip)