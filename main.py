import cv2
from ultralytics import YOLO
import time

# 加载YOLO模型
model = YOLO("models/yolov8n.pt")

cap = cv2.VideoCapture(0)

start_time = time.time()

print("LHY AI Vision System")
print("Neural Network Loading...")
print("YOLO Detection Activated")

while True:

    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    # HUD标题
    cv2.putText(
        annotated,
        "AI VISION SYSTEM",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    # 扫描提示
    cv2.putText(
        annotated,
        "SCANNING...",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,0),
        2
    )

    # 运行时间
    uptime = int(time.time() - start_time)

    cv2.putText(
        annotated,
        f"UPTIME: {uptime}s",
        (20,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0,255,0),
        2
    )

    # 目标检测提示
    if len(results[0].boxes) > 0:
        cv2.putText(
            annotated,
            "TARGET DETECTED",
            (20,160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,0,255),
            2
        )

    cv2.imshow("AI Vision System", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()