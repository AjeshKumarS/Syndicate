import math


class Signal:
    lanes_densities = [0, 0, 0, 0]
    lanes_waiting_time = [0, 0, 0, 0]
    lanes_priority = [0, 0, 0, 0]
    lanes_duration = [0, 0, 0, 0]
    prev_lane_that_was_open = None
    curr_lane_to_open = None
    maximum_waiting_time = 70
    minimum_green_duration = 20
    emergency = False
    lane_with_emergency = 1
    IMAGE_PROCESSING_FREQUENCY = 5
    EMERGENCY_CONSTANT = 5

    @staticmethod
    def calculate_priority(waiting_time, density):
        waiting_time_fraction = waiting_time / Signal.maximum_waiting_time
        return (math.pow(waiting_time_fraction, 10) + density) / 10

    @staticmethod
    def update_timings(densities, waiting_duration=None, lane_not_waiting=None):
        if not (densities == []):
            Signal.lanes_densities = densities
        if waiting_duration == None or lane_not_waiting == None:
            for i in range(4):
                priority = Signal.calculate_priority(
                    Signal.lanes_waiting_time[i], Signal.lanes_densities[i]
                )
                Signal.lanes_priority[i] = priority
                Signal.lanes_duration[i] = int(
                    max(1.5 * Signal.lanes_densities[i],
                        Signal.minimum_green_duration)
                )
        else:
            for i in range(4):
                if i != lane_not_waiting:
                    Signal.lanes_waiting_time[i] += waiting_duration
                if i == lane_not_waiting:
                    Signal.lanes_waiting_time[i] = 0
                priority = Signal.calculate_priority(
                    Signal.lanes_waiting_time[i], Signal.lanes_densities[i]
                )
                Signal.lanes_priority[i] = priority
                Signal.lanes_duration[i] = int(
                    max(0.6 * Signal.lanes_densities[i],
                        Signal.minimum_green_duration)
                )
        Signal.prev_lane_that_was_open = Signal.curr_lane_to_open
        Signal.curr_lane_to_open = Signal.lanes_priority.index(
            max(Signal.lanes_priority)
        )

    # @staticmethod
    # def update_priority(, densities):
    #     Signal.lanes_densities = densities
    #     for i in range(4):
    #         priority = Signal.calculate_priority(
    #             Signal.lanes_waiting_time[i], Signal.lanes_densities[i])
    #         Signal.lanes_priority[i] = priority
    #     Signal.prev_lane_that_was_open = Signal.curr_lane_to_open
    #     Signal.curr_lane_to_open = Signal.lanes_priority.index(
    #         max(Signal.lanes_priority))

    @staticmethod
    def timings():
        for i in range(4):
            print("Lane {0}: {1}".format(i, Signal.lanes_duration[i]))
