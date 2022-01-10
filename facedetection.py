"""
Face Detection
- Recognising whether a face is present. Different from face recognition
- Happens using classifiers trained on images to classify images as positive or negative, based on whether it detects a face in the image or not.
- OpenCV comes with pre-trained classifiers that we can use in any program.
- Two main classifiers 
    1. Haar cascades
    2. Local binary patterns (more advanced haar cascades, not as prone to noise)
- You can find Haar cascades in OpenCV's Haar cascade classifier
"""

import cv2 as cv
img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Person', img)

img2 = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Group', img2)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray2)

# Crating haar Cascade variable
# CascadeClassifier(src of xml file containing haar classifier)
haar_cascade = cv.CascadeClassifier('./haar_face.xml')

# haar_cascade_detectMultiScale(src, scaleFactor, minNeighbours, flags, minSize, maxSize)
# minNeighbours -> Number of neighbours a rectangle needs to have to be called a face
# This function returns rectangular coordinates of that face as a list to faces_rect
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)
print("Number of faces found: " + str(len(faces_rect)))

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Detected image', img)


# Second example
faces_rect_2 = haar_cascade.detectMultiScale(gray2, 1.1, 1)
print("Number of faces found: " + str(len(faces_rect_2)))

for (x, y, w, h) in faces_rect_2:
    cv.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 1)

cv.imshow('Detected image 2', img2)

# group_2.jpg details
# No of faces found -> 7
# No of actual faces -> 5
# Detected stomach and part of a neck... lol
# Finetune by modifying scale factor and minimum neighbours
# Increasing min_neighbours -> More accurate / less sensitive


cv.waitKey(0)
