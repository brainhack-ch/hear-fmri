from mxm.midifile import MidiOutFile
import midi
​
class Channel:
	#Create file
	def __init__(self, channel):
		out_file = open(data_folder + str(channel)+'.mid', 'wb')
		self.midi = MidiOutFile(out_file)
​
	def store_channels(channel_signal):
		self.signal = channel_signal
​
	def output(self):
		self.midi.header(format=0, nTracks=1, division=96)
		self.midi.start_of_track()
		self.midi.update_time(0)
		for idx, val in enumerate(self.signal):
			if(val == 1):
				self.midi.note_on(idx, 0x40, 0x64)
				self.midi.update_time(idx+50)
				self.midi.note_off(0, 0x40, 0x40)