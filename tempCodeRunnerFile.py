import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!!!")
    else:
        speak("Good Evening sir!!!")
    speak("I am SRK sir.Please tell me how may I Help you")

def takeCommand():
    #It takes microphone input from the user and return String as an output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)   
        print("Say that again please......")
        return "None" 
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('201b139@juetguna.in','13112001Kshitij')
    server.sendmail('201b139@juetguna.in',to,content)
    server.close()

if __name__=="__main__":
    speak("SRK is cool")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace ("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:  
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open JUET' in query:
            webbrowser.open("juet.ac.in")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\SRK\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")    
        elif 'open code' in query:
            codePath = "C:\\Users\\Kshitij\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to Kshitij & Pragya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "201b139@juetguna.in","201b183@juetguna.in"
                sendEmail(to ,content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry Sir I am unable to send the email!!")