import json
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st

# Set the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))  # Recommended for Streamlit
model_path = f"{working_dir}/trained model/Plant_Disease_Detection.h5"

# Load model and class names
model = load_model(model_path)
class_names = json.load(open(f"{working_dir}/class_names.json", 'r'))

# Function to preprocess image
def process_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img = np.array(img) / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)
    return img

# Function to make predictions
def model_prediction(model, image_path, class_names):
    img = process_image(image_path)
    prediction = model.predict(img)
    predicted_class = int(np.argmax(prediction, axis=1)[0])  
    print(f"Predicted class index: {predicted_class}")  
    predicted_class_name = class_names[str(predicted_class)]
    return predicted_class_name

# Streamlit App
st.title('🌿 Plant Disease Predictor')

uploaded_img = st.file_uploader("Upload Image File", type=["jpeg", "png", "jpg"])

if uploaded_img is not None:
    image = Image.open(uploaded_img)
    col1, col2 = st.columns(2)

    with col1:
        resized_image = image.resize((150, 150))
        st.image(resized_image)

    with col2:
        if st.button('Predict'):
            prediction = model_prediction(model, uploaded_img, class_names)
            st.success(f'Prediction: {str(prediction)}')
