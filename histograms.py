import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

# Histogram for grayscale images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# calcHist(image list, noOfChannels, mask, histSize [bins], ranges)
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale  Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# How masking affects histogram
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

gray_hist_2 = cv.calcHist([gray], [0], mask, [256], [0, 256])
plt.figure()
plt.title('Grayscale  Histogram with Mask')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist_2)
plt.xlim([0, 256])
plt.show()


# Calculate histogram for a color image


# Without mask
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)

plt.show()


# With mask

plt.figure()
plt.title('Color Histogram with Mask')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)

plt.show()

cv.waitKey(0)
