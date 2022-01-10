import cv2 as cv
import numpy as np
import os

# Using OpenCV's built-in face recognizer
# We trained it in faces_train.py
# Saved it in face_trained.yml

# Load haar cascade classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Pre-load our saved features and labels
people = []
DIR = r'Resources/Faces/train'
for i in os.listdir(DIR):
    people.append(i)
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('Resources/Faces/val/ben_afflek/1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect face in image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces_rect:
    # Crop to region of interest
    faces_roi = gray[y:y+h, x:x+h]
    # Now, we can predict who the face is
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')
    cv.putText(img, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('Recognized person', img)

cv.waitKey(0)
