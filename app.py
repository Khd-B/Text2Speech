# app.py

import os
from gtts import gTTS
import streamlit as st

# Title of the app
st.title("Text-to-Speech App")

# Text input
text = st.text_area("Enter text here", "Hello! This is a text-to-speech test using Google Text-to-Speech.")

if st.button("Generate Speech"):
    # Create TTS
    tts = gTTS(text=text, lang='en')
    
    # Save to a temporary file
    temp_file = "output.mp3"
    tts.save(temp_file)
    
    # Play audio
    audio_file = open(temp_file, "rb")
    st.audio(audio_file.read(), format='audio/mp3')
    audio_file.close()
    
    # Clean up temporary file
    os.remove(temp_file)
