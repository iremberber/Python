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

