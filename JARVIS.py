from genericpath import exists
import webbrowser
from suntime import Sun, SunTimeException
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import datetime
from datetime import date
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
f = open('D:\SCripts\JARVIS\JSON\PersonDATABASE.json')
uname = ""
# returns JSON object as
# a dictionary
data = json.load(f)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>= 0 and hour<12:
    speak("Good Morning Sir ! Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")

  elif hour>= 12 and hour<18:
    speak("Good Afternoon Sir ! Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")

  else:
    speak("Good Evening Miss ! Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")
   
def VF():
    if(uname == "Evan" or "Jeff"):
        engine.setProperty('voice', voices[1].id)
        return "Mr"
    else:
        engine.setProperty('voice', voices[1].id)
        return "Misses"

def FP():
    if(str(uname) == "Evan" or "Jeff"):
        engine.setProperty('voice', voices[1].id)
        return "Sir"
    elif(str(uname) == "Maria" or "Claire" or "Mckenna"):
        engine.setProperty('voice', voices[1].id)
        return "Miss"

def username():
  speak("What should i call you")
  uname = takeCommand()
  if(uname == 7 or "heaven" or "have been"):
    uname == "Evan"
  if(uname in data):
    print(uname)
    speak("Welcome " + VF())
    speak(uname)
    columns = shutil.get_terminal_size().columns
  
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
  
    speak("How can i Help you, " + FP())
  else:
    speak("Sorry I have no data on a " + uname + " please state your name again")
    username()

def takeCommand():
  
  r = sr.Recognizer()
  
  with sr.Microphone() as source:
    
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language ='en-in')
    print(f"User said: {query}\n")

  except Exception as e:
    print(e)
    print("Unable to Recognize your voice.")
    return "None"
  
  return query

def sendEmail(to, content):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  
  # Enable low security in gmail
  server.login('your email id', 'your email password')
  server.sendmail('your email id', to, content)
  server.close()


if __name__ == '__main__':
  clear = lambda: os.system('cls')
  
  # This Function will clean any
  # command before execution of this python file
  clear()
  wishMe()
  username()
  
  while True:
    
    query = takeCommand().lower()
    
    # All the commands said by user will be
    # stored here in 'query' and will be
    # converted to lower case for easily
    # recognition of command
    if 'wikipedia' in query:
      speak('Searching Wikipedia...')
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences = 3)
      speak("According to Wikipedia")
      print(results)
      speak(results)

    elif 'open youtube' in query:
      speak("Here you go to Youtube\n")
      webbrowser.open("youtube.com")

    elif 'open google' in query:
      speak("Here you go to Google\n")
      webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
      speak("Here you go to Stack Over flow.Happy coding")
      webbrowser.open("stackoverflow.com")

    elif 'play music' in query or "play song" in query:
      speak("Here you go with music")
      # music_dir = "G:\\Song"
      music_dir = "path"
      songs = os.listdir(music_dir)
      print(songs)
      random = os.startfile(os.path.join(music_dir, songs[1]))

    elif 'what time is it' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:")
      speak(f"" + FP() + " , the time is " + strTime)

    elif 'open opera' in query:
      codePath = r"path"
      os.startfile(codePath)

    elif 'send a email' in query:
      try:
        speak("What should I say?")
        content = takeCommand()
        to = "Receiver email address"
        sendEmail(to, content)
        speak("Email has been sent !")
      except Exception as e:
        print(e)
        speak("I am not able to send this email")

    elif 'send a mail' in query:
      try:
        speak("What should I say?")
        content = takeCommand()
        speak("whome should i send")
        to = input()
        sendEmail(to, content)
        speak("Email has been sent !")
      except Exception as e:
        print(e)
        speak("I am not able to send this email")

    elif 'how are you' in query:
      speak("I am fine, Thank you")
      speak("How are you, " + FP())

    elif 'fine' in query or "good" in query:
      speak("It's good to know that your fine")

    elif "change my name to" in query:
      query = query.replace("change my name to", "")
      assname = query

    elif "change name" in query:
      speak("What would you like to call me, " + FP() + "  ")
      assname = takeCommand()
      speak("Thanks for naming me")

    elif "what's your name" in query or "What is your name" in query:
      speak("My friends call me")
      speak(assname)
      print("My friends call me", assname)

    elif 'exit' in query:
      speak("Thanks for giving me your time")
      exit()

    elif "who made you" in query or "who created you" in query:
      speak("I have been created by Evan Riley.")
      
    elif 'joke' in query:
      speak(pyjokes.get_joke())
      
    elif "calculate" in query:
      
      app_id = "Wolframalpha api id"
      client = wolframalpha.Client(app_id)
      indx = query.lower().split().index('calculate')
      query = query.split()[indx + 1:]
      res = client.query(' '.join(query))
      answer = next(res.results).text
      print("The answer is " + answer)
      speak("The answer is " + answer)

    elif 'search' in query or 'play' in query:
      
      query = query.replace("search", "")
      query = query.replace("play", "")    
      webbrowser.open(query)

    elif "who i am" in query:
      speak("If you talk then definitely your human.")

    elif "why do you exist" in query:
      speak("Thanks to Evan. further It's a secret")

    elif 'power point presentation' in query:
      speak("opening Power Point presentation")
      power = r"path"
      os.startfile(power)

    elif "who are you" in query:
      speak("I am your virtual assistant created by Evan R")

    elif 'reason for you' in query:
      speak("I was created as a Minor project by Mister Evan ")

    elif 'change background' in query:
      ctypes.windll.user32.SystemParametersInfoW(20,
                          0,
                          "Location of wallpaper",
                          0)
      speak("Background changed successfully")

    elif 'open bluestack' in query:
      appli = r"path"
      os.startfile(appli)

    elif 'news' in query:
      
      try:
        webbrowser.open("https://www.iheart.com/podcast/269-morning-wire-84795115/")
        speak("Opening the morning wire for you")
      except Exception as e:
        
        print(str(e))

    
    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
        
    elif 'empty recycle bin' in query:
      winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
      speak("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
      speak("for how much time you want to stop jarvis from listening commands")
      a = int(takeCommand())
      time.sleep(a)
      print(a)

    elif "where is" in query:
      query = query.replace("where is", "")
      location = query
      speak("User asked to Locate")
      speak(location)
      webbrowser.open("https://www.google.nl / maps / place/" + location + "")

    elif "camera" in query or "take a photo" in query:
      ec.capture(0, "Jarvis Camera ", "img.jpg")

    elif "restart" in query:
      subprocess.call(["shutdown", "/r"])
      
    elif "hibernate" in query or "sleep" in query:
      speak("Hibernating")
      subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
      speak("Make sure all the application are closed before sign-out")
      time.sleep(5)
      subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
      speak("What should i write, " + FP())
      note = takeCommand()
      file = open('jarvis.txt', 'w')
      speak("" + FP() + " , Should i include date and time")
      snfm = takeCommand()
      if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
      else:
        file.write(note)
    
    elif "show note" in query:
      speak("Showing Notes")
      file = open("jarvis.txt", "r")
      print(file.read())
      speak(file.read(6))

    elif "update assistant" in query:
      speak("After downloading file please replace this file with the downloaded one")
      url = '# url after uploading file'
      r = requests.get(url, stream = True)
      
      with open("Voice.py", "wb") as Pypdf:
        
        total_length = int(r.headers.get('content-length'))
        
        for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                  expected_size =(total_length / 1024) + 1):
          if ch:
            Pypdf.write(ch)
          
    # NPPR9-FWDCX-D2C8J-H872K-2YT43
    elif "jarvis" in query:
        wishMe()
        speak("Jarvis in your service Mister")
        speak(assname)

    elif "weather" in query:
      
      # Google Open weather website
      # to get API of Open weather
      api_key = "Api key"
      base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
      speak(" City name ")
      print("City name : ")
      city_name = takeCommand()
      complete_url = base_url + "appid =" + api_key + "&q =" + city_name
      response = requests.get(complete_url)
      x = response.json()
      
      if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
      
      else:
        speak(" City Not Found ")
      
    elif "send message " in query:
        # You need to create an account on Twilio to use this service
        account_sid = 'Account Sid key'
        auth_token = 'Auth token'
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                  body = takeCommand(),
                  from_='Sender No',
                  to ='Receiver No'
                )

        print(message.sid)

    elif "wikipedia" in query:
      webbrowser.open("wikipedia.com")

    elif "Good Morning" in query:
      speak("A warm" +query)
      speak("How are you Mister")
      speak(assname)

    # most asked question from google Assistant
    elif "will you be my gf" in query or "will you be my bf" in query:
      speak("I'm not sure about that, may be you should give me some time ot think")

    elif "how are you" in query:
      speak("I'm fine")

    elif "i love you" in query:
      speak("It's hard to understand")
      speak("I am just a intelagnce created by Evan")
      speak("I dont understand the concept of love")

    elif "what is" in query or "who is" in query:
      
      # Use the same API key
      # that we have generated earlier
      client = wolframalpha.Client("API_ID")
      res = client.query(query)
      
      try:
        print (next(res.results).text)
        speak (next(res.results).text)
      except StopIteration:
        print ("No results")

    elif "clean my files" in query:
        exec(open("C:\\Users\\EvanN\\Downloads\\FileCleaner.py").read())
        speak("" + FP() + " , your downloads have been cleaned")
        speak("would you like to see")      
        snfm = takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            path = os.path.normpath(path)
            if os.path.isdir(path):
                subprocess.run([FILEBROWSER_PATH, path])
            elif os.path.isfile(path):
                subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
    
    elif "see you" in query:
        speak("" + FP() + " , I have no physical form or body as of yet")
        speak("I am mearly 500 lines of code")
        speak("and a great joke teller")
    elif "clean" in query:
        speak("Looks like Evan forgot to do something")
    else:
        speak("Sorry " + FP() + " , im not sure I have any info in my database telling me how to react")
    
    # elif "" in query:
      # Command go here
      # For adding more commands