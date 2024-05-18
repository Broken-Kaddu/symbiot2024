
import cv2
import numpy as np
from ultralytics import YOLO
import os
import time

model = YOLO("yolo-Weights/yolov8s.pt", verbose=False)
FALL_THRESHOLD = 40

cap = cv2.VideoCapture(0)
fall_detected = False
fall_start_time = 0

while True:
    ret, frame = cap.read()
    results = model.predict(frame, verbose=False)
    for result in results:
        class_id = int(result.boxes.cls[0])
        confidence = result.boxes.conf[0]
        if class_id == 0 and confidence > 0.5:
            x1, y1, x2, y2 = result.boxes.xyxy[0]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            box_height = y2 - y1
            box_width = x2 - x1

            if box_width < box_height * 0.5:
                if not fall_detected:
                    fall_start_time = time.time()
                    fall_detected = True

            if fall_detected and time.time() - fall_start_time > 5:
                print("Fall detected")
                
                os.system("python sms_script.py")
                
                os.system("python arduino_script.py")
                fall_detected = False

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
