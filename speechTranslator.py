import os
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

recognizer = sr.Recognizer()
translator = Translator()

with sr.Microphone() as source:
    print("Say something in English...")
    audio = recognizer.listen(source)

try:
    english_text = recognizer.recognize_google(audio)
    print(f"You said: {english_text}")
    
    hindi_translation = translator.translate(english_text, src='en', dest='hi')
    print(f"Translation in Hindi: {hindi_translation.text}")
    tts = gTTS(text=hindi_translation.text, lang='hi')
    tts.save("hindi_speech.mp3")
    os.system("start hindi_speech.mp3")
except :
    print("Sorry cant Translate...")