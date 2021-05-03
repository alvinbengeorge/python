import pyaudio
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio=r.record(source,duration=5)
    try:
        text=r.recognize_google(audio)
        print("Words: ",text)
    except:
        print("Sorry didnt hear ya")
