import streamlit as st
from PIL import Image

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
        padding: 15px 25px; /* Adjust padding to increase button size */
        font-size: 2.5rem; /* Adjust font size */
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
spacer1, center_column, spacer2 = st.columns([0.45, 0.1, 0.45])
with center_column:
    if st.button('SUBMIT'):
        st.write('Button clicked!')
