import random
import threading
from ..algorithm.algorithm import algorithm
from ..signal import Signal


class Simulator:
    @staticmethod
    def gen_densities():
        densities = [0, 0, 0, 0]
        for i in range(4):
            if Signal.lanes_priority[i] != 0:
                densities[i] = Signal.lanes_densities[i] + \
                    random.randrange(0, 50)
            else:
                # assuming approx 10 cars pass through each second
                # while the light is green
                # TODO: optimize based on the timing calculation algo
                densities[i] = Signal.lanes_densities[i] - \
                    Signal.lanes_timing[i] * 10
        Signal.update_timings(densities)

    @staticmethod
    def run_algo():
        algorithm()

    @staticmethod
    def simulate():
        gen_thread = threading.Thread(target=Simulator.gen_densities)
        algo_thread = threading.Thread(target=Simulator.run_algo)

        gen_thread.start()
        algo_thread.start()

        gen_thread.join()
        algo_thread.join()
