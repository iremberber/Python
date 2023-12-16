#Day21 Project Day
counter = 0

for i in range(11):
    answer = input(str(i) + " x 7 = ")
    correct_answer = i*7
    if answer == str(i * 7):
        print("Correct!")
        counter += 1
    else:
      print("That's not correct. It should have been",correct_answer)
      continue

print("You got " + str(counter) + " out of 10 questions correct.")

#Day22 Libraries

import random

print("Totally Random One-Million-to-One")

correct_number = random.randint(1, 1000000)
attempt = 1 

while True:
    user_guess = int(input("Pick a number between 1 and 1,000,000: "))

    if user_guess < 0:
        print("Now we'll never know what the answer is …")
        exit()
    elif user_guess < correct_number:
        print("That number is too low. Try again!")
        attempt += 1
    elif user_guess > correct_number:
        print("That number is too high. Try again!")
        attempt += 1
    elif user_guess == correct_number:
        print("You are a winner! 🥳🥳")
        print("It took you", attempt, "attempt(s) to get the correct answer.")
        break
    else:
        print("That is not a number I recognize.")

#Day23

def rollDice():
  import random
  dice = random.randint(1,6)
  print("you rolled", dice)

for i in range(100):
  rollDice()

#Common Errors

"""
def print My Name():
  print("My Name is David")
  
print My Name()
"""
def printMyName():
  print("My Name is Mary")
  
printMyName()

"""
def countToFive:
  for i in range(1, 6):
    print(i)
    
countToFive()
"""

def countToFive():
  for i in range(1, 6):
    print(i)
  
countToFive()

#Challenge

def login():
    while True:
      username = input("Enter username: ")
      password = input("Enter password: ")
      if username == "Mary" and password == "6161":
        print("Welcome David")
        break
      else:
        print("That is not the correct username or password. Try again!")
        continue
    
print("REPLIT LOGIN SYSTEM")
login()

#day24

def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")
  
userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")

whichCake(userIngredient, userBase, userCoating)

#commonError

"""
def biggerNumber(number1 number2):
  if(number1 > number2):
    print(number 1, "is bigger")
  else:
    print(number 2, "is bigger")
biggerNumber (18,332)
"""

def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  else:
    print(number2, "is bigger")
biggerNumber (18,332)

#FixMyCodePart

"""
def pizza_order(topping1 topping2):
  if topping1 = "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than" topping1)

topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")
  pizza_order(topping1, topping2)
"""

def pizza_order(topping1, topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than", topping1)

topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")
pizza_order(topping1, topping2)

#challenge

import random
side = int(input("How many sides does your dice have?"))
game = "yes" or "Yes"

def rollDice(side):
   print("You rolled", random.randint(1, side))
  
while game == "yes" or game == "Yes":
  rollDice(side)
  game = input("Roll again?")

rollDice(side)

#day25

#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin

myPin = pinPicker(4) #4 means we want 4 random numbers

print(myPin)

#CommonErrors
"""
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
areaOfTriangle (5, 22)
"""
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
myArea = areaOfTriangle (5, 22)
print(myArea)

"""
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
areaOfTriangle (5, 22)
print(area)
"""

def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
area=areaOfTriangle (5, 22)
print(area)

#fixMyCode

"""
def area_square(side1 side2):
  area = side1 * side2
  return area_square
area_square(4, 12)
print(area)
"""

def area_square(side1, side2):
  area = side1 * side2
  return area
area = area_square(4, 12)
print(area)

#Challenge

import random

def roll_dice(dice1,dice2):
  healt = dice1*dice2
  return healt
healt = roll_dice(random.randint(1,6),random.randint(1,8))
  

name = input("What is your character's name?")
print(name + "'s healt is " + str(healt)+ "ph")
