# Real-Time Gun Detection System 🎯

An automated computer vision application built with Python and OpenCV that detects firearms in real-time using a live webcam feed. 

This project utilizes Haar Cascade classifiers to identify specific object features (guns) frame-by-frame, providing low-latency security monitoring.

## 🚀 Features
* **Real-Time Processing:** Captures and analyzes live video feeds using your built-in webcam.
* **Haar Cascade Integration:** Uses a pre-trained XML model to accurately draw bounding boxes around detected firearms.
* **Optimized Performance:** Implements `imutils` for frame resizing to reduce computational overhead, ensuring smooth video playback and rapid detection.

## 🛠️ Technologies Used
* **Python 3.x**
* **OpenCV (`cv2`)** - For image processing and video capture.
* **Imutils** - For efficient frame resizing.
* **NumPy** - For array operations and data structuring.

## 📂 Project Structure
* `Gun Detector.py`: The main Python script that initializes the camera, processes the video stream, and outputs the detection results.
* `cascade.xml`: The pre-trained Haar Cascade model used to identify the geometric features of firearms.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Tech-Talib/Gun-Detector.git](https://github.com/Tech-Talib/Gun-Detector.git)
   cd Gun-Detector
