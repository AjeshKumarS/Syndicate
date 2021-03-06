import threading
import sys
from src.imageProcessing.image import main
from src.algorithm.algorithm import run_algorithm
from src.sound.sound import sound
from src.simulator.simulator import Simulator

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-sim":
        Simulator.simulate()
    elif len(sys.argv) > 1 and sys.argv[1] == "-perf":
        Simulator.simulate_with_perf()
    elif len(sys.argv) > 1 and sys.argv[1] == "-visuals":
        # The flask server MUST be running to use this option
        Simulator.simulate_with_visuals()
    else:
        t1 = threading.Thread(target=run_algorithm)
        t2 = threading.Thread(target=main)
        t3 = threading.Thread(target=sound)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
