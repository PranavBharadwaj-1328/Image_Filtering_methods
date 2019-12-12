import matplotlib.pyplot as plt
import numpy as np
import cv2

def removewhitenoise():
  S = input('Enter Filename:')
  img = cv2.imread(S,0)
  kernel = np.ones((5,5),np.uint8)
  erosion = cv2.erode(img,kernel,iterations=1)
  plt.subplot(121),plt.imshow(img)
  plt.title("Orginal")
  plt.subplot(122),plt.imshow(erosion)
  plt.title("eroded")
  plt.show()

removewhitenoise()

