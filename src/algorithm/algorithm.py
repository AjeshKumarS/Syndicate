import time
from ..signal import Signal


def algorithm():
	while True:
		i = 0
		while i < 4:
			Signal.timings()
			print("Current Lane: " + str(i) + "\n")
			for j in range(Signal.lanes[i]):
				if Signal.emergency:
					i = Signal.target - 1
					Signal.emergency = False
					break
				else:
					time.sleep(1)
			i = i + 1
