import cv2 as cv

import numpy as np

"""
What are contours?
- Boundaries of objects.
- Line or curve that joins points along boundary.
- Contours are edges, but from a math perspective
they are not.
- Contours are useful for shape analysis, object detection
and recognition.
- 
"""

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Method 1: Use Blur and Canny Edge

# # Blur
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Grab edges of image using canny
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)


# Method 2: Use Threshold function
# cv.threshold(canvas, lower limit, upper limit, type)
# Binarise the image. If pixel is below 125 -> white, above 225 -> white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
# Disadvantage -> Not exactly the best, may lose accuracy.


# To visualize contours
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Finding Contours
# findContours(edges, mode, approximation method, contours)
# mode cv.RETR_TREE -> All hierarchical contours
# mode cv.RETR_EXTERNAL -> only external contours
# mode cv.RETR_LIST -> All contours

# approximation cv.CHAIN_APPROX_NONE -> Does nothing. just returns all contours
# approximation cv.CHAIN_APPROX_SIMPLE -> returns a compressed value of contours


# contours -> Python list of coordinates of contours
# hierarchies -> hierarchical representation of contours

# Method 1
# contours, hierarchies = cv.findContours(
#     canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# Method 2
contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# 2794 before blurring, 380 after blurring
print(str(len(contours)) + " contours are found")
# 839 using Thresh... threshold seems very accurate.

# Visualize contours by drawing over the image -> Numpy (blank) array needed
# drawContours(canvas, contour list, noOfContours [all=-1], color, thickness)
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)
