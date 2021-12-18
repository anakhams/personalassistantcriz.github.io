
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess

print('Hi welcome, I am your personal assistant Criz ')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if (hour >= 0) and (hour < 12):
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif (hour >= 12) and (hour < 18):
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Hi welcome, I am your personal assistant Criz")
wishMe()


if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Criz is shutting down,Good bye')
            print('your personal assistant Criz is shutting down,Good bye')
            break

        if 'Open wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open classroom' in statement:
            webbrowser.open_new_tab("https://classroom.google.com")
            speak("Google classroom is open now")
            time.sleep(5)

        elif 'open meet' in statement:
            webbrowser.open_new_tab("https://meet.google.com")
            speak("Google meet is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)


        elif 'Time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-one version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Anakha, Gowri & Meenakshy")
            print("I was built by Anakha, Gowri & Meenakshy")

        elif "open tinkerhub" in statement:
            webbrowser.open_new_tab("https://tinkerhub.org/")
            speak("Tinkerhub is open, Happy reading")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some of the latest news from the Times of India,Happy reading')
            time.sleep(6)


        elif 'weather' in statement:
            news = webbrowser.open_new_tab("https://www.windy.com/?9.963,76.296,5")
            speak('Please enter the location and get the weather update')
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(10)