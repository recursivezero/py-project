import streamlit as st
import os
from datetime import datetime
from PIL import Image, UnidentifiedImageError
import base64
from io import BytesIO

from constants import *
from messages import *
import audio_recorder
import speech_to_text


# Header
image_logo = Image.open('./voice-resume.png')

# st.markdown(
#     HEADER_HTML (image_logo),
#     unsafe_allow_html=True
# )

st.markdown(HEADER_HTML, unsafe_allow_html=True)

# Sidebar buttons
st.sidebar.header("Voice Resume")

if "page" not in st.session_state:
    st.session_state.page = "resume_uploader"

if st.sidebar.button("Resume Uploader"):
    st.session_state.page = "resume_uploader"

if st.sidebar.button("Audio Recorder"):
    st.session_state.page = "audio_recorder"

if st.sidebar.button("Speech to Text"):
    st.session_state.page = "speech_to_text"


# Footer

# st.markdown(FOOTER, unsafe_allow_html=True)

# Conditional rendering based on session state
if st.session_state.page == "resume_uploader":
    st.title(TITLE)
    st.write(DESCRIPTION)
    # Image Generation Page
    st.subheader("Upload resume")
    single_image = st.file_uploader(SINGLE_IMAGE_LABEL, type=ALLOWED_EXTENSIONS)
    if single_image is not None:
        try:
            first_image = Image.open(single_image)
        except UnidentifiedImageError:
            st.error(SINGLE_IMAGE_INVALID)

    show_progress_message = st.empty()

    if st.button("Upload"):
        with show_progress_message.container():
            st.subheader(IMAGE_GENERATION_IN_PROGRESS)

elif st.session_state.page == "audio_recorder":
    # Audio Recorder Page
    audio_recorder.main()  # Call the main function from audio_recorder.py

elif st.session_state.page == "speech_to_text":
    # Speech to Text Page
    speech_to_text.main()  # Call the main function from speech_to_text.py
