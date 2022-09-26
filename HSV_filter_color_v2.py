import cv2
import numpy as np
vid = cv2.VideoCapture(0)

cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)
def on_trackbar(val):
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")




cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, on_trackbar)
cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)

HSV_avg=[100,100,100]
HSV_sum=[0,0,0]
HSV_count=[0,0,0]
ret, frame = vid.read()
frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
print(frameHSV)

imgtest=cv2.imread('img4.png')
imgtest= cv2.cvtColor(imgtest, cv2.COLOR_BGR2HSV)
cv2.imshow('imgHSV',imgtest)

def position(action, x, y, flags, *userdata):

    if action==cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        for i in range(3):
            HSV_sum[i]+=frameHSV[y][x][i]
            HSV_count[i]+=1
            HSV_avg[i]=HSV_sum[i]//HSV_count[i]
        print(frameHSV[y][x])
        print(HSV_avg)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    #frame=cv2.GaussianBlur(frame,(9,9),cv2.BORDER_DEFAULT)
    cv2.imshow('frame', frame)

    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV',frameHSV)
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    #lower = np.array([HSV_avg[0]-10, HSV_avg[1]+10, HSV_avg[2]-10])
    #upper = np.array([HSV_avg[0]+10, HSV_avg[1]-10, HSV_avg[2]+10])

    imgMASK = cv2.inRange(frameHSV, lower, upper)



    cv2.imshow('mask',imgMASK)
    cv2.setMouseCallback("HSV", position)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
