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

