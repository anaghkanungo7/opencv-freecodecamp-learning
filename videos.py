# Required imports
import cv2 as cv

# Video
capture = cv.VideoCapture(0)
print(type(capture))
while True:
    #     Read video frame by frame - returns frame and bool
    isTrue, frame = capture.read()
    print(type(frame))
    #     Reference a particular frame
    cv.imshow('Video', frame)
    #     Prevent it from playing indefinitely - as soon as "D" key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

    #     If you get -215:Assertion error -> opencv could not find more frames

# Delete capture pointer and free memory
capture.release()
cv.destroyAllWindows()
