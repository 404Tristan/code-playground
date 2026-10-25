class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self.__grades = []

    def add_grades(self, grades):
        for grade in grades:
           if 0 <= grade <= 100:
                self.__grades.append(grade)
                print(f"Successfully added grade: {grade}")
           else:
               print(f"Invalid grade: {grade}. Must be between 0 to 100")

    def get_average(self):
        return (sum(self.__grades)/len(self.__grades) if self.__grades else 0.0)

    def get_details(self):
        avg = (round(self.get_average(), 2) if self.__grades else "No Grades are given")
        return f"""
        ------ Student Information ------
        Name: {self.name}
        Age : {self.age}
        ID  : {self.student_id}
        Course: {self.course}
        Average: {avg}
        ---------------------------------"""

class Teacher(Person):
    def __init__(self, name, age, employee_id, subject_taught):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject_taught = subject_taught

    def get_details(self):
        return f"""
        ------ Teacher Information ------
        Name: {self.name}
        Teacher ID: {self.employee_id}
        Subject   : {self.subject_taught}
        ---------------------------------"""


student = Student("Tristan", 10, "2026-10001M", "BSCS")
student.add_grades([90, 90, 101, 90])
teacher = Teacher("Dwein", 30, "094-374M", "OPERSYS")

people = [student, teacher]

for person in people:
    print(person.get_details())
