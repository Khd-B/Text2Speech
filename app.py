import os
from gtts import gTTS
import streamlit as st

# Title of the app
st.title("Text-to-Speech App")

# Text input
text = st.text_area("Enter text here", "یہ ایک ٹیسٹ ہے")  # Default Urdu text

# Language selection
language_options = {
    "British English": "en-uk",
    "Spanish": "es",
    "French": "fr",
    "Arabic": "ar",
    "Chinese (Mandarin)": "zh",
    "Urdu": "ur",
    "Russian": "ru"
}

language = st.selectbox("Select Language", list(language_options.keys()))

if st.button("Generate Speech"):
    # Create TTS
    tts = gTTS(text=text, lang=language_options[language])
    
    # Save to a temporary file
    temp_file = "output.mp3"
    tts.save(temp_file)
    
    # Play audio
    audio_file = open(temp_file, "rb")
    st.audio(audio_file.read(), format='audio/mp3')
    audio_file.close()
    
    # Clean up temporary file
    os.remove(temp_file)
