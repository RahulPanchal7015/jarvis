import speech_recognition as sr
import webbrowser
import pyttsx3

import musiclibrary

#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open instagrame" in c.lower():
        webbrowser.open("http:/instagrame.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)


   




if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen for the wake word "Jarvis..."
        #obtain audio from the microphone
        r = sr.Recognizer()
        


        print("recognizing...")
        try: 
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                # listen for command  
                with sr.Microphone() as source:
                    print(" Jarvis active ")
                    audio = r.listen(source) 
                    command= r.recognize_google(audio)  

                    processcommand(command)

        except Exception as e:
            print(" eroor; {0}".format(e))

