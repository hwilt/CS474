"""
RPG game using voice prompts
"""

import sys
import time
import pyttsx3
import speech_recognition as sr
from player import *

class Voice():
    def __init__(self, tts):
        self.tts = tts
    
    def speak(self, tts, text):
        tts.say(text)
        tts.runAndWait()

    def listen(self):
        res = []
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Please Speak.")
            user_input = None
            sys.stdout.write(">")
            listener.pause_threshold = 0.5
            audio = listener.listen(source, timeout=10)
            try:
                user_input = listener.recognize_google(audio, show_all = True)
                alternatives = inputs.get('alternative')[0]
                print(alternatives)
                res.append(alternatives)
                #self.speak(self.tts, user_input)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            except OSError:
                print("No speech detected")
        return res

    def get_user_input(self):
        user_input = None
        while user_input is None:
            user_input = self.listen()
        return user_input

def character_create(tts, voice):
    res = None
    voice.speak(tts, "What is your name?")
    name = voice.get_user_input()
    voice.speak(tts, "Hello, " + name[0] + ".")
    res = Player()
    res.set_name(name[0])
    return res



def gameloop():
    tts = pyttsx3.init()
    voice = Voice(tts)
    print(voice.get_user_input())
    character_create(tts, voice)

    
    

if __name__ == "__main__":
    gameloop()