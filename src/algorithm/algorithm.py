import time
from ..signal import Signal


def algorithm():
    # Wait to ensure image processing algorithm runs at least once
    time.sleep(Signal.IMAGE_PROCESSING_FREQUENCY)
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
