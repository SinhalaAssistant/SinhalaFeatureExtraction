import os
from pydub import AudioSegment
rootdir = '/home/sudeepa/Documents/FYP/'  #path/to/bank/folder
output ="/home/sudeepa/Documents/output/"  #path/to/output

print "we are there"
for (subdir, dirs, files) in os.walk(rootdir):
    for file in files:
        sound = AudioSegment.from_file(os.path.join(subdir, file))  
        if not os.path.exists(output+subdir.split("/")[-1]+"/"):
            try:
                original_umask = os.umask(0)
                os.makedirs(output+subdir.split("/")[-1]+"/", 0o777)
            finally:
                os.umask(original_umask)
        sound.export(output+subdir.split("/")[-1]+"/"+file.split(".")[0]+".wav", format="wav")

