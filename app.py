# Install the required libraries
!pip install pytesseract Pillow streamlit

import streamlit as st
import pytesseract
from PIL import Image
import io

# Function to extract text from image
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Streamlit app
def main():
    st.title("Text Extraction from Image")

    st.write("Upload an image to extract text:")

    # Upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Open the image file
        image = Image.open(uploaded_file)
        
        # Extract text from the image
        text = extract_text(image)
        
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Extracted Text:")
        st.write(text)

if __name__ == "__main__":
    main()
