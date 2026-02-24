import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

st.set_page_config(page_title="YOLO Object Detection", layout="wide")

st.title("🔥 Real-Time Object Detection using YOLOv8")

# Load model once
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# Sidebar settings
confidence = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.45)

source = st.sidebar.selectbox("Select Source", ["Image Upload", "Video Upload", "Webcam"])

# ================= IMAGE =================
if source == "Image Upload":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        results = model(img, conf=confidence)
        annotated_frame = results[0].plot()

        st.image(annotated_frame, channels="BGR")

# ================= VIDEO =================
elif source == "Video Upload":
    uploaded_video = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

    if uploaded_video is not None:
        tfile = open("temp.mp4", "wb")
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture("temp.mp4")
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, conf=confidence)
            annotated_frame = results[0].plot()

            stframe.image(annotated_frame, channels="BGR")

        cap.release()

# ================= WEBCAM =================
elif source == "Webcam":
    run = st.checkbox("Start Camera")
    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=confidence)
        annotated_frame = results[0].plot()
        FRAME_WINDOW.image(annotated_frame, channels="BGR")

    cap.release()