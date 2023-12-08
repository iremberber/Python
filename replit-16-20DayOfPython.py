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