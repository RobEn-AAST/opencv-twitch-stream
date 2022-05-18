import cv2
import numpy as np

IMG_RES = (640, 480)
def scale_now(img1,img2):
    img1 = cv2.resize(img1, IMG_RES)
    img2 = cv2.resize(img2, (int(IMG_RES[0] / 2.5), int(IMG_RES[1] / 2.5)))

    rows, cols, channels = img2.shape
    row_main, col_main, channels_main = img1.shape

    roi = img1[row_main-rows: row_main, col_main-cols: col_main]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)

    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
    dst = cv2.add(img1_bg, img2_fg)
    img1[row_main-rows: row_main, col_main-cols: col_main] = dst

    return img1
