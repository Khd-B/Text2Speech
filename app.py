import streamlit as st
from gtts import gTTS
import os

# Function to generate speech
def generate_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# Streamlit App
st.title("Text to Speech Converter")

# Language selection
lang = st.selectbox("Select Language", ["English", "Urdu", "Punjabi"])

# Language mapping
lang_mapping = {
    "English": 'en',
    "Urdu": 'ur',
    "Punjabi": 'pa'
}

# Get the selected language code
lang_code = lang_mapping.get(lang, 'en')

# Text input
text_input = st.text_area("Enter text:")

# Generate speech button
if st.button("Generate Speech"):
    if text_input:
        audio_file = generate_speech(text_input, lang_code)
        st.audio(audio_file, format='audio/mp3')
        # Optionally, delete the audio file after playing
        os.remove(audio_file)
    else:
        st.error("Please enter some text.")
