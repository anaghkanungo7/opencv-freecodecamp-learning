import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Park', img)

# In a kernel (nxn grid), blur happens as a result of the pixels around it.
# Blur -> Smooth out image to reduce noise

# Averaging
# Define a kernel window (divide pic into nxn grids) -> Compute pixel intensity of middle pixel as average of surrounding grid -> happens throughout the image
# Higher kernel size -> more blur
average = cv.blur(img, (3, 3))
cv.imshow('Average', average)


# Gaussian Blur
# Instead of computing average of surrounding pixels, each surrounding pixel is given a particular weight -> Average of those weights is the pixel intensity
# Less blur as compared to averaging method, more natural
# cv.GaussianBlur(img, (kernel), std dev in x direction)
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gauss', gauss)

# Median Blur
# Instead of average of surrounding pixels, it finds the median
# Tends to be more effective in reducing noise as compared to averaging and gaussian blur
# Used in advanced CV projects that depend on reduction of noise
# .medianBlur(img, int kernel)
# Generally not suitable for high kernel sizes
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)


# Bilateral blurring
# Most effective, used in advanced CV projects
# How it blurs: It applies blurring but retains the edges in the image. Traditional methods do not consider edges when blurring.
# bilateralFilter(img, diameter, sigma Color, sigma space)
# sigma space -> you want pixels from x distance far away to influence computation of blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)
