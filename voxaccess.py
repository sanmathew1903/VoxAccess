import speech_recognition as sr
import pyttsx3
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
s=pyttsx3.init()
voices=s.getProperty('voices')
s.setProperty('voice',voices[1].id) # id[1] is for female voice
def speak(audio):     # this is the speak function
    s.say(audio)
    s.runAndWait()

r=sr.Recognizer()  # recognises audio
with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source, duration=5)   # checks the environment of user
  r.dynamic_energy_threshold = True    # sets the recognizer acc. to noise in environment
  #speak("what can i do for you sir")
  speak("say password")

  audio=r.listen(source)
  text=r.recognize_google(audio,language="en-in").lower()
  print(text)
  a="apple"
  if text==a:
    speak("welcome sir")
    i=1
    while i==1:
      try:
        
        with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source, duration=5)
          r.dynamic_energy_threshold = True
          speak("what can i do for you")
          audio=r.listen(source)
          text=r.recognize_google(audio,language="en-in").lower()
          print(text)


          if "hello" in text:
              speak("hello sir")


          elif "who are you" in text:
            speak("I am a artificial intelligaence developed by San ")
          
          elif "what can you do" in text:
            speak("i can help you with google,youtube and watsapp ")


          elif "open whatsapp" in text:
            speak("opening whatsapp sir")
            chromedriver="E:\\chromedriver"
            driver=webdriver.Chrome(chromedriver)
            driver.get("https://web.whatsapp.com/")
            speak("please scan the code sir")


            #voice automating wassup  currently incomplete
            
            #taking name
            with sr.Microphone() as source:
              r.adjust_for_ambient_noise(source, duration=5)
              r.dynamic_energy_threshold = True
              speak("whom do u wnat to send the message sir")
              audio=r.listen(source)
              text=r.recognize_google(audio,language="en-in").lower()
              name=text
              print(name)

            #taking message
            with sr.Microphone() as source:
              r.adjust_for_ambient_noise(source, duration=5)
              r.dynamic_energy_threshold = True
              speak("what is the message sir")
              audio=r.listen(source)
              message=r.recognize_google(audio,language="en-in").lower()
              msg=message
              print(msg)

            #taking no of times
            with sr.Microphone() as source:
              r.adjust_for_ambient_noise(source, duration=5)
              r.dynamic_energy_threshold = True
              speak("what number of times do you want to send this message sir")
              audio=r.listen(source)
              no=r.recognize_google(audio).lower()
              count=int(no)
              print(count)

              chat=driver.find_element_by_css_selector('#side > header > div._3euVJ > div > span > div:nth-child(2)')
              chat.click()


              openbox=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]')
              openbox.send_keys(name)
              openbox.send_keys(Keys.RETURN)

              msg_box=driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")

                                            
              for i in range(count):
                msg_box.send_keys(msg)
                button=driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div:nth-child(3) > button")
                button.click()
                


          elif "open google" in text:
            speak("opening google sir")
            #webbrowser.open("google.com")  
            chromedriver="E:\\chromedriver"
            driver=webdriver.Chrome(chromedriver)
            driver.get("https://google.com/")

            #searching gooole
              
            with sr.Microphone() as source:
              r.adjust_for_ambient_noise(source, duration=5)
              r.dynamic_energy_threshold = True
              speak("what do you want to search sir")
              audio=r.listen(source)
              text=r.recognize_google(audio,language="en-in").lower()
              print(text)
              n=text
              
              search=driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
              search.send_keys(n)
              search.send_keys(Keys.RETURN)
              #tsf > div:nth-child(2) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input


          elif "open youtube" in text:
            speak("opening youtube")
            chromedriver="E:\\chromedriver"
            driver=webdriver.Chrome(chromedriver)
            driver.get("https://youtube.com/")
            with sr.Microphone() as source:
              r.adjust_for_ambient_noise(source, duration=5)
              r.dynamic_energy_threshold = True
              speak("what do you want to search sir")
              audio=r.listen(source)
              text=r.recognize_google(audio,language="en-in").lower()
              print(text)
              n=text
              #
              search=driver.find_element_by_name("search_query")
              search.send_keys(n)
              search.send_keys(Keys.RETURN)




          elif "quit" or "exit" in text:
            speak("quitting sir")
            speak("thank you sir")
            i=2


      
      #else:
       # speak("incorrect password")

      except Exception:
        speak("didn't get that sir")
    #  speak(text)
    
  #    speak("didnt get that sir ")