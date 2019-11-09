import pygame
'''
class MidiChannel:
	#Create file
	def __init__(self, channel, input_midi):
		self.channel = channel
		out_file = open(data_folder + str(channel)+'.mid', 'wb')
		self.output_midi = MidiOutFile(out_file)
		self.input_midi = MidiInFile(MidiToCode(), input_midi)
​
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
'''
class WavChannel:
	#Create file
	def __init__(self, channel, name = ''):

		# channel number
		self.channel = channel

		# channel name
		self.name = name

		# This is the sound channel
		self.voice = pygame.mixer.Channel(channel)

	def setWave(self,input_wav):
		self.sound = pygame.mixer.Sound(input_wav)


	def store_channels(self, channel_sig):
		self.signal = channel_sig

	def startPlay(self):
		self.sound.play()

	def isPlaying(self):
		return self.voice.get_busy()

	def checkPlay(self, idx):
		if self.signal[idx] == 1:
			if not self.isPlaying():
				self.voice.play(self.sound)
			return self.name
		else:
			#self.sound.stop()
			self.sound.fadeout(500)
		return None


	def endPlay(self):
		self.sound.stop()