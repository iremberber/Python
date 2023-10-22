#Day6

print("SECURE LOGIN")
username = input("Username > ")
password = input("Password > ")

if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "irem" and password == "iremirem":
  print("Welcome master!")
else:
  print("Go away!")

#day7

order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")

#task7

print("Fake Fan Finder")

q1 = input("Are you a Swiftie?")

if q1 == "yes":
    q2 = input("What is your favorite song?")
    if q2 == "IDK":
        print("You are not a fan!")
    else:
        print("You are a fan!")
else:
  print("That's fine")

#day8 Project Day

name = input("What is your name? ")
age = input("How old are you? ")
job = input("What is your dream job? ")
hope = input("You think you can achieve this? Rate 1-10 ")

if int(age) <= 20 and int(hope) > 5 :
  print("Hi" , name , "! It's nice to see you. I know, you wanna be a" , job , "and with this confident, I'm pritty sure that you can. Don't Give Up!")
  
elif int(age) > 20 and int(hope) > 5 :
  print("Hi" , name , "! It's nice to see you. I know, you wanna be a" , job , " You know that it's never to late! You can be whatever you want!")

elif int(age) <= 20 and int(hope) < 5 :
  print("Hi" , name , "! It's nice to see you. I know, you wanna be a" , job , " You are so young! Why are you so hopeless? You can be whatever you want! Just do it!")

else:
  print("Hi" , name , "! It's nice to see you. I know, you wanna be a" , job , "and I know, you are hopeless but want you to know, it's not too late. You can be whatever you want! Just keep pushing!")

#day9

myScore = input("Your score: ")
if int(myScore) > 100000:
  print("Winner!")
else:
  print("Try again 😭")

myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")

#task

birthyear = int(input("Enter your birth year: "))

if 1925 < birthyear <1946:
    print("You are a Traditionalist")
elif 1947 < birthyear < 1964:
    print("You are a Baby Boomer")
elif 1965 < birthyear < 1981:
    print("You are a Generation X")
elif 1982 < birthyear < 1995:
    print("You are a Millennial")
elif 1995 < birthyear < 2011:
    print("You are a Generation Z")
else:
    print("You are a Generation Alpha")

#day10

adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)

#task

bill = input("What was the bill?")
tip = input("What percentage would you like to tip?")
total = int(bill) * (1 + (int(tip) / 100) )
numberOfPeople = int(input("How many people?: "))
answer = total / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)


