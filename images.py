# Required imports
import cv2 as cv

# Read image
img = cv.imread('Resources/Photos/cat.jpg')

# Show image as matrix of pixels
# cv.imshow(nameOfWindow, matrixOfPixels)
cv.imshow('Cat', img)
# Wait for a specific delay for a key to be pressed - 0 is infinite time
cv.waitKey(0)


# Reading large image
# img2 = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat2', img2)
# cv.waitKey(0)
