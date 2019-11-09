import pygame

class WavChannel:
	#Create file
	def __init__(self, channel, name = ''):

		# channel number
		self.channel = channel

		# channel name
		self.name = name

		# This is the sound channel
		self.voice = pygame.mixer.Channel(channel)

	def setMode(self, mode):
		self.mode = mode

	def setWave(self,input_wav):
		try:
			self.sound = pygame.mixer.Sound(input_wav)
		except:
			print("Cannot find {0}".format(input_wav))

	def store_channels(self, channel_sig):
		self.signal = channel_sig

	def startPlay(self):
		self.sound.play()

	def isPlaying(self):
		return self.voice.get_busy()

	def checkPlay(self, idx):
		if self.mode == 'binary':
			if self.signal[idx] == 1:
				if not self.isPlaying():
					self.voice.play(self.sound)
				return self.name
			else:
				#self.sound.stop()
				self.sound.fadeout(500)
		elif self.mode == 'modulate':
			#print(self.channel, self.signal[idx])
			if self.signal[idx] > 0:
				self.sound.set_volume(self.signal[idx])
				if not self.isPlaying():
					self.voice.play(self.sound)
				return "{0} ({1:.2f})".format(self.name,self.signal[idx])
			else:
				self.sound.fadeout(50)
		elif self.mode == 'trigger':
			#print(self.channel, self.signal[idx])
			if self.signal[idx] > 0:
				#self.sound.set_volume(self.signal[idx])
				if not self.isPlaying():
					self.voice.play(self.sound)
				return "{0} ({1:.2f})".format(self.name,self.signal[idx])
			else:
				self.sound.fadeout(2000)
		else:
			self.voice.play(self.sound)
			return self.name

		return None


	def endPlay(self):
		self.sound.stop()