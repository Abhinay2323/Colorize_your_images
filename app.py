import streamlit as st
import fastai
from deoldify.visualize import *

def image_colorizer(url):
    colorizer = get_image_colorizer(artistic=True)
    source_url = url
    render_factor = 35
    watermarked = True 

    if source_url is not None and source_url !='':
        print(source_url)
        image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
        print(image_path)
    else:
        print('Provide an image url and try again.')
    return image_path

st.set_page_config(layout='wide')

st.title('Image Colorizer App')

input_text = st.text_input('Enter your URL')

if input_text is not None:
    if st.button('Colorize'):

        col1, col2 = st.columns([1,1])

        with col1:
            st.info("Your image")
            st.image(input_text)
        with col2:
            result = image_colorizer(input_text)
            st.success("Your colorized Image")
            st.image("result_images/image.png")