import cv2

img = cv2.imread("task1.png")

# cv2.imshow("output", img)
low_value = (68, 72, 68)
high_value = (68, 72, 68)

imgfinal = cv2.inRange(low_value, high_value)
cv2.imshow("output", imgfinal)
cv2.waitKey(0)