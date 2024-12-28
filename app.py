import os
import cv2
import time
import uuid

Images_Path = os.path.join('data', 'images')
labels = ['awake', 'drowsy']
total_images = 5

os.makedirs(Images_Path, exist_ok=True)

cap = cv2.VideoCapture(0)

try:
    for label in labels:
       
        label_path = os.path.join(Images_Path, label)
        os.makedirs(label_path, exist_ok=True)
        
        print("Collecting images for {}".format(label))
        time.sleep(5)
        
        for img_num in range(total_images):
            print("Collecting images for {}, image number {}".format(label, img_num))
            
            ret, frame = cap.read()
            
            if not ret:
                print("Failed to capture image. Skipping...")
                continue
            
            imgname = os.path.join(label_path, label + '.' + str(uuid.uuid1()) + '.jpg')
            cv2.imwrite(imgname, frame)
            
            time.sleep(2)
            
finally:
    cap.release()
    cv2.destroyAllWindows()
