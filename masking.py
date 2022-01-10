# Masking using Bitwise operators
import cv2 as cv
import numpy as np


img = cv.imread('Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

# Masking
# Allows us to focus on certain parts of the image

# Dimensions of mask have to be same as that of image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

# Create a circle in the mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0] // 2), 100, 255, -1)
cv.imshow('Mask', mask)

# Juxtapose aka Mask the image
# bitwise_and(src1, src2, mask)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)


cv.waitKey(0)
