import streamlit as st
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
