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

import random, os, time
def rollDice(side):
  result = random.randint(1,side)
  return result
def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat
def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat
print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()
c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()
round = 1
winner = None
while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  c1Dice = rollDice(6)
  c2Dice = rollDice(6)
  difference = abs(c1Strength - c2Strength) + 1
  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)
  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()
  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")