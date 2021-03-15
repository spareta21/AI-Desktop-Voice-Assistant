import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of current voices

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Ma'am!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Ma'am!")

    else:
        speak("Good Evening Ma'am!")

    speak("I am Anna, Please tell me how may help you.")


def takeCommand():
    '''
    It takes microphone input from the user and returns the string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # we can took a pause of 1 sec while speaking
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query} \n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('spareta21@gmail.com','panasonic_t40')
    server.sendmail('spareta21@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        #Logic for executing commands based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'play music' in query:
            music_dir = 'F:\\New folder\\party songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Ma'am the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\SHRADDHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to shraddha' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "spareta21@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")

        elif 'no thanks' in query:
            speak("thanks for using me mam, have a good day!")
            sys.exit()

        speak("Mam, do you have any other work?")