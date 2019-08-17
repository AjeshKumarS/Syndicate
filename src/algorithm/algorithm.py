import time
from ..signal import Signal


def algorithm():
    # Wait to ensure image processing algorithm runs at least once
    time.sleep(Signal.IMAGE_PROCESSING_FREQUENCY)
    while True:
        curr_lane = Signal.curr_lane_to_open
        curr_timing = Signal.lanes_duration[curr_lane]
        print(
            "Lane {0} is given green signal for {1} seconds".format(
                curr_lane, curr_timing
            )
        )
        for i in range(curr_timing):
            if Signal.emergency:
                while Signal.emergency:
                    print(
                        "Lane {0} is given green signal for {1} seconds".format(
                            Signal.lane_with_emergency, Signal.EMERGENCY_CONSTANT
                        )
                    )
                    time.sleep(Signal.EMERGENCY_CONSTANT)
                break
            else:
                time.sleep(1)
        Signal.update_priority(curr_timing, curr_lane)
