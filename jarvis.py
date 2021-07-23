##============Package Installation Needed Run this Commands in your Terminal or cmd or Powershell===========##
'''
pip install pyttsx3
pip install speechRecognition
pip install wikipedia
pip install datatime
pip install opencv-python
pip install pywhatkit
pip install pyjokes
pip install ecaptur==0.0.7

'''
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import time 
import random
import string
import cv2
import pywhatkit
import pyjokes
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me How may I help you")

def takeC():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        q=r.recognize_google(audio, language='en-in')
        print(f"User said: {q}\n")
    except Exception as e:
        #print(e)
        print("Say that again please.....")
        speak("Say that again please")
        return "None"
    return q

def sendEmail(to, content):
    p='############' # Erase # symbol and Enter your phone number
    q='######@gmail.com' # Erase # symbol Enter your gmail id
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(q,p)
    server.sendmail(q,to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    #if 1:
    while True:
        query = takeC().lower()

        ##===============================Open Wikipedia====================================================##
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(3)
            speak("Next Commond")
            
        ##===============================Open Youtube======================================================##    
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            time.sleep(3)
            speak("Next Commond")

        ##===============================Open Google=======================================================##            
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
            time.sleep(3)
            speak("Next Commond")

        ##==========================Open Data Structure Playlist===========================================##            
        elif 'open data structure playlist' in query:
            speak("Opening Data Structure Youtube Play List")
            webbrowser.open("https://youtube.com/playlist?list=PLir19lgiavA3naiXm-LQY8MrS6Y_X6QIL")
            time.sleep(3)
            speak("Next Commond")

        ##============================Play Music===========================================================##   
        elif 'music' in query:
            music_dir = 'O:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            time.sleep(3)
            speak("Next Commond")

        ##=============================Time================================================================##   
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            time.sleep(3)
            speak("Next Commond")

        ##=========================Email or Gmail==========================================================## 
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeC()
                to = "#####@gmail.com" # Replace # to gmail id
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry email not send")
                
        ##============================Searching============================================================##       
        elif 'search' in query or 'find' in query:
            speak('Searching')
            query = query.replace("search", "")
            webbrowser.open(query)
            speak("Your Search is Successfull")
            time.sleep(3)
            speak("Next Commond")
            
        ##============================Shutdown and Restart=================================================##
        elif 'shut down' in query:
            speak('Shutdowning Your System')
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            speak('Restarting Your System')
            os.system("shutdown /r /t 1")
            
        ##==========================Taking Personal========================================================##
        elif "how are you" in query:
            speak("I am Fine Sir")
            speak("What about you Sir")
        elif "fine" in query or 'great' in query or 'cool' in query:
            speak("I am glad to speak You Sir")
            speak("What is my next command sir")
            
        ##============================Jokes================================================================##
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            time.sleep(3)
            speak("Next Commond")

        ##=========================Click Photo=============================================================##
        elif 'take a photo' in query or  'click photo' in query:
            a=random.choice(string.ascii_letters)
            b=random.choice(string.ascii_letters)
            c=a+b
            s=cv2.VideoCapture(0)
            r=True
            ret,frame = s.read()
            cv2.imwrite(c+".jpg",frame)
            s.release()
            cv2.destroyAllWindows()
            speak("Image Captured Successfully")
            time.sleep(3)
            speak("Next Commond")

        ##=========================Whatsapp Message Sender=================================================##
        elif 'send meassge to whatsapp' in query:
            pywhatkit.sendwhatmsg("+917020409611",'Good Afternoon',13,11)
            speak("Meassage Send Successfully")

            
        ##=============================Exit================================================================##
        elif 'exit' in query or 'stop' in query or 'good bye' in query or 'ok bye' in query:
            speak("Thank You Sir Using Me, Now I am shutting down")
            exit()

        ##============================Web Browser==========================================================##
        else:
            webbrowser.open(query)
            speak(query+"Searching on Google")
            time.sleep(4)
            speak("Next Commoand")
