from time import time
import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say something .. ")
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("You are saying:")
        print(text)

    except:
        print("Sorry")

