#!/usr/bin/env python

from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np

(rate,sig) = wav.read("prev.wav")
(rate1,sig1) = wav.read("1.wav")
wavs=[]
# print(len(rate))
mfcc_feat = mfcc(sig,rate)
mfcc_feat1 = mfcc(sig1,rate1)
#mfcc_feat = mfcc(sig,rate,0.025,0.01,13,26,1200)
# d_mfcc_feat = delta(mfcc_feat, 2)
# fbank_feat = logfbank(sig,rate)



wavs.append(mfcc_feat)
wavs.append(mfcc_feat1)
wavs1=[]
for i in wavs:
    b=np.zeros((252, 13))
    result= np.zeros(b.shape)
    result[:i.shape[0],:i.shape[1]] = i

            # print(result.shape)
            #end of padding
    wavs1.append(result.ravel())

    
np.savetxt('test.csv',wavs1,delimiter=',')
print(mfcc_feat.shape)
print(mfcc_feat1.shape)
#print(d_mfcc_feat.size)
