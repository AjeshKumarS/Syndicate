import time
from ..signal import Signal
from ..bolt.bolt import change_signal


def algorithm():
    curr_lane = Signal.curr_lane_to_open
    curr_timing = Signal.lanes_duration[curr_lane]
    change_signal(curr_lane)
    print(Signal.lanes_densities, Signal.lanes_waiting_time)
    print(
        "Lane {0} is given green signal for {1} seconds".format(
            curr_lane + 1, curr_timing
        )
    )
    print("Prio : ", Signal.lanes_priority)
    print("WT : ", Signal.lanes_waiting_time)

    for i in range(curr_timing):
        if Signal.emergency:
            while Signal.emergency:
                change_signal(curr_lane)
                print(
                    "Lane {0} is given green signal for {1} seconds".format(
                        Signal.lane_with_emergency + 1, Signal.EMERGENCY_CONSTANT
                    )
                )
                time.sleep(Signal.EMERGENCY_CONSTANT)
            break
        else:
            # time passed in reduced to 0.3 sec just for testing
            time.sleep(0.3)
    Signal.update_timings(curr_timing, curr_lane)


def run_algorithm():
    # Wait to ensure image processing algorithm runs at least once
    time.sleep(Signal.IMAGE_PROCESSING_FREQUENCY)
    while True:
        algorithm()
