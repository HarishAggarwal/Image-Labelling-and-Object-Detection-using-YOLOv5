# Image Labeling and Object Detection Using YOLOv5

This repository contains a project that involves manually labeling images using [Label Studio](https://labelstud.io/) and training an object detection model using YOLOv5. The repository includes scripts for collecting and labeling images, as well as for using a trained YOLOv5 model for real-time object detection.

---

## Features

- **Image Collection**: Script for capturing images and organizing them into labeled folders.
- **Manual Image Labeling**: Use Label Studio to manually annotate the collected images.
- **Object Detection**: Real-time object detection using a custom-trained YOLOv5 model.

---

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.8+
- OpenCV
- PyTorch
- Label Studio
- Matplotlib
- YOLOv5 repository

---

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Image Collection

Run the `app.py` script to capture images using your webcam. Images will be saved in the `data/images` directory, organized by labels.

```bash
python app.py
```

Follow the prompts to capture images for each label.

---

### 2. Image Labeling

Use [Label Studio](https://labelstud.io/) for manual labeling of images:

1. Install Label Studio:

   ```bash
   pip install label-studio
   ```

2. Start Label Studio:

   ```bash
   label-studio
   ```

3. Navigate to `http://localhost:8080` in your browser and upload the images from the `data/images` directory.

4. Label the images and export the annotations in YOLO format.

---

### 3. Creating the `dataset.yaml` File

The `dataset.yaml` file is required for training the YOLOv5 model. It specifies the paths to the dataset and the class labels.

1. Open a text editor and create a file named `dataset.yaml`.
2. Add the following content, replacing `<your_dataset_path>` with the actual path to your dataset:

   ```yaml
   train: <your_dataset_path>/train/images
   val: <your_dataset_path>/val/images

   nc: <number_of_classes>
   names: ['class1', 'class2', 'class3']  # Replace with your class labels
   ```

   - **`train`**: Path to the training images folder.
   - **`val`**: Path to the validation images folder.
   - **`nc`**: Number of classes in your dataset.
   - **`names`**: List of class labels.

3. Save the file as `dataset.yaml` in the YOLOv5 directory.

Example:

```yaml
train: data/images/train
val: data/images/val

nc: 2
names: ['awake', 'drowsy']
```

---

### 4. Training the YOLOv5 Model

To train your YOLOv5 model:

1. Clone the YOLOv5 repository:

   ```bash
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```

2. Organize your labeled dataset into `train` and `val` directories.

   ```
   data/
   ├── train/
   │   └── images/
   │       ├── awake/
   │       └── drowsy/
   └── val/
       └── images/
           ├── awake/
           └── drowsy/
   ```

3. Place the `dataset.yaml` file in the YOLOv5 directory.

4. Train the model:

   ```bash
   python train.py --img 640 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt --cache
   ```

5. Save the trained weights (`last.pt`) to the `yolov5/runs/train/exp*/weights/` directory.

---

### 5. Real-Time Object Detection

Run the `index.py` script to use the trained YOLOv5 model for real-time object detection.

```bash
python index.py
```

Press `q` to quit the webcam feed.

---

## Commands Overview

| Command                                | Description                              |
|----------------------------------------|------------------------------------------|
| `python app.py`                        | Collect labeled images.                 |
| `label-studio`                         | Launch the Label Studio interface.      |
| `python index.py`                      | Run real-time object detection.         |
| `python train.py`                      | Train the YOLOv5 model.                 |

---

## Directory Structure

```
.
├── data/
│   └── images/
│       ├── awake/
│       └── drowsy/
├── app.py
├── index.py
├── yolov5/
│   └── runs/train/exp*/weights/
├── requirements.txt
└── README.md
```

---

## Notes

- Ensure your webcam is properly configured and accessible for `app.py` and `index.py`.
- For best results, use a balanced dataset with diverse examples for each label.
- Make sure to adjust the YOLOv5 configuration files to suit your dataset and hardware capabilities.

---

## Contributing

Feel free to submit issues and pull requests to improve this project. Contributions are always welcome!

---

## License

This project is licensed under the [MIT License](LICENSE).
