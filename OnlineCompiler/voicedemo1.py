import pyttsx3
import speech_recognition as sr              
from colorama import *
import os
import pyautogui
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source,duration=1)
         
         #r.energy_threshold()
         print(Fore.GREEN+"Listening : "+Fore.RESET)
         audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(Fore.YELLOW+text+Fore.RESET)
    except:
        print(Fore.RED+"sorry, could not recognise"+Fore.RESET)
        speak("Cannot Recognise speak again")
    #return "none"
    return text