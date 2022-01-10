import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
# threshold(src, thresholding value, maximum value, method)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Inverse thresholded image
threshold, thresh_inverse = cv.threshold(
    gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold', thresh_inverse)


# Adaptive Threshold
# Don't have to manually specify optimal threshold value
# adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# C value -> Integer subtracted from mean, to finetune threshold
# ADAPTIVE_THRESH_MEAN_C -> Mean of nearby cells
# ADAPTIVE_THRESH_GAUSSIAN_C -> Gaussian method to calculate mean, add weight

adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive threshold', adaptive_thresh)

cv.waitKey(0)
