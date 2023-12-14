#Day16

print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()
counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss":
    break
print("Thanks for playing!")
print("You got the correct lyrics in", counter, "attempt(s).")

#day17
from getpass import getpass as input

counter1 = 0
counter2 = 0
while True:

  print("You should use 'r' for rock, 'p' for paper, and 's' for scissors. After your move, please press enter.")
  player_1 = input("Player 1, what is your move? ")

  player_2 = input("Player 2, what is your move? ")

  if player_1=="p" and player_2=="s":
    print("player 2 wins")
    counter2 +=1

  if player_1=="p" and player_2=="r":
    print("player 1 wins")
    counter1 +=1

  if player_1=="s" and player_2=="r":
    print("player 2 wins")
    counter2 +=1

  if player_1=="s" and player_2=="p":
    print("player 1 wins")
  counter1 +=1

  if player_1=="r" and player_2=="s":
    print("player 1 wins")
    counter1 +=1

  if player_1=="r" and player_2=="p":
    print("player2 2 wins")
    counter2 +=1

  if player_1==player_2:
    print("draw")

  if counter1==3 or counter2==3:
    print("game over")
    break

  #Day 18

print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")
correct_number = 2300
attempt = 1
while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You are a winner! 🥳🥳")
    break 
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")

#day19
loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))

#Day20
for i in range(100,110):
  print(i)

print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)

for i in range (0, 1000000, 25):
  print(i)

for i in range(10, -1, -1):
  print(i)

for i in range (10, 0, -1):
  print(i)

#fix the code

#while i in range (20, 40, -1):
  #print(i)

for i in range (40, 20, -1):
  print(i)

#day 20 challenge

start = input("Enter a starting number: ")
ending = input("Enter an ending number: ")
increment = input("Enter an increment: ")

for i in range(int(start), int(ending) + 1, int(increment)):
  print(i)

