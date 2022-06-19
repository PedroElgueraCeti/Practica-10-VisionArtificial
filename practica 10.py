import cv2
import numpy as np

img_rgb = cv2.imread('R.png')
img_rgb=cv2.resize(img_rgb,(400,300))
img_original = cv2.imread('R.png')
img_original=cv2.resize(img_original,(400,300))
hh, ww = img_rgb.shape[:2]

# threshold on white
# Define lower and uppper limits
lower = np.array([200, 200, 200])
upper = np.array([255, 255, 255])

# Create mask to only select black
thresh = cv2.inRange(img_rgb, lower, upper)

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# invert morp image
mask = 255 - morph

# apply mask to image
result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
img_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img_gray, 40, 0.01, 10)
corners = np.int0(corners)
   
for i in corners:
    x,y = i.ravel()
    cv2.circle(img_rgb, (x,y), 3, 255, -1)

cv2.imshow('Original',img_original)
cv2.imshow('Sin fondo',result)
cv2.imshow('Esquinas',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()