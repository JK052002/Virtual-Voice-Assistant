import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3
import datetime
import os
import cv2
import wikipedia
import webbrowser
import pywhatkit as kit
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=2,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query} ")

    except Exception as e:
        speak("say that again please")
        return "none"
    return query

def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")

    elif hour>12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("I am a virtual voice assistant Please tell me how can i help you")

if __name__=="__main__":
    wish()
    #while True:
    if 1:

        query=takecommand().lower()

        if "open notepad" in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir="D:\MUSIC"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime} ")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm=takecommand().lower()
            webbrowser.open((f"{cm}"))


listener = sr.Recognizer()
tts = pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()


def mic():
    with sr.Microphone() as source:
        print ("program is listening....")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        print (data)
        return data.lower()


dict = {"jk":"jkthemass2002@gmail.com"}

def send_mail(receiver,subject,body):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("mightymidas07@gmail.com","rvsimqomwpysllhu")
    email = EmailMessage()
    email["From"] = "mightymidas07@gmail.com"
    email["To"] =  receiver
    email["Subject"] = subject
    email.set_content(body)
    server.send_message(email)

def main_poc():
    talking_tom("To whom do you want to send this email?")
    name = mic()
    receiver = dict[name]
    talking_tom("speak the subject of the email")
    subject = mic()
    talking_tom("speak the message of the email")
    body = mic()
    send_mail(receiver,subject,body)
    print("your email has been sent!!")

main_poc()







