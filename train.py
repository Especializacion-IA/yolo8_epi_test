from ultralytics import YOLO

# download YOLOv8 pretrained model
model = YOLO("yolov8n.pt")

# train the model with local dataset
model.train(data="dataset/data.yaml", epochs=30, imgsz=640)