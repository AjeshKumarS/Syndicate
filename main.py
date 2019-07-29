import threading
from src.image.image import image
from src.algorithm.algorithm import algorithm


if __name__ == "__main__":
	t1 = threading.Thread(target=algorithm)
	t2 = threading.Thread(target=image)
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
