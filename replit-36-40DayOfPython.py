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
