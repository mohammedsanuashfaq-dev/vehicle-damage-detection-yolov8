from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Video paths
input_video = "videos/test.mp4"
output_video = "outputs/output.mp4"

cap = cv2.VideoCapture(input_video)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    results = model(frame, conf=0.5)

    annotated_frame = results[0].plot()

    out.write(annotated_frame)

    cv2.imshow("Vehicle Damage Detection", annotated_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved successfully!")