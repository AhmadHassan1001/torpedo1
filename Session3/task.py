import cv2
import numpy as np


src="test4.png"

img=cv2.imread(src)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)


def on_trackbar(val):
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    mask = cv2.inRange(img_hsv, lower, upper)
    cv2.imshow('mask', mask)


cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, on_trackbar)
cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)

hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")
while True:

    cv2.imshow('Original',img)
    cv2.imshow('HSV',img_hsv)



    cv2.waitKey(1)


