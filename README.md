# 🚀YOLOv8-Streamlit-RealTime-Object-Detection

## 📌 Project Overview

This project is a real-time object detection web application built using YOLOv8 and Streamlit.

## The system allows users to:

Upload images

Upload videos

Use live webcam feed

It performs deep learning-based object detection and displays annotated results directly in the browser.

This demonstrates deployment of a computer vision model into an interactive web application.

---

## 🧠 Tech Stack

Python

YOLOv8 (Ultralytics)

OpenCV

Streamlit

NumPy

---

## 🔥 Key Features

- Image Object Detection
- Video Object Detection
- Real-Time Webcam Detection
- Adjustable Confidence Threshold
- Interactive Web UI
- Fast and Lightweight Inference

---

## 🏗️ System Architecture

User Input (Image / Video / Webcam)
→ Frame Processing (OpenCV)
→ YOLOv8 Inference
→ Bounding Box & Label Rendering
→ Streamlit Web Display

--- 

## ⚙️ Installation

### 2️⃣ Install Dependencies
pip install -r requirements.txt

Or manually:

pip install ultralytics opencv-python streamlit numpy
### ▶️ How to Run the App
streamlit run app.py

The application will open in your browser at:

http://localhost:8501

---

## 🎛️ How to Use

### Select detection source:

Image Upload

Video Upload

Webcam

Adjust confidence threshold from sidebar

View real-time annotated results

---

## 📊 How It Works

The YOLOv8 model is loaded once using Streamlit caching.

Frames are processed individually.

Model predicts:

Bounding boxes

Class labels

Confidence scores

Results are rendered dynamically in the web interface.

---

## 🎯 Real-World Applications

Smart surveillance systems

Retail analytics

Traffic monitoring

Industrial automation

AI-powered web applications

---

## 💼 Why This Project Matters

This project demonstrates:

✔ End-to-end AI application development
✔ Deep learning model integration
✔ Real-time computer vision pipeline
✔ Web deployment skills
✔ User interface integration with AI

---

# 👩‍💻 Author

## Akshitha Hirakari
## Aspiring AI & Computer Vision Engineer
