import speech_recognition as sr
import os
import datetime
from gtts import gTTS
import wikipedia
import random
import warnings
import pyaudio
import calendar
warnings.filterwarnings('ignore')

#PSS listening to commands
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

    return data





#PSS response
def assistantResponse(text):
    print(text)
    myobj=gTTS(text=text,lang='en',slow=False)

    myobj.save('assistant_response.mp3')
    os.system('afplay assistant_response.mp3')

    #text="This is a test by my master Darshil"





def wakewords(text):
    WAKE_WORDS=["hi","hey pss","hi darshil","hai"]
    text=str(text)
    text=text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False





def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum= now.month
    daynum=now.day

    month_names=["January","February","March","April","May","June","July","August","September","October","November","December"]
    ordinal_numbers=["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th",
    "15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th"
    ,"29th","30th","31st"]

    return "Today is "+weekday+", "+month_names[monthNum-1]+" the "+ordinal_numbers[daynum-1]+"."





#returning a greeting
def greeting(text):
    GREETING_INPUTS=["hi","hey","ola","kem chho ?"]
    GREETING_RESPONSES=["hi","hey there","majhama"]

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + "."
            


def getPerson(text):
    wordList=text.split()

    for i in range(0,len(wordList)):
        if i+3 <=len(wordList) -1 and wordList[i].lower()=='who' and wordList[i+1].lower()=='is':
            return wordList[i+2] + wordList[i+3]


while(True):

    text=recordAudio()
    response=''

    if(wakewords(text)==True):
        response=response+greeting(text)
        

        if "date" in text:
            get_date=getDate()
            response=response+" "+get_date

        if "who is" in text:
            person=getPerson(text)
            wiki=wikipedia.summary(person,sentences=2)
            response=response + ' ' + wiki
    
    assistantResponse(response)

