from pymir import AudioFile
import glob
import numpy as np
import librosa
import os
from python_speech_features import mfcc

wavs = []
maxSize= 949
for i in range (1,2):
  for y in range(1,2):
    dirName = 'Data/'+str(i)+'/'+str(y) +'/sorted/'
    for filename in glob.glob(dirName+'*.wav'):
        features = []
        wavData = AudioFile.open(filename)
        fixedFrames = wavData.frames(1024)
        print(len(fixedFrames))
        if ((len(fixedFrames)) < 350 ):
          for frame in fixedFrames:
            features.append(frame.lpcc())
          featuresNP = np.array(features)
          print(featuresNP.shape)
          # wavs.append(featuresNP.ravel())
        # print (dirName + '                     '+ str(len(fixedFrames)))

# print(len(wavs))
# np.savetxt('lpc/lpcFrameLens512.csv',wavs,delimiter=',')

# print((fixedFrames[1].lpc()) )                       # LPC, with order = len(fixedFrames[0])-1
# print(len(fixedFrames))
# print((fixedFrames[0].lpc()))

# spectra = [f.spectrum() for f in fixedFrames]
# print(len(spectra[0].mfcc2()))
