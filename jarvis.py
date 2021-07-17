import speech_recognition as sr
import os
import datetime
from gtts import gTTS
import wikipedia
import random
import warnings
import pyaudio
warnings.filterwarnings('ignore')

def recordAudio():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something\n")
        audio=r.listen(source)

    data=''
    try:
        data=r.recognize_google(audio)
        print("You said: "+data)
    except:
        print("Didn't get ya !")


def assistantResponse(text):
    print(text)
    myobj=gTTS(text=text,lang='en',slow=False)

    myobj.save('assistant_response.mp3')
    os.system('afplay assistant_response.mp3')

text="This is a test by my master Darshil"

recordAudio()
assistantResponse(text)
