import cv2
import numpy as np
import matplotlib.pyplot as plt

lst=[]
for i in range(4):
    lst.append(cv2.imread('img{i}.png'.format(i=i+1)))

f, axarr = plt.subplots(2,2)

for i in range(2):
    for j in range(2):
        axarr[i,j].imshow(lst[i*2+j])

plt.show()




