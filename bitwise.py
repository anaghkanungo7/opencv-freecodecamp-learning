import cv2 as cv
import numpy as np

# Bitwise operators
# Like in C++ / C
# AND XOR NOT

# Create blank canvas
blank = np.zeros((400, 400), dtype='uint8')

# Draw white filled rectangle
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# Draw white filled circle
circle = cv.circle(blank.copy(), (200, 200), (200), 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


# Bitwise AND
# Returns intersection
# bitwise_and(src1, src2)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_and', bitwise_and)


# Bitwise OR
# Returns union (non-intersecting and intersecting regions)
# bitwise_or(src1, src2)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_or', bitwise_or)

# Bitwise XOR
# Returns non-intersecting regions
# bitwise_xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_XOR', bitwise_xor)

# Bitwise NOT
# Inverts binary color (w->b, b->w)
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise_NOT', bitwise_not)


cv.waitKey(0)
