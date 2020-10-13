import cv2

def main():
	img = cv2.imread("task1.png")
	hsv_img = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	low_value = (68, 72, 68)
	high_value = (68, 72, 68)

	img_final = cv2.inRange(hsv_img, low_value, high_value)
	cv2.imshow("output", img_final)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()