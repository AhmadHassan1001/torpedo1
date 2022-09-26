import cv2
import numpy as np


src="test5.png"

img=cv2.imread(src)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



lowerRed = np.array([166, 70, 75])
upperRed = np.array([179, 255, 210])

lowerYellow = np.array([20, 150, 105])
upperYellow = np.array([31, 255, 220])

maskYellow = cv2.inRange(img_hsv, lowerYellow, upperYellow)
maskRed = cv2.inRange(img_hsv, lowerRed, upperRed)
mask=cv2.bitwise_or(maskRed,maskYellow)
cv2.imshow('mask', mask)

cv2.imshow('Original',img)
cv2.imshow('HSV',img_hsv)

img_masked=cv2.bitwise_and(img,img,mask=mask)

print(img.shape)
outputRed = cv2.connectedComponentsWithStats(maskRed, 4, cv2.CV_32S)
posRed=(-1,-1)
preposRed=(0,0)
cntRed=0
for i in range(1,outputRed[0]):
    if outputRed[2][i,cv2.CC_STAT_AREA]>300:
        print((int(outputRed[3][i][0]), int(outputRed[3][i][1])),outputRed[2][i,cv2.CC_STAT_AREA])
        #cv2.circle(img_masked, (int(outputRed[3][i][0]), int(outputRed[3][i][1])), 20, (0, i*20, 255-i*20), -1)
        preposRed = (preposRed[0]+int(outputRed[3][i][0]),preposRed[1]+int(outputRed[3][i][1]))
        cntRed+=1
if cntRed>0:
    posRed=(preposRed[0]/cntRed,preposRed[1]/cntRed)

print("posRed=",posRed)
cv2.circle(img_masked, (int(posRed[0]), int(posRed[1])), 20, (0,0, 255), -1)

outputYellow = cv2.connectedComponentsWithStats(maskYellow, 4, cv2.CV_32S)



posYellow=(-1,-1)
preposYellow=(0,0)
cntYellow=0
for i in range(1,outputYellow[0]):
    if outputYellow[2][i,cv2.CC_STAT_AREA]>300:
        print((int(outputYellow[3][i][0]), int(outputYellow[3][i][1])),outputYellow[2][i,cv2.CC_STAT_AREA])
        cv2.circle(img_masked, (int(outputYellow[3][i][0]), int(outputYellow[3][i][1])), 20, (0, i*20, 255-i*20), -1)
        preposYellow = (preposYellow[0]+int(outputYellow[3][i][0]),preposYellow[1]+int(outputYellow[3][i][1]))
        cntYellow+=1
if cntYellow>0:
    posYellow=(preposYellow[0]/cntYellow,preposYellow[1]/cntYellow)

print("posYellow=",posYellow)
cv2.circle(img_masked, (int(posYellow[0]), int(posYellow[1])), 20, (0,255, 255), -1)
cv2.imshow('OriginalMasked',img_masked)

imgOutput=np.zeros([img.shape[0],img.shape[1],3],dtype=np.uint8)
color1=(0,0,0)
if posYellow[0]<img.shape[1]//3 and posYellow[0]!=-1:
    color1=(0,255,0)
if posRed[0]<img.shape[1]//3  and posRed[0] != -1:
    color1=(color1[0],color1[1],255)
imgOutput=cv2.rectangle(imgOutput, (0,0), (img.shape[1]//3,img.shape[0]), color1, -1)
color2=(0,0,0)
if posYellow[0]>=img.shape[1]//3 and posYellow[0]<=2*img.shape[1]//3:
    color2=(0,255,0)
if posRed[0]>=img.shape[1]//3 and posRed[0]<=2*img.shape[1]//3:
    color2=(color2[0],color2[1],255)
imgOutput=cv2.rectangle(imgOutput, (img.shape[1]//3,0), (2*img.shape[1]//3,img.shape[0]), color2, -1)

color3=(0,0,0)
if posYellow[0]>=2*img.shape[1]//3:
    color3=(0,255,0)
if posRed[0]>=2*img.shape[1]//3:
    color3=(color3[0],color3[1],255)
imgOutput=cv2.rectangle(imgOutput, (2*img.shape[1]//3,0), (img.shape[1],img.shape[0]), color3, -1)


cv2.imshow('Output',imgOutput)

cv2.waitKey(0)




