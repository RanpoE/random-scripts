from ultralytics import YOLO
import cv2 as cv

video_path = 'VideoFiles/cats.mp4'  # Change file location
capture = cv.VideoCapture(video_path)  # video file or device camera

model = YOLO('yolo-weights/yolov8n.pt')

while True:
    success, frame = capture.read()
    result = model(frame, stream=True, show=True)
    for r in result:
        boxes = r.boxes
        for box in boxes:
            label = model.names.get(box.cls.item())
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv.putText(frame, label, (x1, y1 + 20),
                       cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    cv.imshow('Video', frame)
    cv.waitKey(1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
