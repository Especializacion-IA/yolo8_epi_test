import sys
from ultralytics import YOLO
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# model upload
model = YOLO("runs/detect/train9/weights/best.pt")

# img path
image_path = sys.argv[1] if len(sys.argv) > 1 else "test_images/casco10.jpg"

# prediction
results = model(image_path, save=True)  # prediction path runs/detect/predict

# DataFrame reception
df = results[0].to_df()

if df.empty:
    print("Objects were not recognized.")
else:
    conteo = df['name'].value_counts()
    print("\n Object on the image:")
    print(conteo)

    persons = conteo.get('person', 0)
    print(f"\n Total people(person): {persons}")

    # Vizualization — img display
    from pathlib import Path
    import os

    # saveed image path
    filename = os.path.basename(image_path)
    save_dir = results[0].save_dir  # путь вроде runs/detect/predict10
    save_path = os.path.join(save_dir, filename)

    # read and display the saved image
    img = cv2.imread(save_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img_rgb)
    plt.title("Detection YOLOv8")
    plt.axis("off")
    plt.show()