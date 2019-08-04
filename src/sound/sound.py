import time
from ..signal import Signal


def sound():
    time.sleep(45)
    Signal.emergency = True
    Signal.lane_with_emergency = 0
