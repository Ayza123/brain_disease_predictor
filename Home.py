import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Neurolens", page_icon="", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; color: #2c3e50; }
    .st-bx { 
        border: 3px solid #3498db;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        background-color: transparent;
        min-height: 130px;
        font-size: 18px;
        font-weight: bold;
    }
    .feature-title { color: #f1c40f; font-size: 20px; font-weight: bold; }
    .feature-text { color: #Ff007f; font-size: 16px; font-weight: normal; }
    .disease-title { font-size: 22px; font-weight: bold; color: #f1c40f; }
    .disease-text { font-size: 18px; color: #Ff007f; }
    .fixed-image { 
        height: 250px !important;  
        width: 100%;  
        object-fit: cover;  
        margin-bottom: 10px; /* Adds spacing below image */
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Introduction
st.title("wellcome To Neurolens")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### Cutting-edge AI technology for early disease detection.")
    st.markdown(
        "Our AI-based medical tool assists in detecting critical neurological diseases. "
        "Upload your medical images and get AI-powered insights for **Brain Tumors, Stroke, Alzheimer's, Multiple Sclerosis (MS), and Parkinson’s Disease**."
    )

with col2:
    st.image("images/start.jpg", caption="", use_column_width=True)

st.write("---")

# Disease Overview
st.write("## Disease Overview")

# Disease List with Fixed Image Sizes
diseases = [
    {"name": "Multiple Sclerosis (MS)", "image": "images/brain1.jpg", "description": "Multiple sclerosis (MS) is a chronic autoimmune disease that "
    "affects the central nervous system, causing inflammation and damage to the protective myelin sheath around nerve fibers. This leads to symptoms"
    " like muscle weakness, vision problems, and coordination issues. While there is no cure, treatments can help manage symptoms and slow disease progression."},


    {"name": "Stroke", "image": "images/brain2.jpg", "description": "A stroke occurs when blood flow to the brain is blocked or reduced, causing brain cells to"
    " die due to a lack of oxygen. It can lead to paralysis, speech difficulties, and cognitive impairments. Immediate medical attention is crucial to minimize"
    " damage and improve recovery outcomes."},


    {"name": "Brain Tumor", "image": "images/brain3.jpg", "description": "A brain tumor is an abnormal growth of cells in the brain that can be benign "
    "(non-cancerous) or malignant (cancerous). It can cause symptoms like headaches, seizures, vision problems, and cognitive changes. Treatment options include"
    " surgery, radiation, and chemotherapy, depending on the type and location of the tumor."},


    {"name": "Parkinson’s Disease", "image": "images/brain4.jpg", "description": "Parkinson’s disease is a progressive neurodegenerative disorder that affects"
    " movement due to the loss of dopamine-producing neurons in the brain. Symptoms include tremors, muscle stiffness, slow movement, and balance difficulties."
    " While there is no cure, medications and therapies can help manage symptoms and improve quality of life."},


    {"name": "Alzheimer’s Disease", "image": "images/brain5.png", "description": "Alzheimer’s disease is a progressive neurodegenerative disorder that primarily affects "
    "memory, thinking, and behavior. It is the most common cause of dementia, leading to cognitive decline and difficulty performing daily tasks. While there is no"
    " cure, treatments can help slow progression and manage symptoms."}
]

# Initialize session state for tracking disease index
if "disease_index" not in st.session_state:
    st.session_state.disease_index = 0

# Display the current disease
disease = diseases[st.session_state.disease_index]
col1, col2 = st.columns([1, 2])

with col1:
    st.image(disease["image"], use_column_width=True, output_format="auto", caption="")  # Image now at the top

with col2:
    st.markdown(f'<div class="disease-title">{disease["name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="disease-text">{disease["description"]}</div>', unsafe_allow_html=True)

# Add a "Next Disease" button to cycle through diseases
if st.button("Next Disease ➡️"):
    st.session_state.disease_index = (st.session_state.disease_index + 1) % len(diseases)

st.write("---")

# Features Section (Now Visible)
st.write("## Features")

col1, col3 = st.columns(2)
with col1:
    st.markdown('<div class="st-bx"><span class="feature-title"> 🏥 Advanced AI Diagnosis</span><br><span class="feature-text">Detects diseases with high accuracy.</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="st-bx"><span class="feature-title"> 📊 Image Processing</span><br><span class="feature-text">Upload MRI, CT scans for analysis.</span></div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    st.markdown('<div class="st-bx"><span class="feature-title"> 🧬 Multiple Disease Detection</span><br><span class="feature-text">Brain Tumor, Stroke, Alzheimer\'s, etc.</span></div>', unsafe_allow_html=True)
with col5:
    st.markdown('<div class="st-bx"><span class="feature-title"> ☁️ Cloud-Based System</span><br><span class="feature-text">Access reports from anywhere.</span></div>', unsafe_allow_html=True)

st.write("---")


st.write(" Select diseases predictor from menu for real time prediction")