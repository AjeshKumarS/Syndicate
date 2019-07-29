import cv2
import time
from ..signal import Signal


class Image:
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.height, self.width = self.img.shape
        self.pixelCount = self.height * self.width

    def getPixelCount(self):
        return self.pixelCount

    def getBlackPixelCount(self):
        return cv2.countNonZero(self.img)

    def getImage(self):
        return self.img


def getDensity(base, image):
    diff = cv2.subtract(image.getImage(), base.getImage())
    nonBlackPixels = cv2.countNonZero(diff)
    total = image.getPixelCount()
    density = (nonBlackPixels * 100) / total
    return density


def processLanes(n):
	densities = []
    for i in range(n):
        base = Image("./images/lane" + str(i + 1) + "/base.png")
        if base == None:
            print("Base image not found error")
            exit(0)
        image = Image("./images/lane" + str(i + 1) + "/1.png")
        density = str(getDensity(base, image))
        print("Density of lane " + str(i + 1) + ": " + density)
        densities.append(density)
        # Delete 1.png
	return densities


def takePhotos():
    cameras = [0]
    for i in cameras:
        camera = cv2.VideoCapture(i)
        if camera == None:
            print("Camera not detected error")
            exit(0)
        _, img = camera.read()
        cv2.imwrite(
            "./images/lane" + str(i + 1) + "/2.png", img
        )  # CHANGE TO 1.png for final use
        # cv2.imshow("test", img)
        # cv2.waitKey(0)
        del camera


def main():
    NUMBER_OF_LANES = 4
    INTERVAL_BETWEEN_SUCCESSIVE_CAPTURE = 5
    while True:
		takePhotos()
		densities = processLanes(NUMBER_OF_LANES)
		for i in densities:
			Signal.update_timings(i)
		time.sleep(INTERVAL_BETWEEN_SUCCESSIVE_CAPTURE)


if __name__ == "__main__":
    main()
