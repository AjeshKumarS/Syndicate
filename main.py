import threading
import sys
from src.imageProcessing.image import main
from src.algorithm.algorithm import algorithm
from src.sound.sound import sound
from src.simulator.simulator import Simulator


if __name__ == "__main__":
    if sys.argv[1] == "-sim":
        Simulator.simulate()
    else:
        t1 = threading.Thread(target=algorithm)
        t2 = threading.Thread(target=main)
        t3 = threading.Thread(target=sound)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
