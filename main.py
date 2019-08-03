import threading
from src.imageProcessing.image import main
from src.algorithm.algorithm import algorithm
from src.sound.sound import sound


if __name__ == "__main__":
    t1 = threading.Thread(target=algorithm)
    t2 = threading.Thread(target=main)
    t3 = threading.Thread(target=sound)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
