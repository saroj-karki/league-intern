import cv2

img = cv2.imread("task1.png")

cv2.imshow("output", img)
cv2.inRange(68, 72, 68)
cv2.waitKey(0)