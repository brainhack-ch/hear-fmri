
import simpleaudio as sa

'''
pygame.mixer.music.load("music.mid")
pygame.mixer.music.play()
'''
class WavChannel:
	#Create file
	def __init__(self, channel, name = ''):
		self.channel = channel
		self.name = name

	def setWave(self,input_wav):
		self.wave_obj = sa.WaveObject.from_wave_file(input_wav)

	def store_channels(self, channel_sig):
		self.signal = channel_sig

	def startPlay(self):
		self.play_obj = self.wave_obj.play()

	def checkPlay(self, idx):
		if self.signal[idx] == 1:
			print (idx, self.name)
			self.play_obj = self.wave_obj.play()
			self.play_obj.wait_done()

	def endPlay(self):
		self.play_obj.wait_done()