import os
from gtts import gTTS
import streamlit as st

# Title of the app
st.title("International Text-to-Speech App")

# Text input
text = st.text_area("Enter text here", "یہ ایک ٹیسٹ ہے")  # Default Urdu text

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

# Function to chunk text into manageable sizes
def chunk_text(text, max_length=300):
    words = text.split()
    current_chunk = []
    chunks = []

    for word in words:
        # If adding the next word exceeds the max_length, start a new chunk
        if sum(len(w) for w in current_chunk) + len(word) + len(current_chunk) > max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
        else:
            current_chunk.append(word)
    
    # Add any remaining words as a final chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

# Generate Speech Button
if st.button("Generate Speech"):
    if not text.strip():
        st.error("Please enter valid text.")
    else:
        try:
            # Chunk the text
            text_chunks = chunk_text(text)
            audio_files = []

            # Process each chunk
            for i, chunk in enumerate(text_chunks):
                # Create TTS for each chunk
                tts = gTTS(text=chunk, lang=language_options[language])
                
                # Save to a temporary file
                temp_file = f"output_{i}.mp3"
                tts.save(temp_file)
                audio_files.append(temp_file)

            # Play all audio files sequentially
            for audio_file in audio_files:
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format='audio/mp3')

            # Clean up temporary files
            for audio_file in audio_files:
                os.remove(audio_file)

        except Exception as e:
            st.error(f"Error during speech generation: {e}")
