# Real-Time Gesture Recognition System using YOLOv11n

---

## 1. Project Overview

This project presents a robust **real-time object detection system** specifically designed for **gesture recognition**. Leveraging the advanced **YOLO (You Only Look Once) architecture**, the system aims to accurately identify and classify various human gestures within a live video stream. This research demonstrates the practical application of deep learning in critical domains such as human-computer interaction, accessible technology, and surveillance.

---

## 2. Data and Project Structure

All requisite project data, encompassing the meticulously curated dataset for model training and the essential `data.yaml` configuration file, are systematically organized and hosted on Google Drive to facilitate seamless access and collaborative development.

### 2.1. Google Drive Data Organization

The primary Google Drive directory, accessible via: `https://drive.google.com/drive/folders/1Npll7i7y0y5tb7Yn9G0hIxEsn4U1Bb2f?usp=sharing`, comprises the following key components:

* **`Extracted_Files/`**: This crucial directory encapsulates the core dataset and associated configuration files.
    * **`data.yaml`**: This YAML file serves as the definitive configuration for the dataset. It precisely maps the locations of training and validation image and label directories, specifies the total number of distinct classes (`nc`), and enumerates the corresponding class names (`names`).
        * **`data.yaml` Format Structure**:
            ```yaml
            train: ../path/to/train/images
            val: ../path/to/val/images
            nc: <number_of_classes>
            names: ['class_name_1', 'class_name_2', ...]
            ```
            This structure is paramount for the YOLO framework to correctly parse and utilize the dataset during the training phase.
    * **`dataset/`**: This hierarchical folder contains the raw image and label files, structured in accordance with YOLO's expected input format.
        * **`images/`**: Contains the raw image files.
            * **`train/`**: Images allocated for model training.
            * **`val/`**: Images designated for model validation.
        * **`labels/`**: Contains the YOLO-formatted `.txt` annotation files, with bounding box coordinates and class IDs corresponding to each image.
            * **`train/`**: Labels for training images.
            * **`val/`**: Labels for validation images.
* **`results_dl/`**: This directory is the designated repository for all outputs generated during the model training process. This includes trained model weights, comprehensive training logs, and various performance metrics.
    * **`exp/`**: A dynamically generated sub-directory for each experimental run, ensuring organized storage of specific training outcomes.

---

## 3. Methodology

### 3.1. Model Selection and Training Regimen

The foundational element of this real-time gesture recognition system is the **YOLOv11n model**. This variant of the YOLO architecture was strategically selected due to its inherent efficiency and high suitability for deployment in real-time inference scenarios. To expedite the learning process and leverage pre-existing visual knowledge, the model was initialized with pre-trained weights.

The training process was meticulously configured with the following parameters:

* **Data Configuration Source:** The `data.yaml` file, residing within the `Extracted_Files` directory on Google Drive, served as the authoritative source for dataset structure and class mapping.
* **Training Epochs:** The model underwent training for **15 epochs**. This iterative process enabled the model to progressively refine its internal representations and optimize its ability to discern intricate gesture patterns.
* **Input Image Resolution:** To ensure consistent input and facilitate the capture of granular visual features, all input images were uniformly resized to **960x960 pixels** during the training phase.
* **Result Persistence:** All training artifacts, including finalized model weights and detailed execution logs, were systematically archived within the `results_dl/exp` directory in the Google Drive.

### 3.2. Real-Time Inference Protocol

Upon the successful culmination of the training phase, the optimized model, saved as `model.pt`, was seamlessly integrated for real-time inference. A standard webcam was utilized as the primary video input source. Each frame from the live video stream was processed sequentially.

For every incoming frame, the model executed object detection based on the following critical parameters:

* **Inference Image Resolution:** Consistent with the training phase, input frames for inference were also resized to **960x960 pixels** to maintain optimal performance.
* **Confidence Threshold:** A stringent confidence threshold of **0.5 (50%)** was enforced. Only detected objects with a prediction confidence score equal to or exceeding this threshold were considered valid and subsequently displayed.
* **Visual Output:** Identified gestures were visually demarcated by dynamically generated bounding boxes drawn around the detected objects. Each bounding box was explicitly labeled with the corresponding predicted class name, providing immediate and intuitive visual feedback to the user.

---

## 4. Results

The training regimen yielded highly encouraging results, unequivocally demonstrating the model's exceptional capability in accurately detecting and classifying the defined set of gestures. A comprehensive summary of the key performance metrics, derived from the validation set, is provided below:

### 4.1. Overall Performance Metrics

* **Precision:** $\text{0.882}$ (88.2%)
* **Recall:** $\text{0.878}$ (87.8%)
* **mAP50 (mean Average Precision at Intersection over Union (IoU) threshold of 0.5):** $\text{0.876}$ (87.6%)
* **mAP50-95 (mean Average Precision averaged across IoU thresholds from 0.5 to 0.95):** $\text{0.796}$ (79.6%)

### 4.2. Class-Specific Performance Breakdown

The following table presents a detailed breakdown of the performance metrics for each individual gesture class identified by the model.

| Class           | Images | Instances | Precision (P) | Recall (R) | mAP50 | mAP50-95 |
| :-------------- | :----- | :-------- | :------------ | :--------- | :---- | :------- |
| **all** | **1200** | **2193** | **0.882** | **0.878** | **0.876** | **0.796** |
| Punch\_VFR      | 58     | 58        | 0.946         | 0.914      | 0.911 | 0.82     |
| Punch\_VFL      | 58     | 58        | 0.962         | 0.914      | 0.922 | 0.844    |
| One\_VFR        | 88     | 88        | 0.849         | 0.841      | 0.834 | 0.751    |
| One\_VFL        | 88     | 88        | 0.848         | 0.841      | 0.838 | 0.747    |
| Two\_VFR        | 87     | 87        | 0.797         | 0.908      | 0.871 | 0.793    |
| Two\_VFL        | 87     | 87        | 0.798         | 0.908      | 0.862 | 0.787    |
| Three\_VFR      | 70     | 70        | 0.874         | 0.9        | 0.886 | 0.824    |
| Three\_VFL      | 70     | 70        | 0.875         | 0.9        | 0.887 | 0.823    |
| Four\_VFR       | 80     | 80        | 0.938         | 0.812      | 0.824 | 0.762    |
| Four\_VFL       | 80     | 80        | 0.937         | 0.812      | 0.853 | 0.762    |
| Five\_VFR       | 70     | 70        | 0.864         | 0.929      | 0.894 | 0.827    |
| Five\_VFL       | 70     | 70        | 0.863         | 0.929      | 0.869 | 0.824    |
| Six\_VFR        | 83     | 83        | 0.854         | 0.867      | 0.855 | 0.784    |
| Six\_VFL        | 83     | 83        | 0.853         | 0.867      | 0.851 | 0.772    |
| Seven\_VFR      | 83     | 83        | 0.862         | 0.88       | 0.87  | 0.788    |
| Seven\_VFL      | 83     | 83        | 0.858         | 0.88       | 0.857 | 0.778    |
| Eight\_VFR      | 69     | 69        | 0.88          | 0.884      | 0.885 | 0.801    |
| Eight\_VFL      | 69     | 69        | 0.881         | 0.884      | 0.875 | 0.805    |
| Nine\_VFR       | 78     | 78        | 0.861         | 0.821      | 0.805 | 0.746    |
| Nine\_VFL       | 78     | 78        | 0.86          | 0.821      | 0.813 | 0.744    |
| Span\_VFR       | 75     | 75        | 0.873         | 0.853      | 0.876 | 0.78     |
| Span\_VFL       | 75     | 75        | 0.872         | 0.853      | 0.861 | 0.785    |
| Horiz\_HBL      | 74     | 74        | 0.934         | 0.838      | 0.881 | 0.782    |
| Horiz\_HFL      | 78     | 78        | 0.929         | 0.897      | 0.919 | 0.811    |
| Horiz\_HBR      | 78     | 78        | 0.928         | 0.897      | 0.919 | 0.833    |
| Horiz\_HFR      | 74     | 74        | 0.934         | 0.838      | 0.89  | 0.791    |
| Collab          | 68     | 68        | 0.849         | 0.941      | 0.925 | 0.82     |
| XSign           | 69     | 69        | 0.893         | 0.913      | 0.914 | 0.851    |
| TimeOut         | 70     | 70        | 0.895         | 0.914      | 0.948 | 0.842    |

### 4.3. Inference Speed Analysis

The real-time inference capability is further corroborated by the system's highly efficient processing speed:

* **Preprocessing:** Approximately $\text{0.3ms}$ per image.
* **Inference:** Approximately $\text{3.2ms}$ per image.
* **Postprocessing:** Approximately $\text{2.6ms}$ per image.

This aggregate low latency is a critical factor in ensuring the seamless and responsive operation of the real-time gesture recognition system.

---

## 5. Conclusion and Future Work

This project has successfully demonstrated the development and deployment of a highly effective **real-time gesture recognition system** powered by the **YOLOv11n model**. The compelling performance metrics, particularly the high precision, recall, and mAP values across diverse gesture classes, coupled with the remarkably efficient inference speed, emphatically underscore the system's considerable effectiveness and its substantial potential for deployment in a myriad of practical applications.

### 5.1. Potential Applications

* **Intuitive Human-Computer Interfaces:** Facilitating touchless interaction with various digital systems and devices.
* **Enhanced Gaming Experiences:** Enabling more immersive and natural control schemes in interactive entertainment.
* **Assisted Living Technologies:** Providing intuitive and accessible control mechanisms for individuals with mobility impairments.
* **Security and Surveillance Systems:** Augmenting situational awareness through the detection and interpretation of specific human actions or signals.

### 5.2. Future Directions

Future research endeavors and developmental iterations could strategically focus on several key areas:

* **Dataset Expansion and Augmentation:** Increasing the diversity and volume of the gesture dataset to enhance model generalization.
* **Advanced Architecture Exploration:** Investigating the efficacy of more recent or specialized YOLO architectures, or other cutting-edge object detection models, to potentially achieve even higher accuracy or efficiency.
* **Edge Device Optimization:** Tailoring and optimizing the current system for deployment on resource-constrained edge computing devices, thereby expanding its applicability in mobile and embedded environments.
