#STUDENT REGISTRATION PROGRAM
#Student Attributes (Name, Course, Year, Section)

class Students:
    def __init__(self,name,course,year,section):
        self.name    = name
        self.course  = course
        self.year    = year
        self.section = section

    def introduce(self):
        print(f"     Name          : {self.name}")
        print(f"     Course        : {self.course}")
        print(f"     Year          : {self.year}")
        print(f"     Section       : {self.section}")

answer = input("Submit student information[Y/Any char]? ")
studentList = []

while answer == "Y" or answer == "y":
    name    = input("Name: ")
    course  = input("Course: ")
    year    = input("Year: ")
    section = input("Section: ")

    person  = Students(name,course,year,section)
    studentList.append(person)

    answer = input("You want to submit another student information [Y/Any char]? ")
    print()

number = 1
print()
for x in studentList:
    print(f"Student #{number}")
    x.introduce()                                       #OR studentList[i].introduce()
    number += 1
    print()
