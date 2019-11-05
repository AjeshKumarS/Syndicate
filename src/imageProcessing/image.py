import cv2
import time
import urllib.request
import numpy as np
# from ..config import CAMERA_URLS
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
    # pass
    # THIS CODE TAKES A PICTURE THROUGH DEFAULT CAMERA
    # COMMENTED OUT FOR NOW SO RANDOM PICTURES OF YOU ARE NOT TAKEN EVERY TIME THE CODE IS RUN
    # cameras = [0]
    # for i in cameras:
    #     camera = cv2.VideoCapture(i)
    #     if camera == None:
    #         print("Camera not detected error")
    #         exit(0)
    #     _, img = camera.read()
    #     cv2.imwrite(
    #         "./images/lane" + str(i + 1) + "/2.png", img
    #     )  # CHANGE TO 1.png for final use
    #     # cv2.imshow("test", img)
    #     # cv2.waitKey(0)
    #     del camera
    CAMERA_URLS=["http://192.168.43.220:8080/photo.jpg","http://192.168.43.1:8080/photo.jpg", "http://192.168.43.231:8080/photo.jpg","http://192.168.43.65:8080/photo.jpg"]
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
