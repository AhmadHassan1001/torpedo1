import cv2
import numpy as np
import matplotlib.pyplot as plt


img =cv2.imread('img1.png',0)
img[img<100]=0
cv2.imshow('Thresh',img)
cv2.waitKey(0)




