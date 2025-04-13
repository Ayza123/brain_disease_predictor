import numpy as np
import streamlit as st
from PIL import ImageOps, Image

def set_background(image_file):
    # Dummy implementation to set background
    pass

def classify(image, model, class_names):
    # Convert image to (224, 224)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # Convert image to numpy array
    image_array = np.asarray(image)

    # Normalize image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Set model input
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Make prediction
    prediction = model.predict(data)

    # Use np.argmax to find the index of the class with the highest confidence
    index = np.argmax(prediction)  # Get index of the class with highest confidence score
    
    # Get the predicted class name and confidence score
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score
