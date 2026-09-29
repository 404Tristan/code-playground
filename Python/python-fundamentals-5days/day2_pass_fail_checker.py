# Day 2: Conditionals (If / Else Statement)
# Task : create "Pass or Fail Checker and Discount Calculator"

from day1_grade_calculator import average
from day1_grade_calculator import age

if average >= 75:
    print("Status: PASSED!")
else:
    print("Status: FAILED!")

#Another Bonus Logic
if age >= 60:
    print("You get a Senior Citizen Discount")
else:
    print("Regular Rate!")

