import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

#help(listener)
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)

    except Exception as f:
        print("Error Detectado")
        print(f)

    return command

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time is " + time)
    elif "wikipedia" in command:
        person = command.replace("wikipedia", "")
        info = wikipedia.summary(person)
        print(info)
        talk(info)
    elif "are you single" in command:
        talk("Sorry, I am in a relationship")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    else:
        talk("Please, say the command again")


run_alexa()

