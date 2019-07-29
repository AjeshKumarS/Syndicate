import time
from ..signal import Signal


def image():
	thresholds = [
		[10, 50, 150, 80],
		[100, 100, 100, 100],
		[150, 30, 100, 100],
	]
	
	for i in range(3):
		Signal.update_timings(thresholds[i])
		time.sleep(1.5)
