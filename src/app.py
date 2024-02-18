import streamlit as st
from glitch_this import ImageGlitcher
from PIL import Image, ImageOps

st.set_page_config(page_title="streamGlitCH", layout="wide")

glitcher = ImageGlitcher()
img_list = []
glitched_imgs = []
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
        st.write("Use the settings below to glitch your images:")

        glitch_amount = st.slider(label="Glitch Amount", min_value=0.1, max_value=10.0)
        color_offset = st.toggle(label="Color Offset", value=True)
        scan_lines = st.toggle(label="Scan Lines", value=False)
        seed = st.number_input(
            label="Insert seed here (leave empty for no seed)", value=None
        )

    else:
        st.write("Please upload your images above.")

if uploaded_images:

    col1, col2 = st.columns([1, 1])

    with col1.expander(label="Uploaded Images:", expanded=True):
        for img in uploaded_images:
            img = Image.open(img)
            img = ImageOps.exif_transpose(img)
            img_list.append(img)

        st.image(image=img_list, output_format="PNG")

    with col2.expander(label="Glitched Images:", expanded=True):
        for img in img_list:
            glitched_img = glitcher.glitch_image(
                src_img=img,
                glitch_amount=glitch_amount,
                color_offset=color_offset,
                scan_lines=scan_lines,
                seed=seed,
            )
            glitched_imgs.append(glitched_img)
        st.image(image=glitched_imgs, output_format="PNG")

else:
    st.title(body="streamGlitCH")

    st.markdown(
        """
            Welcome to streamGlitCH, the image glich generator!
                
            Just upload your files in the left sidebar, select the glitch effects and the click the "Glitch" button.
                
            The images will be shown after the effects got applied. 
        """
    )

    st.markdown("---")

    st.write("Waiting for images...")
