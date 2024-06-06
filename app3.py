import streamlit as st
from PIL import Image
import subprocess
import os

# Set page config to wide mode
st.set_page_config(layout="wide")

# Custom CSS for button styling and centering text
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .centered-text {
        text-align: center;
        font-size: 1.25rem;
        margin-bottom: 2rem;
    }
    .center-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: black; /* Black background */
        color: white; /* White font color */
        padding: 10px 20px; /* Adjust padding to increase button size */
        font-size: 1.25rem; /* Adjust font size */
    }
    </style>
    """, unsafe_allow_html=True)

# Centered Title
st.markdown('<h1 class="centered-title">Before and After Image Comparison</h1>', unsafe_allow_html=True)

# Centered Instructions
st.markdown('<p class="centered-text">Please upload two images: one for "Before" and one for "After".</p>', unsafe_allow_html=True)

# Create four columns with the specified proportions
col1, col2, col3, col4 = st.columns([0.2, 0.4, 0.4, 0.2])

# Upload the first image (Before) in the second column
with col2:
    uploaded_file1 = st.file_uploader('Choose the "Before" image', type=['png', 'jpg', 'jpeg'], key='1')
    if uploaded_file1 is not None:
        image1 = Image.open(uploaded_file1)
        st.image(image1, caption='Before Image', use_column_width=True)

# Upload the second image (After) in the third column
with col3:
    uploaded_file2 = st.file_uploader('Choose the "After" image', type=['png', 'jpg', 'jpeg'], key='2')
    if uploaded_file2 is not None:
        image2 = Image.open(uploaded_file2)
        st.image(image2, caption='After Image', use_column_width=True)

# Add a spacer using columns and center the button
spacer1, center_column, spacer2 = st.columns([0.4, 0.2, 0.4])
with center_column:
    if st.button('Submit'):
        st.write('Running UNet model...')
        # Save uploaded images to a temporary directory
        temp_dir = 'temp_images'
        os.makedirs(temp_dir, exist_ok=True)
        image1_path = os.path.join(temp_dir, 'before.png')
        image2_path = os.path.join(temp_dir, 'after.png')
        image1.save(image1_path)
        image2.save(image2_path)

        # Change directory to the one containing the after image
        os.chdir(os.path.dirname(uploaded_file2.name))

        # Execute the UNet model prediction script with the uploaded images
        subprocess.run(['python3', 'predict.py', '--input', 'DEMO', '--output', 'temp_images'])
        st.write('Model execution complete. Check the output directory for results.')

        # Load and display the predicted image
        predicted_image_path = os.path.join(temp_dir, 'predicted.png')
        if os.path.exists(predicted_image_path):
            predicted_image = Image.open(predicted_image_path)
            st.image(predicted_image, caption='Predicted Image', use_column_width=True)
        else:
            st.write('Predicted image not found. Please check the output directory.')
