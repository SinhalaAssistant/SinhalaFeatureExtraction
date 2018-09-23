import glob
import numpy as np
import librosa
import os
import pandas as pd
from python_speech_features import mfcc

wavs = []
lables=[]
maxSize= 950
for i in range (1,10):
  for y in range(1,10):
    dirName = str(i)+'/'+str(y) +'/sorted/'
    for filename in glob.glob(dirName+'*.wav'):
        wave, sr = librosa.load(filename, mono=True, sr=None)
        yt, index = librosa.effects.trim(wave,top_db=40,frame_length=10, hop_length=2)
        mfcc1 = mfcc(yt,sr,0.025,0.01,13,26,1200)
        # mfcc = librosa.feature.mfcc(yt,sr, S=None, n_mfcc=13)
        # mfcc = np.transpose(mfcc)
        #padding begins
        if (maxSize > mfcc1.shape[0]):
            b=np.zeros((maxSize, 13))
            result= np.zeros(b.shape)
            result[:mfcc1.shape[0],:mfcc1.shape[1]] = mfcc1

            # print(result.shape)
            #end of padding
            wavs.append(result)
        # wavs.append(np.append(mfcc.ravel(),i-1))
            lables.append(i-1)

# for l in wavs:
#     print(l)

wavs1 = np.array(wavs)
lables1 = np.array(lables)
np.save('Train_LSTM.npy',wavs1)
np.save('LSTM_labels.npy',lables1)
# df = pd.DataFrame(wavs1)
print(wavs1.shape)
print(lables1.shape)
# df.to_csv('NewMFCCFeaturesLables.csv')



# with open('NewMFCCFeaturesLables.csv','wb') as file:
#     for l in wavs:
#         file.write(l)
#         file.write('\n')

# np.savetxt('NewMFCCFeaturesMatrices.csv',wavs1,delimiter=',')
# np.savetxt('NewMFCCFeaturesLables.csv',lables,delimiter=',')
    # thefile = open(dirName+str(i)+'_'+str(y)+'_'+'MFCCfeatures.txt', 'w')
    # for x in range (len(wavs)):
    #   for item in wavs[x]:
    #     thefile.write("%s " % item)
    #   thefile.write("\n\n\n")

