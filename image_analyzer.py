from ultralytics import YOLO
import cv2


model = YOLO('yolo-weights/yolov8n.pt')


def analyze_img(file_path):
    results = model(file_path)
    name_list = model.names

    items = {}
    for r in results:
        boxes = r.boxes

        for box in boxes:
            label = str(name_list.get(box.cls.item()))

            items[label] = items[label] + 1 if items.get(label) else 1

        if cv2.waitKey(20) & 0xFF == ord('d'):
            cv2.destroyAllWindows()

    cv2.waitKey(0)
    print(items)


analyze_img("ImageFiles/convo.jpg")
