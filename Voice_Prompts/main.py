"""
RPG game using voice prompts
"""

import sys
import time
import pyttsx3
import speech_recognition as sr
import os
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
            self.speak(self.tts, "Please Speak now")
            user_input = None
            time.sleep(0.5)
            sys.stdout.write(">")
            listener.pause_threshold = 0.5
            audio = listener.listen(source, timeout=10)
            try:
                user_input = listener.recognize_google(audio, show_all = True)
                try:
                    #print(user_input)
                    i = 0
                    while i < len(user_input['alternative']):
                        _new = []
                        _new.append(str(user_input['alternative'][i]['transcript']))
                        _new.append(str(user_input['alternative'][i]['confidence']))
                        i += 1
                        res.append(_new)
                except:
                    res.append(user_input)
                print(res)
                #res.append(user_input)
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

def direction(tts, voice):
    voice.speak(tts, "Which direction would you like to go?")
    voice.speak(tts, "Please say 'forward', 'behind', 'left', or 'right'.")
    direction = voice.get_user_input()
    while direction[0][1] <= 0.5 or direction[0][0] == "" or direction:
        voice.speak(tts, "I'm sorry, I didn't catch that.")
        direction = voice.get_user_input()
    direction = str(direction[0][0])
    if "forward" in direction.lower():
        direction = "forward"
    elif "behind" in direction.lower():
        direction = "behind"
    elif "left" in direction.lower():
        direction = "left" 
    elif "right" in direction.lower():
        direction = "right"
    return direction
    

def pickup(tts, voice):
    voice.speak(tts, "Do you wish to pick up the item?")
    voice.speak(tts, "Please say 'yes' or 'no'.")
    pickup = voice.get_user_input()
    while pickup[0][1] <= 0.5 or pickup[0][0] == "" or pickup:
        voice.speak(tts, "I'm sorry, I didn't catch that.")
        pickup = voice.get_user_input()
    pickup = False
    if "yes" in pickup[0][0].lower():
        pickup = True
    return pickup


def character_create(tts, voice):
    res = None
    time.sleep(1)
    voice.speak(tts, "What is your name?")
    name = voice.get_user_input()
    while name[0][1] <= 0.5 or name[0][0] == "" or name:
        voice.speak(tts, "I'm sorry, I didn't catch that.")
        name = voice.get_user_input()
    name = str(name[0][0])
    voice.speak(tts, "Hello, " + name + ".")
    res = Player()
    res.set_name(name)
    return res


def starting_Room(tts, voice, player, cave):
    starting_String = cave['Back of Cave']['description']
    print(starting_String)
    voice.speak(starting_String)
    if 'item' in cave['Back of Cave'].keys():
        ret = pickup(tts, voice)
        if ret:
            player.set_TORCH()
    
    which_direction = direction(tts, voice)
    if "left" in which_direction[0][0]:
        player.set_player_location("small opening")
    elif "right" in which_direction[0][0]:
        player.set_player_location("large opening")
    
def basic_Room(tts, voice, player, cave):
    basic_String = cave[player.get_player_location()]['description']
    print(basic_String)
    voice.speak(basic_String)
    if 'item' in cave[player.get_player_location()].keys():
        ret = pickup(tts, voice)
        if ret:
            player.set_SWORD()
    which_direction = direction(tts, voice)
    if "forward" in which_direction[0][0] and "forward" in cave[player.get_player_location()].keys():
        player.set_player_location(cave[player.get_player_location()]['forward'])
    elif "behind" in which_direction[0][0] and "behind" in cave[player.get_player_location()].keys():
        player.set_player_location(cave[player.get_player_location()]['behind'])
    elif "left" in which_direction[0][0] and "left" in cave[player.get_player_location()].keys():
        player.set_player_location(cave[player.get_player_location()]['left'])
    elif "right" in which_direction[0][0] and "right" in cave[player.get_player_location()].keys():
        player.set_player_location(cave[player.get_player_location()]['right'])
    
def arena_Room(tts, voice, player, cave):
    monster = {
        health: 50,
        attack: 10,
    }
    arena_String = cave[player.get_player_location()]['description']
    print(arena_String)
    voice.speak(arena_String)

    voice.speak(tts, "Do you fight or do you run?")
    voice.speak(tts, "Please say 'fight' or 'run'.")
    fight_or_run = voice.get_user_input()
    while fight_or_run[0][1] <= 0.5 or fight_or_run[0][0] == "" or fight_or_run:
        voice.speak(tts, "I'm sorry, I didn't catch that.")
        fight_or_run = voice.get_user_input()
    fight_or_run = str(fight_or_run[0][0])
    if "fight" in fight_or_run.lower():
        if player.get_SWORD():
            voice.speak(tts, "You take out your sword and kill the monster in one hit.")
            monster['health'] = 0
        else:
            voice.speak(tts, "You take out your fist and hit the monster.")
            player.set_hp(player.get_hp() - (2*monster['attack']))
            voice.speak(tts, "The monster hits you twice but you are still alive, and with one last punch you kill the monster.")
            monster['health'] = 0
        which_direction = direction(tts, voice)
        if "forward" in which_direction[0][0] and "forward" in cave[player.get_player_location()].keys():
            player.set_player_location(cave[player.get_player_location()]['forward'])
        elif "behind" in which_direction[0][0] and "behind" in cave[player.get_player_location()].keys():
            player.set_player_location(cave[player.get_player_location()]['behind'])
        elif "left" in which_direction[0][0] and "left" in cave[player.get_player_location()].keys():
            player.set_player_location(cave[player.get_player_location()]['left'])
        elif "right" in which_direction[0][0] and "right" in cave[player.get_player_location()].keys():
            player.set_player_location(cave[player.get_player_location()]['right'])
    else:
        player.update_location(cave[player.get_player_location()]['left'])
    


def ending_Room(tts, voice, player, cave):
    ending_String = cave[player.get_player_location()]['description']
    print(ending_String)
    voice.speak(ending_String)
    if player.get_GOLD():
        voice.speak(tts, "You collect all the GOLD!")
    if player.get_SWORD():
        voice.speak(tts, "You collect the SWORD!")
    if player.get_TORCH():
        voice.speak(tts, "You collect the TORCH!")
    congrats = """YOU HAVE FOUND THE END OF THE GAME! CONGRATULATIONS!"""
    voice.speak(congrats)
    print(player)

def gameloop():
    cave = {
        'Back of Cave': {
            'left': 'small opening',
            'right': 'large opening',
            'items': 'torch',
            'description': """You are in a cave, there is a light in the distance. On your left, there
            is a small opening. On your right, there is a large opening. In front of you, there are drawings of cave
            of cave men. On the ground, there is a torch."""
        },
        'small opening': {
            'right': 'Back of Cave',
            'forward': 'light at the end',
            'description': """As you crawl through the tight gap in the wall, in front of you, there is a dim light."""
        },
        'light at the end': {
            'behind': 'small opening',
            'forward': 'arena',
            'description': """You are in a small room, there is a light in the distance. To the right of you,
            the walls seem to be opening up as if the cave is leading to a exit."""
        },
        'arena': {
            'behind': 'light at the end',
            'forward': 'cave entrance',
            'description': """You are in a large room, there is a light in the distance. As you look around,
            a large monster comes out the darkness of the room. It is a giant caveman. You can fight the monster
            or run away."""
        },
        'cave entrance': {
            'description': """You come out of the cave, you finally see the sun shining through the trees.
            You are happy that you made it out of the cave alive."""
        },
        'large opening': {
            'left': 'Back of Cave',
            'forward': 'grumbling noises',
            'descripton': """You hear noises in the distance ahead of you. In the corner you can see the start of a mineshaft.
            There is a chest with a sword and gold in it.""",
            'items': ['sword', '50 gold']
        },
        'grumbling noises': {
            'behind': 'large opening',
            'forward': 'cave entrance',
            'description': """The grumbling noises are getting louder and louder. You can hear the sound of a bat come out
            of nowhere. You can see a light in the distance ahead of you."""
        }
    }
    tts = pyttsx3.init()
    voice = Voice(tts)
    #print(voice.get_user_input())
    player = character_create(tts, voice)
    starting_Room(tts, voice, player, cave)

    while player.get_player_location() != 'cave entrance':
        if player.get_player_location() == 'arena':
            arena_Room(tts, voice, player, cave)
        else:
            basic_Room(tts, voice, player, cave)

    ending_Room(tts, voice, player,cave)
    
    

if __name__ == "__main__":
    gameloop()