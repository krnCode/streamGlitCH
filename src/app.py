import streamlit as st
from glitch_this import ImageGlitcher
from PIL import Image, ImageOps

st.set_page_config(page_title="streamGlitCH", layout="wide")


glitcher = ImageGlitcher()
img_list = []
glitched_imgs = []
file_ext = [".jpg", ".jpeg", ".png", ".gif"]

st.title(body="streamGlitCH")

st.markdown(
    """
            Welcome to streamGlitCH, the image glich generator!
            
            Just upload your files in the left sidebar, select the glitch effects and the click the "Glitch" button.
            
            The images will be shown after the effects got applied. 
            """
)

st.markdown("---")


def image_glitch():
    for img in img_list:
        glitched_img = glitcher.glitch_image(
            src_img=img,
            glitch_amount=glitch_amount,
            color_offset=color_offset,
            scan_lines=scan_lines,
        )
        glitched_imgs.append(glitched_img)

    with st.expander(label="Glitched Images:", expanded=True):
        st.image(image=glitched_imgs, output_format="PNG")


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

        glitch_amount = st.slider(label="Glitch Amount", min_value=0.1, max_value=10.0)
        color_offset = st.toggle(label="Color Offset", value=True)
        scan_lines = st.toggle(label="Scan Lines", value=False)
        bt_img_glitch = st.button(
            label="Glitch",
            on_click=image_glitch,
        )

    else:
        st.write("Please upload your images above.")

if uploaded_images:
    with st.expander(label="Uploaded Images:", expanded=True):
        for img in uploaded_images:
            img = Image.open(img)
            img = ImageOps.exif_transpose(img)
            img_list.append(img)

        st.image(image=img_list, output_format="PNG")


else:
    st.write("Waiting for images...")
