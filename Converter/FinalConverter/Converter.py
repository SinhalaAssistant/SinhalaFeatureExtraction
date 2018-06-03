import glob
import numpy as np
import librosa
import os
from pydub import AudioSegment
import time

start_time = time.time()

for i in range (1,10):
  for y in range(1,10):

    dirName = str(i)+'/'+str(y) +'/sorted/'
    for filename in glob.glob(dirName+'*.webm'):
        print(filename.split('.')[0])
        sound = AudioSegment.from_file(filename)
        sound.export(filename.split('.')[0]+".wav", format="wav")

print("--- %s seconds ---" % (time.time() - start_time))