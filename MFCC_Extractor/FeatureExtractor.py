import glob
from scipy.io.wavfile import read
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np

for i in range (1,10):
  for y in range(1,10):
    wavs = []
    dirName = str(i)+'/'+str(y) +'/'
    for filename in glob.glob(dirName+'*.wav'):
        (rate,sig) = wav.read(filename)
        mfcc_feat = mfcc(sig,rate,0.025,0.01,13,26,1200)
        #padding begins
        b=np.zeros((14352, 13))
        result= np.zeros(b.shape)
        result[:mfcc_feat.shape[0],:mfcc_feat.shape[1]] = mfcc_feat
        #end of padding
        wavs.append(result.ravel())
        # wavs.append(mfcc_feat)
    
    thefile = open(dirName+str(i)+'_'+str(y)+'_'+'MFCCfeatures.txt', 'w')
    for x in range (len(wavs)):
      for item in wavs[x]:
        thefile.write("%s " % item)
      thefile.write("\n\n\n")

