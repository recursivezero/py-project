import streamlit as st
from streamlit_mic_recorder import speech_to_text

state = st.session_state

if 'text_received' not in state:
    state.text_received = []

def main():
    st.title(":green[Speech to Text Converter]")
    st.write("Convert recorded audio to text (Supports English and Hindi)")

    c1, c2 = st.columns(2)
    with c1:
        st.write("Convert speech to text:")
    with c2:
        text = speech_to_text(language='hi', use_container_width=True, just_once=True, key='STT')

    if text:
        state.text_received.append(text)

    for text in state.text_received:
        st.text(text)

if __name__ == "__main__":
    main()
