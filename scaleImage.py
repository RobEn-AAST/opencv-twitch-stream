import cv2
import numpy as np

IMG_RES = (640, 480)

img_tst1 = cv2.imread('3.jpg')
img_tst2 = cv2.imread('2.jpg')

def scale_now(img1,img2):
    img1 = cv2.resize(img1, IMG_RES)
    img2 = cv2.resize(img2, (int(IMG_RES[0] / 2.5), int(IMG_RES[1] / 2.5)))

    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)

    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols] = dst

    cv2.imshow('res', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img1


scale_now(img_tst1, img_tst2)