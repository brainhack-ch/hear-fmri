#!python
#!/usr/bin/env python

# import statements
import sys
from scipy.io import loadmat
from channel  import WavChannel
import numpy as np
import pygame
import time
import math
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy import interpolate
from scipy.io.wavfile import write
import sounddevice as sd


basic_sounds = ["Test_sounds/A.wav", "Test_sounds/Bb.wav","Test_sounds/C.wav",
	           "Test_sounds/D.wav","Test_sounds/E.wav","Test_sounds/F.wav",
	           "Test_sounds/G.wav"]
drum_sounds = ["drum_sounds/Hi-hat 1 .wav",
			  "drum_sounds/Kick.wav",
               "drum_sounds/Hi-hat 2 .wav",
               #"Test_sounds/F.wav",
               #"Dynamic Composition samples/WeeWowWoo - Osc 3.wav",
               
               "drum_sounds/Snare .wav",
               "drum_sounds/Hi-hat 3 .wav",
               
               "Dynamic Composition samples/Bassline - Osc 3.wav",
               #"Test_sounds/A.wav"
               ]

drum_sounds = ["drum_sounds/Hi-hat 1 .wav",
			  "drum_sounds/Kick.wav",
               "drum_sounds/Hi-hat 2 .wav",
               #"Test_sounds/F.wav",
               #"Dynamic Composition samples/WeeWowWoo - Osc 3.wav",
               
               "drum_sounds/Snare .wav",
               "drum_sounds/Hi-hat 3 .wav",
               
               "Dynamic Composition samples/Bassline - Osc 3.wav",
               #"Test_sounds/A.wav"
               ]

dynamic_sounds = [
 "Dynamic Composition samples/Bassline - Osc 3.wav",
"Dynamic Composition samples/Blooooooop - osc 3.wav",
"Dynamic Composition samples/Creaker - Osc 1.wav",
"Dynamic Composition samples/Grr grr grr - Osc 5.wav",
"Dynamic Composition samples/Meow - Osc 6.wav",
"Dynamic Composition samples/Screamer - osc 2.wav",
"Dynamic Composition samples/WeeWowWoo - Osc 3.wav",]

fear_sounds = ["drum_sounds/Kick.wav",
 "Dynamic Composition samples/Bassline - Osc 3.wav",
"Dynamic Composition samples/Blooooooop - osc 3.wav",
"Dynamic Composition samples/Creaker - Osc 1.wav",
"Dynamic Composition samples/Grr grr grr - Osc 5.wav",
"Dynamic Composition samples/Meow - Osc 6.wav",
"Dynamic Composition samples/Screamer - osc 2.wav",
"Dynamic Composition samples/WeeWowWoo - Osc 3.wav",]

vocal_sounds = [
"Bounce Vocal chops/Camille - Sensory Motor.wav",
"Bounce Vocal chops/Charlotte  - Default .wav",
"Bounce Vocal chops/Emma - Frontal Parietal .wav",
"Bounce Vocal chops/Julien - Ventral .wav",
"Bounce Vocal chops/Paula - Dorsal attentional .wav",
"Bounce Vocal chops/Raphael - Sight.wav",
"Bounce Vocal chops/Thomas - Limbic.wav",

]

def playSongAndAnimation(music_array, nchannels, interval, mode, smoothingfactor = 2):
	fig = plt.figure()
	ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
	plt.gca().set_aspect('equal', adjustable='box')
	frame1 = plt.gca()
	frame1.axes.get_xaxis().set_ticks([])
	frame1.axes.get_yaxis().set_ticks([])
	line, = ax.plot([], [], lw=5)


	def init():
	    line.set_data([], [])
	    return line,

	def animate(i):
		#t = np.linspace(0, 1, 20)
		#x = (5)*np.cos(2 * np.pi * (t - 0.01 * i))
		#y = (5)*np.sin(2 * np.pi * (t - 0.01 * i))
		x = []
		y = []
		for t in np.linspace(0, 1, 20):
			r = 5 + 3*np.sin(2*np.pi*t*2- 0.05 * i)
			xpt = r*np.cos(2 * np.pi * (t - 0.001 * i))
			ypt = r*np.sin(2 * np.pi * (t - 0.001 * i))
			x.append(xpt)
			y.append(ypt)
		#tck, u = interpolate.splprep([x, y], s=0)
		#unew = np.arange(0, 1.01, 0.01)
		#out = interpolate.splev(unew, tck)
		#line.set_data(out[0], out[1])
		line.set_data(x, y)
		return line,


	# call the animator.  blit=True means only re-draw the parts that have changed.
	anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(music_array[0]), interval=20, blit=True)
	plt.show()
	 
	# Close the window and quit.
	pygame.quit()
		

def initialiseChannels(nchannels, sounds, data_array, mode):
	pygame.mixer.set_num_channels(nchannels)
	channels = []
	for i in range(nchannels):
		print ("Setting channel data to", data_array[i])
		thischannel = WavChannel(i, sounds[i].split('/')[-1].split('.')[0] )
		thischannel.store_channels(data_array[i])
		thischannel.setWave(sounds[i])
		thischannel.setMode(mode)
		channels.append(thischannel)
	return channels

def playSong(music_array, nchannels, interval, mode = "binary"):

	print(music_array)

	nsteps = len(music_array[0])

	channels = initialiseChannels(nchannels, fear_sounds, music_array, mode)

	for i in range(nsteps):
		notes = []
		for c in channels:
			notes.append(c.checkPlay(i))
		noteinfo = ' '.join([n if n else ' ' for n in notes])
		print("{0} {1}".format( i, noteinfo))
		time.sleep(interval/1000.)

if __name__ == "__main__":
	print("Now running!")
	pygame.init() 
	interval = 720 # milliseconds
	nchannels = 8

	#filename ='test_data/matrix_network.mat'
	#dataname = 'matrix_network'

	#filename = 'test_data/peaks.mat'
	#dataname = 'signals_max'

	#filename = 'test_data/TIMECOURSES_THRESHOLDED.mat'
	#dataname = 'TC_positive'
	#dataname = "TC_negative"

	#filename = "test_data/output_fear 100307.mat"
	#dataname = "output_fear"

	filename = "test_data/output 100307final.mat"
	dataname = "output_fear"

	print ("Reading {0} from {1}".format(dataname, filename))

	fmridata = loadmat(filename)
	print (fmridata)
	#sys.exit()
	music_data = fmridata[dataname]

	if len(music_data) < nchannels:
		raise ValueError("Not enough channels! Expected {0} and got {1}".format(nchannels, len(music_data) ))

	#playSongAndAnimation(music_data, nchannels, interval, mode = "binary")
	
	#fs = 44100
	#duration = 10.5  # seconds
	#sd.default.samplerate = 44100
	#sd.default.device = 'digital output'
	#myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
	playSong(music_data, nchannels, interval, mode = "modulate")
	#sd.wait()
	#write('output.wav', fs, myrecording)

