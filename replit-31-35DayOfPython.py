#day31 project day

def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")
    
title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="
print(f"        {title:^35}")
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")
prev = "prev"
next = "next"
pause = "pause"
print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")
print()
print()
text = "WELCOME TO"
print(f"{colorChange('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{colorChange('blue')}{text:^35}")
text = "Definitely not a rip off"
print(f"{colorChange('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colorChange('yellow')}{text:>35}")
text = "networking site"
print(f"{colorChange('yellow')}{text:>35}")
text = "Honest."
print(f"{colorChange('red')}{text:^35}")
text = "Username: "
username = input(f"{colorChange('white')}{text:^35}")
text = "Password: "
username = input(f"{colorChange('white')}{text:^35}")

#day32

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[1])

print()

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])

print()

for lesson in timetable:
  print(lesson)
  
#commonErrors

"""
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[6]}")
"""
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The last color is {colors[5]}")

#fixMyCode

"""
grocery list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print("The first grocery item to buy is {grocery list[1]}.")
"""

groceryList = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print(f"The first grocery item to buy is {groceryList[0]}.")

#Challange

import random

languages = ["merhaba", "hello", "ciao", "salut", "hallo", "hola", "bonjour"]

print(f"{random.choice(languages)}")

#day33

myAgenda = []

def printList():
  print()  #this is just to add an extra space between items
  for item in myAgenda:
    print(item)
  print()  #this is just to add an extra space between items


while True:
    menu = input("add or remove?: ")
    if menu == "add":
        item = input("What's next on the Agenda?: ")
        myAgenda.append(item)
        printList()
    elif menu == "remove":
        item = input("What do you want to remove?: ")
        myAgenda.remove(item)
        printList()

#FixMyCode
        
"""
def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 
while True:
  menu = input("add or remove?: )
  if menu = "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.add(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(list)
    else:
      print("{item} was not in the list)
  printList()
"""

myPartyList = []

def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 
while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.add(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(list)
    else:
      print(f"{item} was not in the list")
  printList()

  #challenge

  ToDoList = []

edit = input("Do you want to view, add, or edit your to-do list? ")

def edit_item(action):
    if action == "view":
        print(ToDoList)
    elif action == "add":
        add_item = input("What do you want to add? ")
        ToDoList.append(add_item)
        print(ToDoList)
    elif action == "edit":
        remove_item = input("What do you want to remove? ")
        ToDoList.remove(remove_item)
        print(ToDoList)
    else:
        print("Unfortunately, that is not an option.")

edit_item(edit)

#day34

import os, time
listOfEmail = []
def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")

#challenge
  
import os
import time

listOfEmail = []


def prettyPrint():
  os.system("clear")
  print("listOfEmail")
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter += 1
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input(
    "1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")

  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu == "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    prettyPrint()
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    for email in listOfEmail:
      print(
        f"Dear {email},\n"
        "It has come to our attention that you're missing out on the amazing Replit 100 days of code. "
        "We insist you do it right away. If you don't, we will pass on your email address to every spammer we've ever encountered "
        "and also sign you up for the My Little Pony newsletter, because that's neat. We might just do that anyway. \n"
        "Love and hugs, \n"
        "Ian Spammington III")
      time.sleep(1)
      os.system("clear")
    break  # Exiting the loop after spamming

  time.sleep(1)
  os.system("clear")