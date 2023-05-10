import streamlit as st

st.title("Hellow World")

# Upload the image
imageUpload = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

# Download file
if imageUpload:
    st.download_button("Download image", imageUpload, "new-image.png", "new-image/png")