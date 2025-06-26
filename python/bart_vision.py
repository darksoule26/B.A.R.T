# bart_vision.py
from ultralytics import YOLO
import cv2

def start_object_detection():
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    print("🎥 Bart's Object Detection Started - Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)[0]

        for r in results.boxes:
            x1, y1, x2, y2 = map(int, r.xyxy[0])
            label = results.names[int(r.cls[0])]
            conf = r.conf[0]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Bart's Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
