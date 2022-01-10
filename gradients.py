import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Gradients can be edge-like things in the image
# Different mathematically

# Two other ways to compute edges apart from Canny Edge detection

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Laplacian Method of Edge Detection
# Laplacian(src, data depth, )
lap = cv.Laplacian(gray, cv.CV_64F)

# Why this step? Essentially, when you transition from black to white and vice versa,
# you get a positive and negative slope
# so you need the absolute value of all pixel values as pixel values cannot be negative
# converted to uint8, the image specific datatype
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# Sobel Gradient Magnitude Representation
# Computes gradients in two directions
# Sobel(src, data depth, x direction, y direction)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

# Combined Sobel image
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)

cv.waitKey(0)
