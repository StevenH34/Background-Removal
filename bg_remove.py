import streamlit as st
from io import BytesIO
from PIL import Image
from rembg import remove

# BytesIO & PIL help with file types & memory management
# rembg.remove to remove the image background

# Page layout using streamlit
st.set_page_config(layout="wide", page_title="Image Background Remover")
st.write("## Remove background from your image")
st.write(
    "Upload an image and remove its the background." 
)
st.write("This code is open source and available [here](<https://github.com/tyler-simons/BackgroundRemoval>) on GitHub. Special thanks to the [rembg library](<https://github.com/danielgatis/rembg>)")
st.sidebar.write("## Upload and download :gear:")

# Adding layout columns
col1, col2 = st.columns(2)

# Upload the image
# imageUpload = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

# Convert the image to BytesIO
def convertImage(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byteImg = buf.getvalue()
    return byteImg

def fixImage(upload):
    image = Image.open(upload)
    col1.write("Original Image:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image: ")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button(
        "Download fixed image", convertImage(fixed), "new-image.png", "image/png"
    )

# Upload folder
myUpload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if myUpload is not None:
    fixImage(upload = myUpload)
else:
    fixImage("./Red-necked-wallaby.jpg")