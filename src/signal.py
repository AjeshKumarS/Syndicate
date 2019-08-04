class Signal:
	maximum = 90
	standard = 60
	minimum = 10
	lanes = [20, 20, 20, 20]
	emergency = False
	target = 1
	IMAGE_PROCESSING_FREQUENCY = 5
	
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
