from pydub import AudioSegment
sound = AudioSegment.from_file("Samples/1.webm")
sound.export("Samples/1.wav", format="wav")