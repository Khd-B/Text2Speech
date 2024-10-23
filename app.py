# Step 1: Install gTTS
!pip install gTTS

# Step 2: Import necessary libraries
from gtts import gTTS
from IPython.display import Audio

# Step 3: Define the text and create TTS
text = "Hello! This is a text-to-speech test using Google Text-to-Speech."
tts = gTTS(text=text, lang='en')

# Step 4: Save the audio file
tts.save("output.mp3")

# Step 5: Play the audio
Audio("output.mp3")
