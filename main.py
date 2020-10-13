import cv2

def main():
    '''Main function of the script'''

    img = cv2.imread('task1.png')
    low_value = (68, 72, 68)
    high_value = (68, 72, 68)
    img_final = cv2.inRange(img, low_value, high_value)
    cv2.imshow('output', img_final)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()