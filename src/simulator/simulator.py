import random
import threading
import time
from ..algorithm.algorithm import algorithm
from ..signal import Signal


class Simulator:
    @staticmethod
    def gen_densities():
        while True:
            # print("gen_densities is goin to run" +
            #       str(Signal.curr_lane_to_open))
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
            # print("gen_densities ran" + str(Signal.curr_lane_to_open))
            time.sleep(0.1)

    @staticmethod
    def run_algo():
        algorithm()

    @staticmethod
    def simulate():
        densities = [0, 0, 0, 0]
        for i in range(4):
            densities[i] = random.randrange(0, 100)
        Signal.update_timings(densities)

        algo_thread = threading.Thread(target=Simulator.run_algo)
        gen_thread = threading.Thread(target=Simulator.gen_densities)

        algo_thread.start()
        gen_thread.start()

        algo_thread.join()
        gen_thread.join()
