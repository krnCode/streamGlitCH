import streamlit as st
from glitch_this import ImageGlitcher
from PIL import Image, ImageOps, ImageSequence
from io import BytesIO
import base64
import random
import os

st.set_page_config(page_title="streamGlitCH", layout="wide")

glitcher_img = ImageGlitcher()
img_list = []
glitched_imgs = []
glitched_gifs = []

file_ext = [".jpg", ".jpeg", ".png", ".gif"]

logo_path = r"../res/img/"
logo = logo_path + random.choice(os.listdir(logo_path))


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

        selection = st.radio(
            label="What are you going to make?",
            options=["Images", "GIFs"],
            horizontal=True,
            help="All GIFs are in 640x360",
        )

        if selection == "Images":
            glitch_amount = st.slider(
                label="Glitch Amount",
                min_value=0.1,
                max_value=10.0,
            )
            color_offset = st.toggle(label="Color Offset", value=True)
            scan_lines = st.toggle(label="Scan Lines", value=False)
            seed = st.number_input(
                label="Insert seed here (leave empty for no seed)", value=None
            )

        else:
            glitch_amount = st.slider(
                label="Glitch Amount",
                min_value=0.1,
                max_value=10.0,
            )
            color_offset = st.toggle(label="Color Offset", value=True)
            scan_lines = st.toggle(label="Scan Lines", value=False)
            seed = st.number_input(
                label="Insert seed here (leave empty for no seed)", value=None
            )
            width = st.number_input(
                label="Width of the gif", min_value=1, value=640, help="Default: 640"
            )
            height = st.number_input(
                label="Height of the gif", min_value=1, value=360, help="Defalt: 360"
            )
            frames = st.number_input(
                label="Insert number of frames here", min_value=2, max_value=1000
            )
            duration = st.number_input(
                label="Visible frame time",
                value=200,
                min_value=0,
                help="This shows how much time the frame should be visible. This is in centiseconds: 1 centisecond = 0.01 second",
            )
            loop = st.number_input(
                label="How many times the GIF should loop?",
                min_value=0,
                help="keep 0 if you want infinite loop",
            )

    else:
        st.write("Please upload your images above.")

if uploaded_images:
    if selection == "Images":
        col1, col2 = st.columns([1, 1])

        with col1.expander(label="Uploaded Images:", expanded=True):
            for img in uploaded_images:
                img = Image.open(img)
                img = ImageOps.exif_transpose(img)
                img_list.append(img)

            st.image(image=img_list, output_format="PNG")

        with col2.expander(label="Glitched Images:", expanded=True):
            for img in img_list:
                glitched_img = glitcher_img.glitch_image(
                    src_img=img,
                    glitch_amount=glitch_amount,
                    color_offset=color_offset,
                    scan_lines=scan_lines,
                    seed=seed,
                )
                glitched_imgs.append(glitched_img)
            st.image(image=glitched_imgs, output_format="PNG")

    else:
        st.write("Under construction...")
        # col1, col2 = st.columns([1, 1])

        # with col1.expander(label="Uploaded Images:", expanded=True):
        #     for img in uploaded_images:
        #         img = Image.open(img)
        #         img = ImageOps.exif_transpose(img)
        #         img_list.append(img)

        #     st.image(image=img_list, output_format="auto")

        # with col2.expander(label="Glitched GIFs:", expanded=True):
        #     for img in img_list:
        #         glitched_gif = glitcher_img.glitch_image(
        #             src_img=img,
        #             glitch_amount=glitch_amount,
        #             seed=seed,
        #             color_offset=color_offset,
        #             scan_lines=scan_lines,
        #             gif=True,
        #             frames=frames,
        #         )

        #         resized_glitched_gif = [
        #             frame.resize((width, height)) for frame in glitched_gif
        #         ]

        #         with BytesIO() as bIO:
        #             resized_glitched_gif[0].save(
        #                 bIO,
        #                 format="GIF",
        #                 append_images=resized_glitched_gif[1:],
        #                 save_all=True,
        #                 duration=duration,
        #                 loop=loop,
        #             )
        #             glitched_gif_bytes = bIO.getvalue()

        #         # glitched_gifs.append(glitched_gif_bytes)

        #         b64 = base64.b64encode(glitched_gif_bytes).decode()

        #         # st.write(glitched_gifs)
        #         # st.image(image=glitched_imgs, channels="RGB", output_format="GIF")
        #         st.markdown(
        #             f"![Glitched GIF](data:image/gif;base64,{b64})",
        #             unsafe_allow_html=True,
        #         )

else:
    st.image(image=logo)
    st.title(body="streamGlitCH")

    st.markdown(
        """
            Welcome to streamGlitCH, the image glich generator!
                
            Just upload your files in the left sidebar, and change the settings to glitch the image.
                
            The images will be glitched as you change the settings. 
        """
    )

    st.markdown("---")

    st.write("Waiting for images...")
