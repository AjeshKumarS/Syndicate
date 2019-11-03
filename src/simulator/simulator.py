import random
import threading
import time
from ..algorithm.algorithm import algorithm
from ..signal import Signal
from enum import Enum


density_reduction_rate = 2/20
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
                if densities[i] <= Signal.lanes_duration[Signal.curr_lane_to_open] * (density_reduction_rate):
                    densities[i] = 1
                else:
                    densities[i] = Signal.lanes_densities[i] - \
                        Signal.lanes_duration[Signal.curr_lane_to_open] * \
                        (density_reduction_rate)

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
            densities[i] = random.randrange(5, 100)
        Signal.update_timings(densities)

        Simulator.run_algorithm()

    @staticmethod
    def simulate_with_perf():
        sum_time_algo = 0
        avg_algo = 0.00
        sum_time_fixed = 0
        avg_fixed = 0.00
        for i in range(1):
            densities = [0, 0, 0, 0]
            for j in range(4):
                densities[j] = random.randrange(5, 100)
            Signal.update_timings(densities)
            algo_densities = densities[:]
            lanes_done = 0
            while lanes_done != 4:
                curr_lane = Signal.curr_lane_to_open
                curr_timing = Signal.lanes_duration[curr_lane]
                sum_time_algo += curr_timing
                if algo_densities[curr_lane] > 0:
                    if algo_densities[curr_lane] - (density_reduction_rate) * curr_timing > 0:
                        algo_densities[curr_lane] = algo_densities[curr_lane] - \
                            (density_reduction_rate) * curr_timing
                    else:
                        algo_densities[curr_lane] = 0
                    if algo_densities[curr_lane] == 0:
                        lanes_done += 1
                Signal.update_priority(curr_timing, curr_lane)

            # Fixed : 30 sec for 1 lane
            lanes_done = 0
            while lanes_done != 4:
                for j in range(len(densities)):
                    if densities[j] > 0:
                        sum_time_fixed += 120
                        if densities[j] - (density_reduction_rate) * 120 > 0:
                            densities[j] = densities[j] - (density_reduction_rate) * 120
                        else:
                            densities[j] = 0
                        if densities[j] <= 0:
                            lanes_done += 1
        avg_fixed = float(sum_time_fixed/1)
        avg_algo = float(sum_time_algo/1)
        print("Avg time taken to empty all lanes in")
        print("Fixed : ", avg_fixed)
        print("Algo : ", avg_algo)
