import cv2

# base = cv2.imread("./images/lane1/base.jpg")
base = cv2.imread("./base.jpg")
base = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
cv2.imshow("base", base)
cv2.waitKey()
(thresh, base) = cv2.threshold(base, 170, 255, cv2.THRESH_BINARY)
cv2.imshow("base", base)
cv2.waitKey()

# img = cv2.imread("./images/lane1/2.jpg")
img = cv2.imread("./photo.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img", img)
cv2.waitKey()
(thresh, img) = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img)
cv2.waitKey()

diff = cv2.subtract(base, img)
cv2.imshow("diff", diff)
cv2.waitKey()
