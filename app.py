import streamlit as st
import requests
from PIL import Image
import io

# Your API key
api_key = 'K85949597588957'

# OCR API URL
ocr_url = 'https://api.ocr.space/parse/image'

# Function to call the OCR API
def extract_text_from_image(image):
    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    # Make the POST request to the OCR API
    response = requests.post(
        ocr_url,
        files={'image': img_bytes},
        data={'apikey': api_key}
    )

    # Parse the response
    result = response.json()

    # Return the parsed text
    return result.get("ParsedResults")[0].get("ParsedText")

# Streamlit app
st.title("Text Extraction from Image")

st.write("Upload an image to extract text")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text
    st.write("Extracting text from the image...")
    extracted_text = extract_text_from_image(image)
    
    # Display extracted text
    st.write("Extracted Text:")
    st.write(extracted_text)
