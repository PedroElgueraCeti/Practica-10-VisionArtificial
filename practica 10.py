import cv2
import numpy as np

img_rgb = cv2.imread('circuitos.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(img_gray, 40, 0.01, 10)
corners = np.int0(corners)
   
for i in corners:
    x,y = i.ravel()
    cv2.circle(img_rgb, (x,y), 3, 255, -1)