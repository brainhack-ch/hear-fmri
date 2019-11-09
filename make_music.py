#!python
#!/usr/bin/env python

# import statements
import sys
from scipy.io import loadmat
from channel  import WavChannel
import numpy

if __name__ == "__main__":
	print("Now running!")

	stepsize = 720 #ms

	fmridata = loadmat('test_data/matrix_network.mat')
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
		print("{0} {1}".format(i,notes))
		

	#for c in channels:
	#	c.process()
