# Day 1: Variables, Input/Output & Data Types
# Task : create "Grade Average Calculator"

name =     input("Enter your name: ")
age  = int(input("Enter your age : "))
print()
grade_softeng = float(input("Enter your in SoftEng: "))
grade_os      = float(input("Enter your in OS     : "))
grade_algo    = float(input("Enter your in Algo   : "))

average = round(((grade_softeng + grade_os + grade_algo)/3), 2)
print(f"Hello {name}, your average grade is {average}")

