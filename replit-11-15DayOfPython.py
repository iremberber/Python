#Day11

print("How many seconds are in a year?")

leap = input("Is this a leap year? Yes or No only.")

if leap == "Yes":
  print(60 * 60 * 24 * 365 * 366)
else:
  print(60 * 60 * 24 * 365 * 365)