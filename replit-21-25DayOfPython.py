#Day21 Project Day
counter = 0

for i in range(11):
    answer = input(str(i) + " x 7 = ")
    correct_answer = i*7
    if answer == str(i * 7):
        print("Correct!")
        counter += 1
    else:
      print("That's not correct. It should have been",correct_answer)
      continue

print("You got " + str(counter) + " out of 10 questions correct.")

