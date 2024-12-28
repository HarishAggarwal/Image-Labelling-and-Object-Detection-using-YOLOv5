import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp5/weights/last.pt', force_reload=True)

# file_path = os.path.join('data', 'images', '0d1c43fd-awake.75c4381d-c470-11ef-81d9-8e43eba8ae05.jpg')
# results = model(file_path)

# results.print()  # Prints detected objects
# results.show()   # Shows the image with bounding boxes


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
     
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()