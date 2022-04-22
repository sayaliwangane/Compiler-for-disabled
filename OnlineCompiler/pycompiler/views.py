import sys

from django.shortcuts import render


#Adding libraries
import pyttsx3
import speech_recognition as sr              
from colorama import *
import os
import pyautogui
import time

# Create your views here.

#create index function
def landing(request):
    print("Code inside landing page")
    return render(request, 'landing.html')

def back(request):
    print("Code inside landing page")
    return render(request, 'landing.html')

def text(request):
    print("Code inside text page")
    return render(request, 'text.html')

def sign(request):
    print("Code inside text page")
    return render(request, 'sign.html')


def index(request):
    print("Code inside index page")
    return render(request, 'index.html')

def runcode(request):
    print("Code inside runcode method")
    import datetime;
  
    # ct stores current time
    ct = datetime.datetime.now()
    print("current time:-", ct)
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render(request , 'index.html', {"code":codeareadata , "output":output,"timestamp":ct})


def sign1(request):
    print("Code inside runcode method")
    import datetime;
  
    # ct stores current time
    ct = datetime.datetime.now()
    print("current time:-", ct)
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render(request , 'sign.html', {"code":codeareadata , "output":output,"timestamp":ct})


def text1(request):
    print("Code inside runcode method")
    import datetime;
  
    # ct stores current time
    ct = datetime.datetime.now()
    print("current time:-", ct)
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render(request , 'text.html', {"code":codeareadata , "output":output,"timestamp":ct})

def runOnVoiceCommand(request):
        print("Inside runOnVoiceCommand method")
        while True :            
            query = takecommand()  
                  
            print(query)
            codeareadata=query;
            symbol(query)
            return render(request,'index.html',{"code":codeareadata})


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    print("Inside speak function")
    engine.say(audio)
    engine.runAndWait()

def symbol(a):
    if 'plus' in a.lower():
        pyautogui.write("+")
    elif 'subtract' in a.lower():
        pyautogui.write("-")
    elif 'multiply' in a.lower():
        pyautogui.write("*")
    elif 'divide' in a.lower():
        pyautogui.write("/")
    elif 'equal to' in a.lower():
        pyautogui.write("=")
    elif 'increment' in a.lower():
        pyautogui.write("++")
    elif 'decrement' in a.lower():
        pyautogui.write("--")
    elif 'open circular bracket' in a.lower():
        pyautogui.write("(")
        speak("printing")
    elif 'close circular bracket' in a.lower():
        pyautogui.write(")")
        speak("printing")
    elif 'single inverted comma' in a.lower():
        pyautogui.write("''")
        speak("printing")
    elif 'double quote' in a.lower():
        pyautogui.write("")
    
    elif 'angular brackets' in a.lower():
        pyautogui.write("<>")
    elif 'curly brackets' in a.lower():
        pyautogui.write("{}")
    elif 'dot' in a.lower():
        pyautogui.write(".")
    elif 'next line' in a.lower():
        pyautogui.typewrite(['ENTER'])
    else:
        pyautogui.write(a)

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
   