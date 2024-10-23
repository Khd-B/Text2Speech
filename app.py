import os
from gtts import gTTS
import streamlit as st

# Title of the app
st.title("International Text-to-Speech App")

# Create a placeholder for the text area
text_placeholder = st.empty()
text = text_placeholder.text_area("Enter text here", "یہ ایک ٹیسٹ ہے")  # Default Urdu text

# Language selection
language_options = {
    "English": "en",
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
            with open(temp_file, "rb") as audio_file:
                st.audio(audio_file.read(), format='audio/mp3')
            
            # Clean up temporary file
            os.remove(temp_file)

        except Exception as e:
            st.error(f"Error during speech generation: {e}")

# Clear Button
if st.button("Clear"):
    text_placeholder.text_area("Enter text here", "")  # Reset the text area to empty
