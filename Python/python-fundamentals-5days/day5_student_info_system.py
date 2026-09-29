# Day 5: Mini-Project
# Task : Create "Simple Student Information Console App"
students_list = []
current_student = 10000
year = 2025

def add_student(students,counter):

    counter += 1
    name   = input("Enter a name: ").lower()
    grade  = input("Enter grade : ")
    gender = input("Enter gender: ").upper()
    print()

    student_data = {
        "id": f'{year}-{counter}'+gender[0],
        "name": name,
        "grade": grade
    }
    students.append(student_data)
    return counter

while True:
    print("1. Add Student Record")
    print("2. View All Students")
    print("3. Exit")
    print()

    user_mini_input = input("Enter your choice number: ")
    if user_mini_input == "1":
        current_student = add_student(students_list,current_student)

    elif user_mini_input == "2":
        for student in students_list:
            print(f"Student ID: {student["id"]}")
            print(f" - Name : {student["name"]}")
            print(f" - Grade: {student["grade"]}")
        print()

    elif user_mini_input == "3":
        print("Bye, see u again :)")
        break
    else:
        print("Invalid choice")