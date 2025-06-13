# Real-Time Object Detection for Gesture Recognition

---

## Project Overview

This project focuses on developing and implementing a **real-time object detection system** for gesture recognition using the **YOLO (You Only Look Once)** architecture. The primary objective is to accurately identify and classify various human gestures in a live video feed, demonstrating the practical application of deep learning in human-computer interaction and surveillance.

---

## Methodology

### Model Selection and Training

The core of this system is a **YOLOv11n model**, a lightweight yet powerful variant of the YOLO series, chosen for its efficiency and suitability for real-time applications. The model was initialized with pre-trained weights to leverage existing knowledge and accelerate the training process.

The training dataset was meticulously prepared and organized, with images and corresponding labels structured for optimal compatibility with the YOLO framework. The dataset is located at `/content/drive/MyDrive/Extracted_Files/dataset/`. The training configuration utilized specific parameters:

* **Data Configuration:** The dataset's structure and class mappings were defined in a `data.yaml` file located at `/content/drive/MyDrive/Extracted_Files/data.yaml`.
* **Epochs:** The model was trained for 15 epochs, allowing it to iteratively refine its understanding of the gesture patterns.
* **Image Size:** Input images were resized to **960x960 pixels** during training to ensure consistent input dimensions and capture fine-grained details.
* **Project Directory:** All training results, including weights and logs, were systematically saved to `/content/drive/MyDrive/results_dl/exp`.

### Real-Time Inference

Following successful training, the optimized model, saved as `model.pt`, was deployed for real-time inference. A standard webcam was used as the input source. The live video stream was processed frame by frame. For each frame, the model performed object detection with the following parameters:

* **Image Size:** Similar to training, input frames for inference were resized to **960x960 pixels**.
* **Confidence Threshold:** A confidence threshold of **0.5** was applied, meaning only detections with a confidence score of 50% or higher were considered valid.
* **Bounding Box and Labeling:** Detected gestures were visually represented by bounding boxes drawn around the identified objects. Each bounding box was accompanied by the predicted class name, providing immediate visual feedback.

---

## Results

The training process yielded promising results, indicating the model's high capability in accurately detecting and classifying the defined gestures. Key performance metrics on the validation set are as follows:

### Overall Performance

* **Precision:** 88.2%
* **Recall:** 87.8%
* **mAP50 (mean Average Precision at IoU 0.5):** 87.6%
* **mAP50-95 (mean Average Precision across IoU thresholds from 0.5 to 0.95):** 79.6%

### Class-Specific Performance

The table below details the performance metrics for each detected gesture class.

| Class           | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
| :-------------- | :----- | :-------- | :----- | :---- | :---- | :------- |
| all             | 1200   | 2193      | 0.882  | 0.878 | 0.876 | 0.796    |
| Punch\_VFR      | 58     | 58        | 0.946  | 0.914 | 0.911 | 0.82     |
| Punch\_VFL      | 58     | 58        | 0.962  | 0.914 | 0.922 | 0.844    |
| One\_VFR        | 88     | 88        | 0.849  | 0.841 | 0.834 | 0.751    |
| One\_VFL        | 88     | 88        | 0.848  | 0.841 | 0.838 | 0.747    |
| Two\_VFR        | 87     | 87        | 0.797  | 0.908 | 0.871 | 0.793    |
| Two\_VFL        | 87     | 87        | 0.798  | 0.908 | 0.862 | 0.787    |
| Three\_VFR      | 70     | 70        | 0.874  | 0.9   | 0.886 | 0.824    |
| Three\_VFL      | 70     | 70        | 0.875  | 0.9   | 0.887 | 0.823    |
| Four\_VFR       | 80     | 80        | 0.938  | 0.812 | 0.824 | 0.762    |
| Four\_VFL       | 80     | 80        | 0.937  | 0.812 | 0.853 | 0.762    |
| Five\_VFR       | 70     | 70        | 0.864  | 0.929 | 0.894 | 0.827    |
| Five\_VFL       | 70     | 70        | 0.863  | 0.929 | 0.869 | 0.824    |
| Six\_VFR        | 83     | 83        | 0.854  | 0.867 | 0.855 | 0.784    |
| Six\_VFL        | 83     | 83        | 0.853  | 0.867 | 0.851 | 0.772    |
| Seven\_VFR      | 83     | 83        | 0.862  | 0.88  | 0.87  | 0.788    |
| Seven\_VFL      | 83     | 83        | 0.858  | 0.88  | 0.857 | 0.778    |
| Eight\_VFR      | 69     | 69        | 0.88   | 0.884 | 0.885 | 0.801    |
| Eight\_VFL      | 69     | 69        | 0.881  | 0.884 | 0.875 | 0.805    |
| Nine\_VFR       | 78     | 78        | 0.861  | 0.821 | 0.805 | 0.746    |
| Nine\_VFL       | 78     | 78        | 0.86   | 0.821 | 0.813 | 0.744    |
| Span\_VFR       | 75     | 75        | 0.873  | 0.853 | 0.876 | 0.78     |
| Span\_VFL       | 75     | 75        | 0.872  | 0.853 | 0.861 | 0.785    |
| Horiz\_HBL      | 74     | 74        | 0.934  | 0.838 | 0.881 | 0.782    |
| Horiz\_HFL      | 78     | 78        | 0.929  | 0.897 | 0.919 | 0.811    |
| Horiz\_HBR      | 78     | 78        | 0.928  | 0.897 | 0.919 | 0.833    |
| Horiz\_HFR      | 74     | 74        | 0.934  | 0.838 | 0.89  | 0.791    |
| Collab          | 68     | 68        | 0.849  | 0.941 | 0.925 | 0.82     |
| XSign           | 69     | 69        | 0.893  | 0.913 | 0.914 | 0.851    |
| TimeOut         | 70     | 70        | 0.895  | 0.914 | 0.948 | 0.842    |

* **Speed:** The inference speed was remarkably efficient, with approximately **0.3ms for preprocessing, 3.2ms for inference, and 2.6ms for postprocessing per image**. This low latency is crucial for maintaining real-time performance.

---

## Conclusion

This project successfully demonstrates the implementation of a **real-time gesture recognition system** using the **YOLOv11n model**. The high precision, recall, and mAP values, coupled with the impressive inference speed, underscore the system's effectiveness and its potential for various applications, including:

* **Touchless Interfaces:** Enabling interaction with devices without physical contact.
* **Gaming:** Enhancing immersive gaming experiences through gesture control.
* **Assisted Living:** Providing intuitive control for individuals with mobility challenges.
* **Security and Surveillance:** Identifying specific actions or signals.

Future work could involve expanding the gesture dataset, exploring more advanced YOLO architectures or other state-of-the-art object detection models, and optimizing the system for deployment on edge devices.
