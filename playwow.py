import sys
import wave
import pyaudio
#python -m pip install pyaudio

#define stream chunk
chunk = 1024

#open a wav format music
#sys.path
#sys.path.append(r"C:/Users/Evan_young computer/george/wowfolder/wow.wav","rb");
f = wave.open(r"C:/Users/Evan_young computer/george/wowfolder/wow.wav","rb")
#instantiate PyAudio
p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)

#play stream
while data:
    stream.write(data)
    data = f.readframes(chunk)

#stop stream
stream.stop_stream()
stream.close()

#close PyAudio
p.terminate()
