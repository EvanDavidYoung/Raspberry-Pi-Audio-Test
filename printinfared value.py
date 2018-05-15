import sys
import wave
import pyaudio


#python -m pip install pyaudio

#define stream chunk
chunk = 1024

#open a wav format music
#sys.path
#sys.path.append(r"C:/Users/Evan_young computer/george/wowfolder/wow.wav","rb");
f = wave.open(r"/home/pi/Raspberry-Pi-Audio-Test/wowfolder/wow.wav","rb")
#instantiate PyAudio
p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)
while(1):

        presence = GPIO.input(7)
"""
        if(presence):
                peoplecount += 1
                presence = 0
                time.sleep(1.5)


        time.sleep(1)
        counter += 1

        if(counter==10):
                print peoplecount
                people.save_value({'value':peoplecount})
                counter = 0
                peoplecount = 0
"""
        time.sleep(.3)
        if(presence):
            print("Motion detected \n")
            while data:
                stream.write(data)
                data = f.readframes(chunk)

            #stop stream
            stream.stop_stream()
            stream.close()

            #close PyAudio
            p.terminate()
        else
            print("No motion detected \n")
