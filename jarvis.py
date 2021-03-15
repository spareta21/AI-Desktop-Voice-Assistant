import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
# import cv2
import random
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import datetime
import pyjokes
import pyautogui
import time
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:     # use the default microphone as the audio source
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)        # listen for the first phrase and extract it into audio data

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "none"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"Its {current_time}")
    speak("I am Alexa, Please tell me how may help you.")

def news():
    nw = 'http://newsapi.org//v2//top-headlines?sources=techcrunch&apiKey=8e04545b3d994df8845dcc2d25a6b4dd'
    main_page = requests.get(nw).json()
    articles = main_page["articles"]
    head=[]
    day = ["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])

    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if "open notepad" in query:
            npath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd")

        # elif "open camera" in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam',img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break
        #         cap.release()
        #         cv2.destroyAllWindows()
        
        elif 'open youtube' in query:
            speak("what should I play on youtube ?")
            query = takeCommand().lower()
            try:
                kit.playonyt(query)
            except Exception as e:
                speak("Result not found! Please try again...")
            
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif "play music" in query:
            music_dir = "F:\\New folder\\party songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            # for song in songs:
            #     if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir,rd))
            
        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")


        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            try:
                results=wikipedia.summary(query, sentences=2)
                # print(results)
                speak("According to wikipedia")
                speak(results)
            except Exception as e:
                speak("The query is not available on wikipedia..")

        elif 'open google' in query:
            speak("What should I search on google?")
            search = takeCommand().lower() 
            webbrowser.open(search)

        elif "no thanks" in query:
            speak("Thanks for using me ma'am, Have a good day!!")
            sys.exit()

        elif "close notepad" in query:
            speak("Okay ma'am, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        # elif "set alarm" in query:
        #     nn = int(datetime.datetime.now().hour)
        #     if nn==16:
        #         music_dir = "F:\\New folder\\party songs"
        #         songs = os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir,songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "news updates" in query:
            speak("Please wait ma'am, fetching the latest news")
            news()

        elif 'send email to shraddha' in query:
            try:
                speak("What should I say?")
                query = takeCommand().lower()
                if "send a file" in query:
                    email = "spareta21@gmail.com"
                    password = "panasonic_t40"
                    send_to_email = "spareta21@gmail.com"
                    speak("Okay Ma'am, what should be the subject of an email?")
                    query = takeCommand().lower()
                    subject = query
                    speak("and Ma'am, what should be the content of this mail?")
                    query2 = takeCommand().lower()
                    message = query2
                    speak("Please enter the correct path of your file into the shell") 
                    file_location = input("please enter the path here") 
                    
                    speak("Please wait! I am sending the email..")    
                    
                    msg = MIMEMultipart()      
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject']=subject
                    
                    msg.attach(MIMEText(message,'plain'))

                    #setup attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application','octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename = %s" %filename)

                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email,password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email,text)
                    server.quit()
                    speak("Email has been send to shraddha..")

                else:
                    
                    email = "spareta21@gmail.com"
                    password = "panasonic_t40"
                    send_to_email = "spareta21@gmail.com"
                    speak("Okay Ma'am, what should be the subject of an email?")
                    query = takeCommand().lower()
                    subject = query
                    speak("and Ma'am, what should be the content of this mail?")
                    query2 = takeCommand().lower()
                    message = query2
                    speak("Please enter the correct path of your file into the shell") 
                    file_location = input("please enter the path here") 
                    
                    speak("Please wait! I am sending the email..")    
                    
                    msg = MIMEMultipart()      
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject']=subject
                    
                    msg.attach(MIMEText(message,'plain'))

                    #setup attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application','octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename = %s" %filename)

                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email,password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email,text)
                    server.quit()
                    speak("Email has been send to shraddha..")



            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")

        else:
            speak("Sorry..This function is not available mam!")

        speak("Mam, do you have any other work")