import simpleaudio as sa

class Channel:
	def __init__(self, infile):
		self.wave_obj = sa.WaveObject.from_wave_file(infile)

	def startPlay(self):
		self.play_obj = self.wave_obj.play()
		
	def endPlay(self):
		self.play_obj.wait_done()
