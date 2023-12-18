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
