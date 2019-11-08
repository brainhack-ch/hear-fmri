#!python
#!/usr/bin/env python

# import statements
import sys
from scipy.io import loadmat
from channel  import Channel
import numpy

if __name__ == "__main__":
	print("Now running!")

	stepsize = 720 #ms

	fmridata = loadmat('test_data/matrix_network.mat')
	music_array = fmridata['matrix_network']
	channels = []
	for i in range(len(music_array)):
		thischannel = Channel("{0}".format(i))
		thischannel.store_channels(music_array[i])
		channels.append(thischannel)

	for c in channels:
		c.output()
