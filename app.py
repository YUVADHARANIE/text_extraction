import streamlit as st
import requests

# Function to extract text using OCR.Space API
def extract_text_from_image(image):
    ocr_space_url = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': 'K85949597588957',  # Get your API key from OCR.Space
    }
    files = {
        'file': image,
    }
    response = requests.post(ocr_space_url, files=files, data=payload)
    result = response.json()
    text = result.get('ParsedResults', [{}])[0].get('ParsedText', '')
    return text

# Streamlit app
def main():
    st.title("Text Extraction from Image")

    st.write("Upload an image to extract text:")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        text = extract_text_from_image(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write("Extracted Text:")
        st.write(text)

if __name__ == "__main__":
    main()
