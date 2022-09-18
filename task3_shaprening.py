import cv2
import numpy as np
import matplotlib.pyplot as plt


img =cv2.imread('img1.png',0)
cv2.imshow('Original',img)
kernal=np.zeros((3,3),np.float32)

for i in range(3):
    for j in range(3):
        kernal[i][j]=-1/9

kernal[1][1]=2


img=cv2.filter2D(img,-1,kernal)

cv2.imshow('Sharp',img)
cv2.waitKey(0)




