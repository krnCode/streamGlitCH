import streamlit as st
from glitch_this import ImageGlitcher
from PIL import Image, ImageOps

glitcher = ImageGlitcher()
file_ext = [".jpg", ".jpeg", ".png", ".gif"]

with st.sidebar:
    uploaded_images = st.file_uploader(
        label="Upload your images here",
        type=file_ext,
        label_visibility="hidden",
        accept_multiple_files=True,
    )

    if uploaded_images:
        st.markdown("---")
        st.write("Use the settings bellow to glith your images:")

    else:
        st.write("Please upload your images above.")

if uploaded_images:
    with st.expander(label="Uploaded Images:"):
        img_list = []
        for img in uploaded_images:
            img = Image.open(img)
            img = ImageOps.exif_transpose(img)
            img_list.append(img)

        st.image(image=img_list, width=200)

else:
    st.write("Waiting for images...")
