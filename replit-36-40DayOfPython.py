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

