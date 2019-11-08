#!python
#!/usr/bin/env python

# import statements

from scipy.io import loadmat
from channel import Channel

if __name__ == "__main__":
	print("Now running!")

	channels = {
		"anxiety": Channel("Test_sounds/Anxiety.wav"),
		"anger1": Channel("Test_sounds/Cranky Chords.wav"),
	}

	for c in channels:
		channels[c].startPlay()
	for c in channels:
		channels[c].endPlay()

	fmridata = loadmat('Brainhack_Nov2019/Data/Rest/Run1/Rest1LR_Sub100307_Glasser.mat')
	print (fmridata)
	#lon = x['lon']
	#lat = x['lat']
	# one-liner to read a single variable
	#lon = loadmat('test.mat')['lon']