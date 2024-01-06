#day36 

#String Manipulation

name = input("What's your name? ")
if name.lower().strip() == "irem":
  print("Hello İrem!")
else: 
  print("Hello stranger!")

#No Duplicates

myList = []
def printList():
  print()
  for i in myList:
    print(i)
  print()
while True:
  addItem = input("Item > ").lower().strip()
  if addItem not in myList:
    myList.append(addItem) 
  printList()

#common errors
"""
myList = []

def printList():
 print()
 for i in myList:
   print(i)
 print()

while True:
 addItem = input("Item > ").capitalize().strip()
 if addItem not in myList:
   myList.append(addItem)
 printList()
"""

myList = []

def printList():
 print()
 for i in myList:
   print(i)
 print()

while True:
 addItem = input("Item > ").strip().capitalize()
 if addItem not in myList:
   myList.append(addItem)
 printList()

#challenge
 
 listOfNames= []

def printList():
  print()
  for name in listOfNames:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in listOfNames:
    listOfNames.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()

#Day 37

myString = "Hello there my friend."
print(myString[0])
print(myString[6:11])
print(myString[:11])
print(myString[11:])

#The Secret Third Argument

myString = "Hello there my friend."
print(myString[0:4:2])
print(myString[::3])
print(myString[::-1])

#split

myString = "Hello there my friend."
print(myString.split())

#Common Errors
"""
Why is it printing 'Hell' instead of 'Hello'?

myString = "Hello there my friend."
print(myString[0:4])
"""

myString = "Hello there my friend."
print(myString[0:5])

"""
myString = "Hello there my friend."
print(myString[0:4:0])
"""

myString = "Hello there my friend."
print(myString[0:4:1])

#fix my code

"""
# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[0:10:0])
"""

myString = "Hello there my friend."
print(myString[0:11:1])

#challenge

print("Lets find your stage name!")

name= input("What's your real name?")
color = input("What's your favourite colour?")
animal= input("what's your favourite animal?")

stagename = name[0:3] + color[0:3] + animal[2:]

print("Your stage name is ", stagename)