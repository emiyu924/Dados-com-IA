from ultralytics import YOLO

model = YOLO("yolov9n.pt")
model.predict(source=0, show=True)
