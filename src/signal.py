import math

class Signal:
    lanes_densities = [0, 0, 0, 0]
    lanes_waiting_time = [0, 0, 0, 0]
    lanes_priority = [0, 0, 0, 0]
    lanes_duration = [0, 0, 0, 0]
    curr_lane_to_open = None
    maximum_waiting_time = 120
    minimum_green_duraiton = 20
    emergency = False
    lane_with_emergency = 1
    IMAGE_PROCESSING_FREQUENCY = 5
    EMERGENCY_CONSTANT = 5

    @staticmethod
    def calculate_priority(waiting_time, density):
        waiting_time_fraction = waiting_time/Signal.maximum_waiting_time
        print((waiting_time_fraction*waiting_time_fraction + density)/10)
        return math.log((waiting_time_fraction*waiting_time_fraction + density)/10, 10)

    @staticmethod
    def update_timings(densities):
        Signal.lanes_densities = densities
        for i in range(4):
            priority = Signal.calculate_priority(Signal.lanes_waiting_time[i], Signal.lanes_densities[i])
            Signal.lanes_priority[i] = priority
            Signal.lanes_duration[i] = int(0.6 * Signal.lanes_densities[i] + 20)
        Signal.curr_lane_to_open = Signal.lanes_priority.index(max(Signal.lanes_priority))


    @staticmethod
    def update_priority(waiting_duration, lane_not_waiting):
        for i in range(4):
            if i != lane_not_waiting:
                Signal.lanes_waiting_time[i] += waiting_duration
            priority = Signal.calculate_priority(Signal.lanes_waiting_time[i], Signal.lanes_densities[i])
            Signal.lanes_priority[i] = priority

    @staticmethod
    def timings():
        for i in range(4):
            print("Lane {0}: {1}".format(i, Signal.lanes_timing[i]))
