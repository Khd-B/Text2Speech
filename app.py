import os
from gtts import gTTS
import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Title of the app
st.title("International Text-to-Speech App")

# Text input
text = st.text_area("Enter text here", "This is a test")  # Default English text

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

# Generate Speech Button
if st.button("Generate Speech"):
    # Check if text input is valid
    if not text.strip():
        st.error("Please enter valid text.")
    else:
        try:
            # Translate text to the selected language
            translated_text = translator.translate(text, dest=language_options[language]).text
            
            # Create TTS
            tts = gTTS(text=translated_text, lang=language_options[language])
            
            # Save to a temporary file
            temp_file = "output.mp3"
            tts.save(temp_file)
            
            # Play audio
            audio_file = open(temp_file, "rb")
            st.audio(audio_file.read(), format='audio/mp3')
            audio_file.close()
            
            # Clean up temporary file
            os.remove(temp_file)
        except Exception as e:
            st.error("Error during translation or speech generation: {}".format(e))
