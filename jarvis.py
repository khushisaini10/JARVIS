import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import keyboard
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# 45print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master. Welcome back.")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Master. Welcome back.")

    else:
        speak("Good Evening Master. Welcome back.")

    speak("I am Jarvis. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Master said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open music' in query:
            webbrowser.open("www.spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Master the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\PyCharm Community Edition 2024.1.5\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'in youtube' in query:
            webbrowser.open("https:\\www.youtube.com\\results?search_query=" + query)
            speak("This is what i've found master")

        elif 'close youtube' in query:
            speak("working on it , master")
            os.system("TASKKILL /F /im youtube.exe")
            speak("done master")

        elif 'in google' in query:
            webbrowser.open("https:\\www.bing.com\\search?pglt=675&q=" + query)
            speak("This is what i've found master")

        elif 'song' in query:
            webbrowser.open("https://open.spotify.com/search/" + query)


        elif 'go to sleep' in query:
            speak("ok master, call me anytime...")
            sys.exit("thankyou for using me master")

        elif 'website' in query:
            speak("which website do you want to open master?")
            name = takeCommand()
            # to remove spaces from the website name
            name = name.replace(" ", "")
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)

        elif 'stop' in query:
            keyboard.press("k")

        elif 'start' in query:
            keyboard.press("k")

        elif 'full screen' in query:
            keyboard.press("f")

        elif 'cinema mode' in query:
            keyboard.press("t")

        elif 'miniplayer' in query:
            keyboard.press("i")

        elif 'mute' in query:
            keyboard.press("m")

        elif 'skip' in query:
            keyboard.press("l")

        elif 'back' in query:
            keyboard.press("j")

        elif 'next video' in query:
            keyboard.press("shift + n")





