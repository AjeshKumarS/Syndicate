import cv2
import time
import urllib.request
import numpy as np
from ..signal import Signal


class Image:
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        (thresh, self.img) = cv2.threshold(base, 170, 255, cv2.THRESH_BINARY)
        self.height, self.width = self.img.shape
        self.pixelCount = self.height * self.width

    def getPixelCount(self):
        return self.pixelCount

    def getBlackPixelCount(self):
        return cv2.countNonZero(self.img)

    def getImage(self):
        return self.img


def getDensity(base, image):
    diff = cv2.subtract(base.getImage(), image.getImage())
    nonBlackPixels = cv2.countNonZero(diff)
    total = image.getPixelCount()
    density = (nonBlackPixels * 100) / total
    return density


def processLanes(n):
    densities = []
    for i in range(n):
        base = Image("./images/lane" + str(i + 1) + "/base.jpg")
        if base == None:
            print("Base image not found error")
            exit(0)
        image = Image("./images/lane" + str(i + 1) + "/2.jpg")
        if image == None:
            print("Image capture returned None")
            exit(0)
        density = getDensity(base, image)
        print("Density of lane " + str(i + 1) + ": " + str(density))
        densities.append(density)
    return densities


def takePhotos():
    CAMERA_URLS = [
        "http://192.168.43.220:8080/photo.jpg",
        "http://192.168.43.1:8080/photo.jpg",
        "http://192.168.43.231:8080/photo.jpg",
        "http://192.168.43.65:8080/photo.jpg",
    ]
    for url in CAMERA_URLS:
        res = urllib.request.urlopen(url)
        arr = np.asarray(bytearray(res.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        cv2.imwrite("./images/lane" + str(CAMERA_URLS.index(url) + 1) + "/2.jpg", img)
        # cv2.imshow("img", img)
        # cv2.waitKey()


def main():
    NUMBER_OF_LANES = 4
    while True:
        takePhotos()
        densities = processLanes(NUMBER_OF_LANES)
        Signal.update_timings(densities)
        time.sleep(Signal.IMAGE_PROCESSING_FREQUENCY)


if __name__ == "__main__":
    main()
