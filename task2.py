Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 


import pyttsx3
import speech_recognition as sr
import os 
import datetime 
import webbrowser


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        audio = recognizer.listen(source)
        said=""
    try:
        print("Recognizing...")
        said = recognizer.recognize_google_cloud(audio)
        print("You said:", said)
        
    except Exception as  e:
        print("Exception: "+str(e))

    return said.lower()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_name():
    speak("my name's hossany")
    

def assistant():
    speak("Hello! How can I help you?")
    while True:
        said = listen().lower()

        if "hello" in said:
            speak("Hello there!")
        elif "how are you" in said:
            speak("I'm doing great, thank you!")

        elif "time" in said:
            current_time=datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"the date is {current_time}")

        elif "search" in said:
            speak("what would you like to search?")
            said_search = listen().lower()
            if said_search:
                url=f"https://www.google.com/search?q={said_search}"
                webbrowser.open(url)
        
        elif "bye" in said:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I'm not sure how to help with that.")
while True:
    text=listen()
    if __name__ == "__main__":
        assistant()
