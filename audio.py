"""
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import subprocess

#command = "ffmpeg -i C:\\Users\\Steve\\Downloads\\PulpFiction(1994)\\Pulp.Fiction.1994.720p.BrRip.x264.YIFY.mp4 -ab 160k -ac 1 -ar 44100 -vn C:\\Users\\Steve\\Downloads\\PulpFiction(1994)\\audio.wav"

#subprocess.call(command)

#from pydub import AudioSegment


#sound = AudioSegment.from_wav("C:\\Users\\Steve\\Downloads\\PulpFiction(1994)\\audio.wav")
#sound = sound.set_channels(1)
#sound.export("C:\\Users\\Steve\\Downloads\\PulpFiction(1994)\\audio2.wav", format="wav")

from pylab import *
import wave

def show_wave_n_spec(speech):
    spf = wave.open(speech,'rb')
    print( spf.getnframes() )
    sound_info = spf.readframes( int(spf.getnframes() / 100) )
    #sound_info = spf.readframes( 100 )
    sound_info = fromstring(sound_info, 'Int16')

    f = spf.getframerate()
   
    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of audio.wav')

    subplot(212)
    spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')
   
    show()
    spf.close()

fil = 'C:\\Users\\Steve\\Downloads\\PulpFiction(1994)\\audio.wav'

show_wave_n_spec(fil)
"""
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('C:\\Users\\Steve\\Downloads\\PulpFiction(1994)\\audio.wav','rb')

#Extract Raw Audio from Wav File
signal = spf.readframes(int(spf.getnframes() / 80))
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print( 'Just mono files' )
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.savefig('C:\\Users\\Steve\\Downloads\\PulpFiction(1994)\\waveform.png')
plt.show()
