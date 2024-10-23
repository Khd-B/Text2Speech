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

# Generate Speech Button
if st.button("Generate Speech"):
    # Check if text input matches selected language
    if (language == "Urdu" and not text.strip()) or (language != "Urdu" and text.strip().isspace()):
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
            st.error("Please select the correct output language.")

# Clear Button
if st.button("Clear"):
    # Clear the session state to reset inputs
    st.session_state.clear()  # Clears all session state

# Initialize state for text and language if not already set
if 'text' not in st.session_state:
    st.session_state.text = "یہ ایک ٹیسٹ ہے"
if 'language' not in st.session_state:
    st.session_state.language = list(language_options.keys())[0]  # Default to first option

# Update text area and selectbox with session state
text = st.text_area("Enter text here", st.session_state.text)
language = st.selectbox("Select Language", list(language_options.keys()), index=list(language_options.keys()).index(st.session_state.language))

# Update session state based on user input
st.session_state.text = text
st.session_state.language = language
