# importing the required modules

import speech_recognition as sr         # for speech recognition
import pyttsx3                          # for interfacing with our device's text to speech engine
import datetime
import time
import Webscraping                      # Our Webscrapping module
import webbrowser                       # For accessing our webbrowser
import os
import subprocess                       # for running any process


# Function to convert text to speech 

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to take command from the user 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"Sai> {statement}\n")
        except Exception as e:
            speak("Unable to understand, could you repeat that again") 
            return None
        return statement


# Function to wish the user based on the time of the day

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 < hour < 12:
        print('Sara> Hello, Good Morning!, Sai')
        speak('Hello, Good Morning, Sai')
    elif 12 <= hour <= 18:
        print('Sara> Hello, Good Afternoon!, Sai')
        speak('Hello, Good Afternoon, Sai')
    else:
        print('Sara> Hello, Good Evening!, Sai')
        speak('Hello, Good Evening, Sai')


# Main Function where everything happens

if __name__=='__main__':
    engine = pyttsx3.init('sapi5')                  # Initializing the speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)       # Setting the voice as female(Zira)
    wishMe()
    print("Sara> Tell me how can I help you?")
    speak("Tell me how can I help you?")
    
    while True:
        statement = takeCommand().lower()           # changing the statement recognized from the user into lower case
        if statement == 0:
            continue
        
        if 'time' in statement:                                         # if keyword 'time' in statement tell the current time
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Sara> The time is {strTime}")
            speak(f"the time is {strTime}")
            time.sleep(2)                                         
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'date' in statement:                                       # if keyword 'date' in statement tell the current date
            strDate = datetime.date.today()
            print(f"Sara> The date is {strDate}")
            speak(f"the date is {strDate}")
            time.sleep(2)
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'binary tree' in statement:                                # if keyword 'binary tree' in statement scrap the content regarding binary tree
            Webscraping.get_content('Binary Tree')                      # run a function in Webscraping module to fetch content regarding the Binary Tree
            print("Sara> The content on Binary Tree scrapped from the web is shown in a notepad. Have a fun reading")
            speak("the content on Binary Tree scrapped from the web is shown in a notepad. Have a fun reading")
            if 'wikipedia' in statement:                                # open notepad and display the scrapped content
                os.system("notepad.exe " + "Binary Tree_Wiki.txt")
            elif 'javatpoint' in statement:
                os.system("notepad.exe " + "Binary Tree_Javat.txt")
            elif 'tutorials point' in statement:
                os.system("notepad.exe " + "Binary Tree_TutorialsPoint.txt")
            time.sleep(1)
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'wikipedia' in statement:                                 # if keyword 'wikipedia' in statement scrap the content asked from Wikipedia
            statement = statement.replace("wikipedia ", "")
            speak(f'Searching Wikipedia for {statement}')
            results = Webscraping.get_content_from_Wikipedia(statement)     # run a function in Webscraping module to fetch content from Wikipedia
            print(results)
            speak(results)
            print('Sara> For more info you can check the document')
            speak('For more info you can check the document')
            os.system("notepad.exe " + f'{statement}_Wiki.txt')
            time.sleep(1)
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'news' in statement:                                      # if keyword 'news' in statement open and display the headlines from Times Of India
            news = webbrowser.open_new("https://timesofindia.indiatimes.com/home/headlines")
            print('Sara> Here are some headlines from the Times of India,Sir. Happy reading')
            speak('Here are some headlines from the Times of India,Sir. Happy reading')
            time.sleep(6)
            time.sleep(1)
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'joke' in statement:                                      # if keyword 'joke' in statement read a joke
            if 'chuck norris' not in statement:
                joke = Webscraping.get_randomjoke()                    # run a function in Webscraping module to fetch a joke
                print(f"Sara> {joke}")
                speak(joke)
            else:
                joke = Webscraping.get_randomjoke_withoutChuckNorris()
                print(f"Sara> {joke}")
                speak(joke)
                time.sleep(1)
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'project' in statement:                                   # if keyword 'project' in statement open our project in a browser
            twain = webbrowser.open_new("https://twain.pythonanywhere.com/")
            time.sleep(1)
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'search' in statement:                                    # if keyword 'search' in statement search for the requested content in google and display it in a browser
            statement = statement.replace("search", "")
            search_content = statement.replace(" ", "+")
            print("Sara> Searching the requested content in the web, Sir")
            print("Searching the requested content in the web, Sir")
            webbrowser.open_new(f"https://www.google.com/search?b-d&q={search_content}")
            time.sleep(5)
            time.sleep(1)
            print()
            print("Sara> What do you want me to do now?")
            speak("What do you want me to do now?")
        
        elif 'log off' in statement or 'sign out' in statement or 'shutdown' in statement or 'switch off' in statement:            # if any keywords in statement given is spoken by the user turn off the PC
            print('Sara> Turning off your PC in 10 seconds, make sure you save your work')
            speak('Turning off your PC in 10 seconds, make sure you save your work')
            time.sleep(10)
            subprocess.call(["shutdown", "/l"])
        
        elif 'what can you do' in statement or 'what all can I ask' in statement:                  # if any keywords in statement given is spoken by the user speak what are the tasks that the assistant can perform
            print('Sara> I am Sara 1 point 0, I am your personal assistant. I can do some minor tasks such as Searching Wikipedia, scrapping the web for some content, can tell you the current time, news, can do a google search and can tell jokes too!')
            speak('I am Sara 1 point 0, I am your personal assistant. I can do some minor tasks such as Searching Wikipedia, scrapping the web for some content, can tell you the current time, news, can do a google search and can tell jokes too!')
        
        elif 'who made you' in statement or ' who created you' in statement or 'who coded you' in statement:            # if any keywords in statement given is spoken by the user speak the name of the people who wrote the code
            print("Sara> I was made by the legends")
            speak("I was made by the legends")
        
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "thank you" in statement:          # if any keywords in statement given is spoken by the user say 'Thank You' and exit the code
            print("Sara> Have a good day, Sir")
            speak("Have a good day, Sir")
            break