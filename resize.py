import cv2 as cv

# Rescale an existing video


def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = [width, height]
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Ca


def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
