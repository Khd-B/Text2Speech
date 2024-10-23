import os
from gtts import gTTS
import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #eaf4fc;  /* Soft light blue background */
            color: #2c3e50;  /* Dark text color */
            font-family: Arial, sans-serif;
        }
        .title {
            text-align: center;
            color: #2980b9;
            font-size: 36px;
            margin-bottom: 20px;
        }
        .stButton {
            background-color: #2980b9;  /* Dark blue button */
            color: white;  /* White text */
            font-weight: bold;  /* Bold text */
            padding: 10px 20px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .stButton:hover {
            background-color: #3498db;  /* Lighter blue on hover */
        }
        .watermark {
            position: absolute;
            top: 10%;
            left: 10%;
            opacity: 0.1;
            z-index: -1;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<h1 class="title">International Text-to-Speech App</h1>', unsafe_allow_html=True)

# Optional: Add a watermark (language symbols or any background image)
# You can replace 'watermark.png' with the path to your own image file
st.markdown('<img class="watermark" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_the_United_Nations.svg/1200px-Flag_of_the_United_Nations.svg.png" width="200" />', unsafe_allow_html=True)

# Create a placeholder for the text area
text_placeholder = st.empty()
text = text_placeholder.text_area("Enter text here", "یہ ایک ٹیسٹ ہے", height=150)  # Default Urdu text

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
