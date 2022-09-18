import cv2
import numpy as np
import matplotlib.pyplot as plt


img =cv2.imread('img1.png',0)
cv2.imshow('Original',img)
edge2=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)

edge2=cv2.Canny(edge2,100,200)
cv2.imshow('Edges2',edge2)
cv2.waitKey(0)

"""

Thresh 100 to 200 
because by trying 200 give strong edges
and 100 get the remaining weak but connected edges
"""


