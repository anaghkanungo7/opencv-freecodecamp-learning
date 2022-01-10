import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    haar_cascade = cv.CascadeClassifier('./haar_face.xml')
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 8)
    print("Number of faces found: " + str(len(faces_rect)))
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame, str(len(faces_rect)), (10, 60),
                   cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


# Delete capture pointer and free memory
capture.release()
cv.destroyAllWindows()
