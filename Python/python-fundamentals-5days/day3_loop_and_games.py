# Day 3: Conditionals (If / Else Statement)
# Task : create "Multiplication Table Generator and Number Guessing Game"

# Multiplication Table
print("Stage 1: Multiplication Table")
number = int(input("Enter a number: "))

for multiply in range(10):
    print(f"{number} * {multiply + 1} = {number * (multiply + 1)}")
print()

# Guess A Number
print("Stage 2: Guess A Number")
target = 7
while True:
    user_num_input = int(input("Input a number: "))
    if user_num_input == target:
        print("You guess it right!!! YEY")
        break

    else:
        print("Wrong Sorry, please try again")
        print()