import streamlit as st
from keras.models import load_model
from PIL import Image
from util import classify

# set title
st.title('Stroke classification')

# set header
st.header('Please upload a MRI image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./model/stroke_model.h5')

# load class names
with open('./model/stroke_labels.txt', 'r') as f:
    class_names = [a.strip().split(' ', 1)[1] for a in f.readlines() if len(a.strip().split(' ', 1)) > 1]

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    #classify image
    class_names,conf_score = classify(image,model,class_names)

# write classification
    st.write("## Predicted Class: **{}**".format(class_name))
    st.write("### Confidence Score: **{:.2f}%**".format(conf_score * 100))
