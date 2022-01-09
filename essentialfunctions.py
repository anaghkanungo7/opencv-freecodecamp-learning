import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Gaussian Blue
# .gaussianBlur(source, kernel size, ?)
# Increase kernel size to increase blur strength
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Edge Cascade
# Trying to find edges in the image
# we will use Canny edge detector
# .canny(source, threshold1, threshold2)
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
# Reduce edges by applying blur
canny2 = cv.Canny(blur, 125, 175)
cv.imshow('Canny3', canny2)


# Dilating
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated', dilated)


# Eroding (reverse dilation to get back edge cascades)
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
