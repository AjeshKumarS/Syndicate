class Signal:
    maximum = 90
    standard = 60
    minimum = 10
    lanes_timing = [20, 20, 20, 20]
    lanes_priority = [1, 1, 1, 1]
    lanes_value = [0, 0, 0, 0]
    lanes_density = [0, 0, 0, 0]
    emergency = False
    lane_with_emergency = 1
    IMAGE_PROCESSING_FREQUENCY = 5
    EMERGENCY_CONSTANT = 5

    @staticmethod
    def update_timings(densities):
        for i in range(4):
            val = int((Signal.standard * densities[i]) / 100)
            val = max(Signal.minimum, val)
            Signal.lanes_timing[i] = min(Signal.maximum, val)
            Signal.lanes_value[i] = Signal.lanes_timing[i] * \
                Signal.lanes_priority[i]

    @staticmethod
    def update_priority():
        for i in range(4):
            Signal.lanes_priority[i] += 1

    @staticmethod
    def timings():
        for i in range(4):
            print("Lane {0}: {1}".format(i, Signal.lanes_timing[i]))
