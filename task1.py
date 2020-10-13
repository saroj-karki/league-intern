import cv2

img = cv2.imread("task1.png")
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow("output", img)
low_value = (68, 72, 68)
high_value = (68, 72, 68)

imgfinal = cv2.inRange(hsv_img, low_value, high_value)
cv2.imshow("output", imgfinal)
cv2.waitKey(0)