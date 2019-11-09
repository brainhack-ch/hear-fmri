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


basic_sounds = ["Test_sounds/A.wav", "Test_sounds/Bb.wav","Test_sounds/C.wav",
	           "Test_sounds/D.wav","Test_sounds/E.wav","Test_sounds/F.wav",
	           "Test_sounds/G.wav"]
drum_sounds = ["drum_sounds/Hi-hat 1 .wav",
               "drum_sounds/Hi-hat 2 .wav",
               "drum_sounds/Hi-hat 3 .wav",
               "drum_sounds/Kick.wav",
               "drum_sounds/Snare .wav",
               "Test_sounds/A.wav", "Test_sounds/Bb.wav",]

def playSongAndAnimation(music_array, nchannels, interval, mode, smoothingfactor = 2):
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED   = (255, 0, 0)

	background_colour = (255,255,255)
	(width, height) = (300, 300)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('A E S T H E T I C')
	pygame.display.update()
 
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	myFont = pygame.font.SysFont('arial', 14)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.draw.circle(screen, GREEN, (0,0), 20) 
		pygame.display.update()
		clock.tick(60)
	 
	# Close the window and quit.
	pygame.quit()
		

def initialiseChannels(nchannels, sounds, data_array, mode):
	pygame.mixer.set_num_channels(nchannels)
	channels = []
	for i in range(len(data_array)):
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

	channels = initialiseChannels(nchannels, drum_sounds, music_array, mode)

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
	interval = 72 # milliseconds
	nchannels = 7

	filename ='test_data/matrix_network.mat'
	dataname = 'matrix_network'

	#filename = 'test_data/peaks.mat'
	#dataname = 'signals_max'

	print ("Reading {0} from {1}".format(dataname, filename))

	fmridata = loadmat(filename)
	music_data = fmridata[dataname]

	if not len(music_data) == nchannels:
		raise ValueError("Incorrect number of channels!")

	playSongAndAnimation(music_data, nchannels, interval, mode = "binary")
	
	#playSong(music_data, nchannels, interval, mode = "binary")
