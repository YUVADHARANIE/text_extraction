import os
import sys
import streamlit as st

# Check if Tesseract is installed
def install_tesseract():
    if os.system("tesseract --version") != 0:
        st.warning("Tesseract is not installed. Installing now...")
        if sys.platform.startswith('linux'):
            os.system("sudo apt-get update && sudo apt-get install -y tesseract-ocr")
        elif sys.platform == 'darwin':  # macOS
            os.system("brew install tesseract")
        else:
            st.error("Tesseract installation is only automated for Linux and macOS.")
            return False
    return True

# Install Tesseract if not available
if not install_tesseract():
    st.stop()

# Import other necessary libraries
from PIL import Image
import pytesseract

st.title("Text Extraction from Image")

st.write("Upload an image to extract text")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Convert image to text
    st.write("Extracting text from the image...")
    extracted_text = pytesseract.image_to_string(image)
    
    # Display extracted text
    st.write("Extracted Text:")
    st.write(extracted_text)
