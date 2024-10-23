import os
from gtts import gTTS
import streamlit as st

# Title of the app
st.title("International Text-to-Speech App")

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

# Function to check if the text is in the selected language
def is_valid_language(text, language):
    text = text.strip()

    if language == "Urdu":
        return any('\u0600' <= char <= '\u06FF' for char in text)  # Check for Urdu characters
    elif language == "Arabic":
        return any('\u0600' <= char <= '\u06FF' for char in text)  # Check for Arabic characters
    elif language == "Chinese (Mandarin)":
        return any('\u4E00' <= char <= '\u9FFF' for char in text)  # Check for Chinese characters
    elif language == "Russian":
        return any('\u0400' <= char <= '\u04FF' for char in text)  # Check for Cyrillic characters
    elif language == "British English":
        return all(char.isascii() for char in text) and any(text)  # Check for ASCII for English
    elif language == "Spanish":
        return all(char.isascii() for char in text) and any(text)  # Check for ASCII for Spanish
    elif language == "French":
        return all(char.isascii() for char in text) and any(text)  # Check for ASCII for French

    return False

# Check if button should be enabled
button_enabled = is_valid_language(text, language)

# Generate Speech Button
if st.button("Generate Speech", disabled=not button_enabled):
    # Check if text input is valid
    if not text.strip():
        st.error("Please enter valid text.")
    else:
        try:
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
        except Exception as e:
            st.error(f"Error during speech generation: {e}")

# Provide feedback about button state
if not button_enabled:
    st.warning("The 'Generate Speech' button will be enabled when the input text matches the selected language.")
