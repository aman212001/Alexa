import speech_recognition as sr                 # Making a self Artificial Intelligent Assistance #
import pyttsx3

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
engine.say("I am your Alexa")
engine.say("What can I do for you")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Listening....")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'alexa' in command:
            print(command)

except:
    pass

