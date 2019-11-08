from mxm.midifile import MidiOutFile
from mxm.midifile import MidiInFile, MidiToCode
class Channel:
	#Create file
	def __init__(self, channel, input_midi):
		self.channel = channel
		out_file = open(data_folder + str(channel)+'.mid', 'wb')
		self.output_midi = MidiOutFile(out_file)
		self.input_midi = MidiInFile(MidiToCode(), input_midi)

	def store_channels(self, channel_sig):
		self.signal = channel_signal

	def process(self):
		self.midi.header(format=0, nTracks=1, division=96)
		self.midi.start_of_track()
		self.midi.update_time(0)
		for idx, val in enumerate(self.signal):
			if(val == 1):
				self.midi.note_on(idx, 0x40, 0x64)
				self.midi.update_time(idx+50)
				self.midi.note_off(0, 0x40, 0x40)

	def play(self,idx)
		self.signal