# BumpAlert: Speed Breaker Detection System

**BumpAlert** is a computer vision project designed to detect painted and unpainted speed breakers on roads using deep learning (YOLOv5). The system helps in real-time detection of speed breakers, which can be used in traffic management systems, smart navigation apps, and autonomous vehicles.

## Features
- Detect painted and unpainted speed breakers in real-time.
- Uses YOLOv5 for object detection.
- Provides bounding boxes on images with detected speed breakers.

## Installation

### Prerequisites:
- Python 3.8+
- pip (Python package installer)
- **Clone YOLOv5** repository from [Ultralytics YOLOv5 GitHub](https://github.com/ultralytics/yolov5) before running the system.

### Steps to Set Up:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/BumpAlert.git
    cd BumpAlert
    ```

2. Clone the YOLOv5 repository:
    ```bash
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Batch Size Note:
- **Batch Size**: The default batch size used for training is `16`. You can adjust this value based on the GPU memory available. For lower GPU memory, use `batch-size 2` to avoid out-of-memory errors during training or inference.

## Usage

### Running the Model:
1. After completing the setup, you can run the model using the following command:
    ```bash
    python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --img 640 --source path_to_image_or_video
    ```

2. You can change the image size (default is `640`) and batch size (e.g., `--batch-size 2` for low-memory devices).

### Running the Tkinter UI:
1. Run the Tkinter UI to upload an image and display the output with bounding boxes:
    ```bash
    python ui.py
    ```

2. The application allows the user to upload an image, run inference, and display the resulting image with bounding boxes around detected speed breakers.

## Folder Structure

```
BumpAlert/
│
├── yolov5/                  # YOLOv5 model and repository (cloned from GitHub)
│   ├── models/               # YOLOv5 models for training and inference
│   ├── utils/                # YOLOv5 utilities for data loading, preprocessing, etc.
│   ├── detect.py             # YOLOv5 inference script
│   ├── train.py              # YOLOv5 training script
│   └── requirements.txt      # Dependencies for YOLOv5
│
├── Speed_breaker_dataset-2/  # Dataset for training (if included in your project)
│   ├── train/                # Training images and labels
│   ├── valid/                # Validation images and labels
│   └── test/                 # Test images and labels
│
├── runs/                     # YOLOv5 results folder (inference and training results)
│   ├── train/                # Training results (model checkpoints, logs)
│   ├── detect/               # Detection results (images with bounding boxes)
│   └── exp/                  # Experiment folder for output images
│
├── ui.py                     # Tkinter UI for uploading images and displaying results
├── requirements.txt          # Python dependencies for the project
├── .gitignore                # Git ignore file to exclude unnecessary files
└── README.md                 # This file
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
