# app.py

from gtts import gTTS
from io import BytesIO
import streamlit as st

# Title of the app
st.title("Text-to-Speech App")

# Text input
text = st.text_area("Enter text here", "Key Atlantic current could collapse soon, 'impacting the entire world for centuries to come,' leading climate scientists warn.")

if st.button("Generate Speech"):
    # Create TTS
    tts = gTTS(text=text, lang='en')

    # Save to a BytesIO object
    audio_bytes = BytesIO()
    tts.save(audio_bytes)
    audio_bytes.seek(0)

    # Play audio
    st.audio(audio_bytes, format='audio/mp3')
