import cv2 as cv

video_path = 'VideoFiles/cats.3gpp'
capture = cv.VideoCapture(video_path)  # video file or device camera


while True:
    success, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
