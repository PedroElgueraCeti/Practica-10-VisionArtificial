import cv2
import numpy as np

img_rgb = cv2.imread('circuitos.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

