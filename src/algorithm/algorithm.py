import time
from ..signal import Signal


def algorithm():
	for i in range(3):
		time.sleep(1)
		Signal.timings()