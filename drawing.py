import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow('Blank', blank)
# img = cv.imread('./Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# Color the image
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Green', blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

# Draw another rectangle - filled
# .rectangle(canvas, coordinates x, coordinate y, border color, thickness)
cv.rectangle(blank, (0, 0), (20, 20), (255, 0, 255), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw a circle
# .circle(canvas, center xy, radius, border, thickness)
cv.circle(blank, (250, 250), 30, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)


# Draw a line
# .line
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)


# Writing text
# putText(canvas, text, coordinates, face, scale, color, thickness, linetype)
cv.putText(blank, 'Hello', (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
