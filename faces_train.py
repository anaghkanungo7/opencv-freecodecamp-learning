import os
import cv2 as cv
import numpy as np

# Initialize list of people using os
people = []
DIR = r'Resources/Faces/train'
for i in os.listdir(DIR):
    people.append(i)

print(people)
haar_cascade = cv.CascadeClassifier('./haar_face.xml')

# Training set will consist of two lists
# Features -> Image array of faces
features = []
labels = []

# Corresponding Label -> Whose face is it, label the image


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        print(path)
        # Label is the index of that particular list
        label = people.index(person)

        for img in os.listdir(path):
            image_path = os.path.join(path, img)
            # Read image from path
            img_array = cv.imread(image_path)
            # Grayscale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, 1.1, 4)

            for (x, y, w, h) in faces_rect:
                # Crop out faces in the image in the face "region of interest"
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print("Training done.")
print(f'Length of features list: = {len(features)}')
print(f'Length of labels list: = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

# Create recogniser
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Now, train our recogniser on features and labels
face_recognizer.train(features, labels)

# Save our trained algorithm for later
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)

# Face recogniser is trained now.
