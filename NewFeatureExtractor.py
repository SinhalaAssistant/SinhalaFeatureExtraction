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
        wave, sr = librosa.load(filename, mono=True, sr=None)
        trimmed, index = librosa.effects.trim(wave,top_db=40,frame_length=10, hop_length=2)
        mfcc1 = mfcc(trimmed,sr,0.025,0.01,13,26,1200)
        # mfcc = librosa.feature.mfcc(trimmed,sr, S=None, n_mfcc=13)
        # mfcc = np.transpose(mfcc)
        #padding begins
        if (maxSize > mfcc1.shape[0]):
            b=np.zeros((maxSize, 13))
            result= np.zeros(b.shape)
            result[:mfcc1.shape[0],:mfcc1.shape[1]] = mfcc1

            # print(result.shape)
            #end of padding
            wavs.append(np.append(result.ravel(),i-1))
        # wavs.append(np.append(mfcc.ravel(),i-1))

# for l in wavs:
#     print(l[-10:])
print(len(wavs))
np.savetxt('Nets/NewMFCCFeaturesWpadding.csv',wavs,delimiter=',')
    # thefile = open(dirName+str(i)+'_'+str(y)+'_'+'MFCCfeatures.txt', 'w')
    # for x in range (len(wavs)):
    #   for item in wavs[x]:
    #     thefile.write("%s " % item)
    #   thefile.write("\n\n\n")

