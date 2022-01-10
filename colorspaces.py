import cv2 as cv

import matplotlib.pyplot as plt

# Image is by default read in BGR format
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Color spaces
# Space of colors, system of representing pixel of colors
# Default -> BGR


# Grayscale
# Show you distribution of pixel intensities at particular locations of your image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# HSV
# Hue saturation value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# LAB (L*A*B)
# more tuned to how humans perceive color
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# RGB is different from BGR. So, if you try to
# display this image in another library, it will
# be of an inverted color.
# Example:
# plt.imshow(img)
# plt.show()
# this shows a completely different image
# because Matplotlib thinks this is an RGB image
# so blue is red and red is blue

# Convert to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


# Converting back
# Cannot convert Grayscale to HSV directly.
# Have to convert Grayscale -> BGR -> HSV

# HSV -> BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV -> BGR', hsv_bgr)
# LAB -> BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB -> BGR', lab_bgr)


cv.waitKey(0)
