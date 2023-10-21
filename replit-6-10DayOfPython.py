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


