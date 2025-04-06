import streamlit as st
import cv2
import numpy as np
import joblib
import os

# Load the trained model
model = joblib.load("svm_rice_leaf.pkl")
categories = ["Bacterial leaf blight", "Brown spot", "Leaf smut"]

# Image preprocessing function
def preprocess_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))
    img = img.flatten()
    img = img / 255.0
    return img.reshape(1, -1)

# Streamlit UI
st.set_page_config(page_title="Rice Leaf Disease Detection", layout="centered")
st.title("🌾 Rice Leaf Disease Detection")

uploaded_file = st.file_uploader("Upload a Rice Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR", caption="Uploaded Image", use_column_width=True)

    processed_img = preprocess_image(image)
    prediction = model.predict(processed_img)[0]
    result = categories[prediction]

    st.success(f"✅ Prediction: {result}")
