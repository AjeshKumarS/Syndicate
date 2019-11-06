import random
import threading
import time
from ..algorithm.algorithm import algorithm
from ..signal import Signal
from enum import Enum
import urllib.request


density_reduction_rate = 2 / 5


density_reduction_rate = 2/5


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
                if densities[i] <= Signal.lanes_duration[Signal.curr_lane_to_open] * (density_reduction_rate):
                    densities[i] = 1
                else:
                    densities[i] = Signal.lanes_densities[i] - Signal.lanes_duration[
                        Signal.curr_lane_to_open
                    ] * (density_reduction_rate)

        curr_lane = Signal.curr_lane_to_open
        curr_timing = Signal.lanes_duration[curr_lane]
        Signal.update_timings(densities, curr_lane, curr_timing)

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
    def simulate_with_visuals():
        BASE_URL = "http://127.0.0.1:5000/setDensities?"
        densities = [0, 0, 0, 0]
        URL = BASE_URL
        for i in range(4):
            densities[i] = random.randrange(5, 100)
            URL = URL + "l" + str(i + 1) + "=" + str(densities[i]) + "&"
        res = urllib.request.urlopen(URL)
        print(res)
        Signal.update_timings(densities)
        Simulator.run_algorithm()

    @staticmethod
    def simulate_with_perf():
        sum_time_algo = 0
        avg_algo = 0.00
        sum_time_fixed = 0
        avg_fixed = 0.00
        no_of_cases = 1
        fixed_duration = 40
        for i in range(no_of_cases):
            densities = [0, 0, 0, 0]
            for j in range(4):
                densities[j] = random.randrange(5, 100)
            Signal.update_timings(densities)
            algo_densities = densities[:]
            print(algo_densities)
            lanes_done = 0
            while lanes_done != 4:
                curr_lane = Signal.curr_lane_to_open
                curr_timing = Signal.lanes_duration[curr_lane]
                sum_time_algo += curr_timing
                if algo_densities[curr_lane] > 0:
                    if (
                        algo_densities[curr_lane]
                        - (density_reduction_rate) * curr_timing
                        > 0
                    ):
                        algo_densities[curr_lane] = (
                            algo_densities[curr_lane]
                            - (density_reduction_rate) * curr_timing
                        )
                    else:
                        algo_densities[curr_lane] = 0
                    time.sleep(2)
                    print(algo_densities)
                    if algo_densities[curr_lane] <= 0:
                        lanes_done += 1
                Signal.update_timings(algo_densities, curr_timing, curr_lane)

            print()
            print(densities)
            lanes_done = 0
            while lanes_done != 4:
                for j in range(len(densities)):
                    sum_time_fixed += fixed_duration
                    if densities[j] > 0:
                        if densities[j] - (density_reduction_rate) * fixed_duration > 0:
                            densities[j] = densities[j] - \
                                (density_reduction_rate) * fixed_duration
                        else:
                            densities[j] = 0
                        time.sleep(2)
                        print(densities)
                        if densities[j] <= 0:
                            lanes_done += 1
        avg_fixed = float(sum_time_fixed/no_of_cases)
        avg_algo = float(sum_time_algo/no_of_cases)
        print("Avg time taken to empty all lanes in")
        print("Fixed : ", avg_fixed)
        print("Algo : ", avg_algo)
