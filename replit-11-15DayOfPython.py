#Day11

print("How many seconds are in a year?")

leap = input("Is this a leap year? Yes or No only.")

if leap == "Yes":
  print(60 * 60 * 24 * 365 * 366)
else:
  print(60 * 60 * 24 * 365 * 365)

#Day12 FixTheErrors

"""
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?)
ans1 = ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈
ans2 = input("Which lesson number is this?")
if(ans2>12):
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")
"""

print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
ans1 = ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")
ans2 = input("Which lesson number is this?")

if(int(ans2)>12):
  print("We're not quite that far yet")
elif(int(ans2)==12):
  print("That's right!")
else:
  print("We've gone well past that!")

#Day12 Project Day

#Exam

print("q1= Which city is the capital of Turkiye?")
print("a) Ankara b) İstanbul c) Izmir d) Bursa")
a1 = input("")

print("q2= x+5=7 What is x?")
print("a) 2 b) 3 c) 4 d) 5")
a2 = input("")

print("q3= what is the hight of Mount Everest?")
print("a) 8847m b) 8848m c) 8849m d) 8850m")
a3 = input("")

print("q4= x-4=1 What is x?")
print("a) 2 b) 3 c) 4 d) 5")
a4 = input("")

if a1 == "a":
  a1 = 25
else:
  a1 = 0

if a2 == "a":
    a2 = 25
else:
    a2 = 0

if a3 == "c":
  a3 = 25
else:
  a3 = 0

if a4 == "d":
   a4 = 25
else:
    a4 = 0
  
print("You got", a1+a2+a3+a4, "out of 100")

#day14

from getpass import getpass as input

print("You should use 'r' for rock, 'p' for paper, and 's' for scissors. After your move, please press enter.")
player_1 = input("Player 1, what is your move? ")

player_2 = input("Player 2, what is your move? ")

if player_1=="p" and player_2=="s":
    print("player 2 wins")

if player_1=="p" and player_2=="r":
  print("player 1 wins")

if player_1=="s" and player_2=="r":
  print("player 2 wins")

if player_1=="s" and player_2=="p":
  print("player 1 wins")

if player_1=="r" and player_2=="s":
  print("player 1 wins")

if player_1=="r" and player_2=="p":
  print("player 2 wins")

if player_1==player_2:
  print("draw")

#Day15
#loops : Fix the problem

"""counter = 0
while counter < 10:
  print(counter)"""

counter = 0
while counter < 10:
  print(counter)
  counter +=  1

"""counter = 0
while counter >= 12:
  print(counter)
  counter += 1"""

counter = 0
while counter <= 12:
  print(counter)
  counter += 1

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")


