
import cv2 as cv
import numpy as np


img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation - Shifting an image along x and y axis
#  Shifting an image along x axis and y axis.
# Shift image up, down, left, right


def translate(img, x, y):
    # Create translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    # dimensions = (width, height)
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> translate to Left
# -y -> translate to Up
# +x -> translate to Right
# +y -> translate to Down


# Shift image right and down by 100px
translated = translate(img, 100, 100)
cv.imshow('Translate', translated)

# Example use case: Adding GUI to the image after translation
# cv.rectangle(translated, (0, 0), (100, 100), (0, 255, 255), thickness=2)
# cv.imshow('Translate', translated)


# Rotation
# +ve angle -> Counterclockwise
# -ve angle -> Clockwise
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        # Assume that we are rotating around center
        rotPoint = (width // 2, height // 2)

    # Create rotation matrix
    # cv.getRotationMatrix2D(point, angle, scale)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Flipping
# cv.flip(src, flipCode, dst)
# flipCode 0 -> vertical flip
# flipCode 1 -> horizontal flip
# flipCode -1 -> both vertical and horizontal
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

# Cropping and Resizing have been discussed in previous files:
# Resizing -> resizing.py
# Cropping -> essentialfunctions.py


cv.waitKey(0)
