class Signal:
	maximum = 90
	standard = 60
	minimum = 30
	lanes = [0, 0, 0, 0]
	
	@staticmethod
	def update_timings(threshold):
		for i in range(4):
			val = int((Signal.standard * threshold[i])/100)
			val = max(Signal.minimum, val)
			Signal.lanes[i] = min(Signal.maximum, val)
	
	@staticmethod
	def timings():
		for i in range(4):
			print("Lane {0}: {1}".format(i, Signal.lanes[i]))
