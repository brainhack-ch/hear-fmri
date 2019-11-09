#!python
#!/usr/bin/env python

# import statements
import sys
from scipy.io import loadmat
from channel  import WavChannel
import numpy as np
import pygame
import time


def drawBrain(fmridata):
	from bokeh.io import output_file, show
	from bokeh.plotting import figure
	from bokeh.transform import linear_cmap
	from bokeh.util.hex import hexbin

	#x = fmridata['TCS_Visual']
	#y = fmridata['TCSnf']

	n = 50000
	x = np.random.standard_normal(n)
	y = np.random.standard_normal(n)

	bins = hexbin(x, y, 0.1)

	p = figure(title="Manual hex bin for 50000 points", tools="wheel_zoom,pan,reset",
	           match_aspect=True, background_fill_color='#440154')
	p.grid.visible = False

	p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
	           fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

	output_file("hex_tile.html")

	show(p)

if __name__ == "__main__":
	print("Now running!")
	pygame.init() 

	stepsize = 720 #ms

	fmridata = loadmat('test_data/matrix_network.mat')
	#drawBrain(fmridata)
	print (fmridata)
	music_array = fmridata['matrix_network']
	nsteps = len(music_array[0])

	channels = []
	sounds = ["Test_sounds/A.wav", "Test_sounds/Bb.wav","Test_sounds/C.wav",
	           "Test_sounds/D.wav","Test_sounds/E.wav","Test_sounds/F.wav",
	           "Test_sounds/G.wav"]

	for i in range(len(music_array)):
		print ("Setting channel data to", music_array[i])
		thischannel = WavChannel("{0}".format(i), sounds[i].split('/')[-1].split('.')[0] )
		thischannel.store_channels(music_array[i])
		thischannel.setWave(sounds[i])
		channels.append(thischannel)

	for i in range(nsteps):
		notes = []
		for c in channels:
			notes.append(c.checkPlay(i))
		noteinfo = ' '.join([n if n else ' ' for n in notes])
		print("{0} {1}".format( i, noteinfo))
		time.sleep(.10)
		

	#for c in channels:
	#	c.process()
