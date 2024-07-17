import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
engine = pyttsx3.init()
recognizer = sr.Recognizer()
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)
options = Options()
service = Service(ChromeDriverManager().install())


def opengoogle():
    speak("opening Google ")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://google.com/")
    speak("what do you want to search ")

    text = recognize()
    search = driver.find_element(By.NAME, 'q')
    search.send_keys(text)
    search.send_keys(Keys.RETURN)


def openyoutube():
    speak("opening youtube ")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.youtube.com/")
    speak("what do you want to search, sir")

    text = recognize()
    search = driver.find_element(By.NAME, 'search_query')
    search.send_keys(text)
    search.send_keys(Keys.RETURN)


def sendmessage():
    speak("opening WhatsApp ")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://web.whatsapp.com/")
    
    speak("Please enter the details to send message ")
    name=input("Enter name")
    msg=input("Enter msg")
    no=int(input("no of times to spam"))
    try:
        search_box =driver.find_element("xpath",'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
        search_box.click()
        search_box.send_keys(name)
        search_box.send_keys(Keys.ENTER)


        for i in range(no+1):
            textbox=driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            textbox.send_keys(msg)
            textbox.send_keys(Keys.ENTER)

    
        time.sleep(300)
        driver.quit()

    except:
        time.sleep(10)
        driver.quit()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def recognize():
    print("Speak")
    with sr.Microphone() as source:
        recognizer.energy_threshold = 300
        recognizer.pause_threshold = 0.5
        audio_text = recognizer.record(source, duration=5)
        """ audio_text = recognizer.listen(source) """
    try:
        return recognizer.recognize_google(audio_text)
    except:
        return ("Sorry, I did not get that")


while 1:
    speak("What do u wanna do ?")
    text = recognize()
    text = text.lower()

    print(text)
    if "open google" in text:
        opengoogle()
    elif "open youtube" in text:
        openyoutube()
    elif "send message" in text:
        sendmessage()
    elif "stop" in text:
        speak("Exit")
        exit(0)
    else:
        speak("didnt get that ")
