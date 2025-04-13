import streamlit as st
from keras.models import load_model
from PIL import Image
from util import classify  # Assuming 'classify' is from the first snippet or a similar one

# Set title
st.title('Alzheimer Classification')

# Set header
st.header('Please upload an MRI image')

# Upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# Load classifier
model = load_model('./model/keras_model_alzheimer.h5')

# Load class names
with open('./model/labels_alzheimer.txt', 'r') as f:
    class_names = [a.strip().split(' ', 1)[1] for a in f.readlines() if len(a.strip().split(' ', 1)) > 1]

# Display image and make prediction
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # Classify the image
    class_name, conf_score = classify(image, model, class_names)

    # Display classification result
    st.write("## Predicted Class: **{}**".format(class_name))
    st.write("### Confidence Score: **{:.2f}%**".format(conf_score * 100))
