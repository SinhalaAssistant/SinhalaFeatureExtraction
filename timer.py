import glob
import numpy as np
import librosa
import os
from python_speech_features import mfcc

wavs = []
maxSize= 949
for i in range (1,10):
  for y in range(1,10):

    dirName = 'Data/'+str(i)+'/'+str(y) +'/sorted/'
    for filename in glob.glob(dirName+'*.wav'):
        # print('a')
        wave, sr = librosa.load(filename, mono=True, sr=None)
        wavs.append((librosa.get_duration(y=wave, sr=sr)))

# for l in wavs:
#     print(l[-10:])
# print(len(wavs))
print (sum(wavs))
#np.savetxt('lengths.csv',wavs,delimiter=',')
    # thefile = open(dirName+str(i)+'_'+str(y)+'_'+'MFCCfeatures.txt', 'w')
    # for x in range (len(wavs)):
    #   for item in wavs[x]:
    #     thefile.write("%s " % item)
    #   thefile.write("\n\n\n")

