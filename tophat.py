import cv2
import numpy as np
import matplotlib.pyplot as plt

def openimg():
    F = input()
    img = cv2.imread(F,0)
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
    plt.subplot(121),plt.imshow(img)
    plt.title('Original'),plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(opening)
    plt.title('Tophat image'),plt.xticks([]),plt.yticks([])
    plt.show()
openimg()

