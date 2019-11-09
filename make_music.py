#!python
#!/usr/bin/env python

# import statements
import sys
from scipy.io import loadmat
from channel  import WavChannel
import numpy as np
import pygame
import time
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from matplotlib import animation

def makeAnimation(fmridata):
	fig = plt.figure()
	ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
	plt.gca().set_aspect('equal', adjustable='box')
	line, = ax.plot([], [], lw=2)
	frame1 = plt.gca()
	frame1.axes.get_xaxis().set_ticks([])
	frame1.axes.get_yaxis().set_ticks([])

	def init():
	    line.set_data([], [])
	    return line,

	def animate(i):
	    #x = np.linspace(0, 2, 1000)
	    #y = np.sin(2 * np.pi * (x - 0.01 * i))
	    #line.set_data(x, y)
	    #return line,
	    circle1 = plt.Circle((0, 0), 0.2, color='r')
	    plt.gca().add_patch(circle1)
	    return circle1,

	# call the animator.  blit=True means only re-draw the parts that have changed.
	anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)
	plt.show()

def playSong(fmridata, stepsize):
	music_array = fmridata['matrix_network']
	nsteps = len(music_array[0])

	channels = []
	sounds = ["Test_sounds/A.wav", "Test_sounds/Bb.wav","Test_sounds/C.wav",
	           "Test_sounds/D.wav","Test_sounds/E.wav","Test_sounds/F.wav",
	           "Test_sounds/G.wav"]

	# set the number of channels
	pygame.mixer.set_num_channels(7)

	for i in range(len(music_array)):
		print ("Setting channel data to", music_array[i])
		thischannel = WavChannel(i, sounds[i].split('/')[-1].split('.')[0] )
		thischannel.store_channels(music_array[i])
		thischannel.setWave(sounds[i])
		channels.append(thischannel)

	for i in range(nsteps):
		notes = []
		for c in channels:
			notes.append(c.checkPlay(i))
		noteinfo = ' '.join([n if n else ' ' for n in notes])
		print("{0} {1}".format( i, noteinfo))
		time.sleep(stepsize)

if __name__ == "__main__":
	print("Now running!")
	pygame.init() 

	stepsize = .0720 # seconds

	fmridata = loadmat('test_data/matrix_network.mat')
	#makeAnimation(fmridata)
	#print (fmridata)
	playSong(fmridata, stepsize)
