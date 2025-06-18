# -------------------------------
# 📦 LIBRARY IMPORTS
# -------------------------------
import speech_recognition as sr           # Speech-to-text
import pyttsx3                            # Text-to-speech
import os                                 # For launching apps
import datetime                           # For current time
import psutil                             # To check battery info
import webbrowser                         # For opening websites
import ctypes                             # To lock screen

# -------------------------------
# 🔊 INIT TEXT TO SPEECH
# -------------------------------
tts = pyttsx3.init()
recognizer = sr.Recognizer()

# -------------------------------
# 🎤 SPEAK FUNCTION
# -------------------------------
def speak(text):
    print("Assistant:", text)
    tts.say(text)
    tts.runAndWait()

# -------------------------------
# 🎧 WAKE WORD LISTENER
# -------------------------------
def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Waiting for wake word 'jarvis'...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                trigger = recognizer.recognize_google(audio).lower()
                print("Heard:", trigger)
                if "jarvis" in trigger:
                    speak("Yes, I'm listening...")
                    return
            except:
                continue

# -------------------------------
# 🎧 COMMAND LISTENER
# -------------------------------
def recognize_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source, timeout=None)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("Command:", command)
            return command
        except:
            return ""

# -------------------------------
# ⚙️ COMMAND HANDLER
# -------------------------------
def process_command(command):
    if "hello" in command:
        speak("Hello there!")

    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")

    elif "open file explorer" in command:
        speak("Opening File Explorer.")
        os.system("explorer.exe")

    elif "Google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    
    elif "email" in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif "search for" in command:
        search_query = command.split("search for")[-1].strip()
        if search_query:
            speak(f"Searching Google for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("What should I search for?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "battery" in command:
        battery = psutil.sensors_battery()
        speak(f"Battery is at {battery.percent} percent.")

    elif "lock the screen" in command:
        speak("Locking the screen.")
        ctypes.windll.user32.LockWorkStation()

    elif "exit" in command or "goodbye" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

# -------------------------------
# 🚀 MAIN LOOP
# -------------------------------
while True:
    listen_for_wake_word()
    command = recognize_command()
    if command:
        process_command(command)
