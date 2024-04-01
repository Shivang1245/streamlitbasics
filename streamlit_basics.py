import streamlit as st
import time
from PIL import Image

# add the title of the app
st.title('My Awsome Streamlit App')

# add header
st.header('New Header')

# add sub-header
st.subheader('New sub - header')

# add text
st.text('New text')

# adding a markdown
st.markdown('This is a markdown')

# add button
st.button('New button')

# add checkbox
st.checkbox('This is a checkbox')

# Radio Button
st.radio('Radio', ['option1', 'option2', 'option3'])

# select
st.selectbox('Select', ['option1', 'option2', 'option3'])

# Multiselect
st.multiselect('multiselect', ['option1', 'option2', 'option3'])

# file uploader
st.file_uploader('File uploader', type=['png','jpeg'])

# Colour Picker
st.color_picker('colour Picker')

# time input
st.time_input('time input')

# text input
st.text_input('text input')

# number input
st.number_input('number input', min_value=1, max_value=10, value=5)

# text area
st.text_area('text area', placeholder='Enter your text ')

# Slider
st.slider('slider', min_value=1, max_value=100, value=5)

# progress bar
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete+1)

# Spinner
with st.spinner('Waiting.. '):
    time.sleep(2)

# add Columns
col1, col2 = st.columns(2)

with col1:
    st.header('This is column 1')
    st.text('This is the text of column 1')

with col2:
    st.header('This is column 2')
    st.text('This is the text of column 2')

# add images from files and displaying it
image = st.file_uploader('File uploader', type=['png', 'jpeg'])
if image:
    st.image(image, caption='Uploaded image', use_column_width=True)
