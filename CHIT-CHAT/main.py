import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice
def listen():
    while True:
        with sr.Microphone() as source:
            print("Processing...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Interpreting...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Can you repeat that?")
            continue  # Continue listening until speech is recognized
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""  # Return an empty string on request error

# Function to open applications
def open_application(application_name):
    try:
        if "browser" in application_name:
            speak("Opening browser.")
            webbrowser.open("https://www.google.com")
        elif "chrome" in application_name:
            speak("Opening Google Chrome.")
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open_new_tab("https://www.google.com")
        elif "notepad" in application_name:
            speak("Opening Notepad.")
            os.system("start notepad")
        elif "student login" in application_name:
            speak("Opening University login page.")
            webbrowser.open("https://students.cuchd.in/")
        elif "study page" in application_name:
            speak("Opening Study login page for student.")
            webbrowser.open("https://lms.cuchd.in/login/index.php")
        elif "gpt" in application_name:
            speak("Opening Chat GPT.")
            webbrowser.open("https://chat.openai.com/")
        elif "computer" in application_name:
            speak("Opening local disk.")
            os.startfile("C:")
        elif "camera" in application_name:
            speak("Opening Camera.")
            os.system("start microsoft.windows.camera:")
        elif "youtube" in application_name:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")
        elif "calculator" in application_name:
            speak("Opening Calculator.")
            os.system("start calc")
        elif "instagram" in application_name:
            speak("Opening Instagram.")
            webbrowser.open("https://www.instagram.com")
        elif "whatsapp" in application_name:
            speak("Opening WhatsApp.")
            webbrowser.open("https://web.whatsapp.com/")
        elif "facebook" in application_name:
            speak("Opening facebook")
            webbrowser.open("https://www.facebook.com/")
        elif "netflix" in application_name:
            speak("Opening Netflix")
            webbrowser.open("https://www.netflix.com")
        else:
            speak("Sorry, I cannot open that application.")
    except Exception as e:
        speak("Sorry, there was an error opening the application.")

# Main function to interact with the user
def main():
    speak("Hello Sir! Good Morning ! I am your voice assistant. CHIT-CHAT. How can I Help you today?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "who program you" in query:
            speak("I am a chit-chat programed by Akash Pandey & Parv Chaubey. There U I D are 21BCA1873 & 21BCA1176 ")
        elif "tell me about you" in query:
            speak("I am a chit-chat. the internet assistent , I help you to open application in this PC. Also , you using me right now.")
        elif "good morning" in query:
            speak("Good Morning Sir! Mey,META. makes your day wonderful")
        elif "good" in query or "better" in query:
            speak("Thats fantastic")
        elif "open" in query:
            open_application(query)
            speak("Application opened.")
        elif "thanks" in query:
            speak("Thanks for using me!")
            break
        else:
            speak("Sorry, I didn't understand. Can you repeat that ?")

if __name__ == "__main__":
    main()
