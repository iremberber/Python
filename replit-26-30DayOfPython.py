#day26

import os , time

print("Welcome")
print("to")
print("Replit")

time.sleep(1)
os.system("clear")
username = input("Username: ")

#challenge

from replit import audio
import os, time
def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
    if stop_playback == 2:
      source.paused = True # let's pause the file 
      return # let's go back from this play() subroutine
    else: 
      continue

while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue

  #day27 Project Day

  name = input("What is your character name? ")
type = input("What is your character type? ")

import random, time, os
os.system("clear")
time.sleep(1)
def roll_dice(dice1,dice2):
  healt = (dice1*dice2/2)+10
  return healt
healt = roll_dice(random.randint(1,6),random.randint(1,12))

print(name + "'s healt is " + str(healt)+ "ph")

def roll_dice2(dice11,dice22):
  strength = (dice11*dice22/2)+12
  return strength
strength = roll_dice2(random.randint(1,6),random.randint(1,12))

print(name + "'s strength is " + str(strength)+ "ph")

#day28

import random
import os
import time

def rollDice(side):
    result = random.randint(1, side)
    return result

def health():
    healthStat = ((rollDice(6) * rollDice(12)) / 2) + 10
    return healthStat

def strength():
    strengthStat = ((rollDice(6) * rollDice(8)) / 2) + 12
    return strengthStat

print("⚔️ CHARACTER BUILDER ⚔️")
print()

name1 = input("Name your Legend:\n")
type1 = input("Character Type (Human, Elf, Wizard, Orc):\n")

name2 = input("Name your Legend:\n")
type2 = input("Character Type (Human, Elf, Wizard, Orc):\n")

health1 = health()
strength1 = strength()
health2 = health()
strength2 = strength()

print()
print(name1)
print("HEALTH:", health1)
print("STRENGTH:", strength1)
print()

print()
print(name2)
print("HEALTH:", health2)
print("STRENGTH:", strength2)
print()

time.sleep(1)
os.system("clear")

print("Battle Time!")

round = 1
winner = None

while True:
    time.sleep(1)
    os.system("clear")
    Dice1 = rollDice(6)
    Dice2 = rollDice(6)
    difference = abs(strength1 - strength2) + 1

    if Dice1 > Dice2:
        health2 -= difference
        if round == 1:
            print(name1, "wins the first blow")
        else:
            print(name1, "wins round", round)
    elif Dice2 > Dice1:
        health1 -= difference
        if round == 1:
            print(name2, "wins the first blow")
        else:
            print(name2, "wins round", round)
    else:
        print("Their swords clash and they draw round", round)

    print()
    print(name1)
    print("HEALTH:", health1)
    print()
    print(name2)
    print("HEALTH:", health2)
    print()

    if health1 <= 0:
        print(name1, "has died!")
        winner = name2
        break
    elif health2 <= 0:
        print(name2, "has died!")
        winner = name1
        break
    else:
        print("And they're both standing for the next round")
        round += 1

    time.sleep(1)
    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    print()

print(winner, "has won in", round, "rounds")

#day29

for i in range(0, 10):
  print(i, end="ıma yaptım ")

print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.1)
  os.system("clear")
  print('\033[?25h', end="")

#challange
  
def newPrint(color, word):
  if color=="red":
    print("\033[0;31m", word, sep="", end="")
  elif color=="blue":
    print("\033[0;34m", word, sep="", end="")
  else:
    print(word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue")

#day30

name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))

name = "Katie"
age = "28"
pronouns = "she/her"
print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))

name = "Katie"
age = "28"
pronouns = "she/her"
response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"
print(response)

for i in range(1, 31):
  print(f"Day {i : ^2} of 30")

#fixmycodepart

"""
food = pizza"
location = "beach"
color = "green"
friend = "Quinn"
"Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame." format(food=food, location=location, color=color,)
print(response)
"""

food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"
response = f"Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame."
print(response)

#challenge

print("30 Days Down")

i = 1
while i < 31:
  print(f"How was the Day {i}?")
  answer = input()

  response = f"Day {i} was {answer}."
  i += 1
  print(f"{response:^35}")

else:
  print("That's all you finish! Keep going!")

  