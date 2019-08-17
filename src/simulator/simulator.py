import random
import threading
import time
from ..algorithm.algorithm import algorithm
from ..signal import Signal
from enum import Enum


class Simulator:
    @staticmethod
    def gen_densities():
        densities = [0, 0, 0, 0]
        for i in range(4):
            if i != Signal.curr_lane_to_open:
                if Signal.lanes_densities[i] < 80:
                    densities[i] = Signal.lanes_densities[i] + \
                        random.randrange(0, 20)
                else:
                    densities[i] = 100
            else:
                # assuming approx 3 cars pass through each second
                # while the light is green
                # TODO: optimize based on the timing calculation algo
                if densities[i] <= Signal.lanes_duration[Signal.curr_lane_to_open] * (2/5):
                    densities[i] = 1
                else:
                    densities[i] = Signal.lanes_densities[i] - \
                        Signal.lanes_duration[Signal.curr_lane_to_open] * \
                        (2/5)

        Signal.update_timings(densities)

    @staticmethod
    def run_algorithm():
        # Wait to ensure image processing algorithm runs at least once
        time.sleep(Signal.IMAGE_PROCESSING_FREQUENCY)
        while True:
            algorithm()
            Simulator.gen_densities()

    @staticmethod
    def simulate():
        densities = [0, 0, 0, 0]
        for i in range(4):
            densities[i] = random.randrange(0, 100)
        Signal.update_timings(densities)

        Simulator.run_algorithm()
