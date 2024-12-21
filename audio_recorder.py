import streamlit as st
import os
from datetime import datetime
from st_audiorec import st_audiorec

def main():
    st.title(":green[Audio Recorder]")
    st.write("Please record the details of the product within one limit (Maximum 60 seconds can be recorded)")

    # Function to record audio
    wav_audio_data = st_audiorec()

    # Function to save audio file with timestamp
    def save_audio_file(audio_data, user_id, filename=None):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        if filename:
            file_name = f'{filename}.wav'
        else:
            file_name = f'recording_{timestamp}.wav'
        file_path = os.path.join('assets', 'audio', user_id, file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(audio_data)
        return file_path

    if wav_audio_data is not None:
        user_id = 'user1'

        # Option to save audio file with custom name
        if st.button("Save Audio File"):
            filename = st.text_input("Enter the name for the audio file (without extension):")
            if filename:  # Ensure filename is not empty
                saved_file_path = save_audio_file(wav_audio_data, user_id, filename)
                st.write(f"Audio file saved as: {saved_file_path}")
            else:
                st.warning("Please enter a filename.")

if __name__ == "__main__":
    main()
