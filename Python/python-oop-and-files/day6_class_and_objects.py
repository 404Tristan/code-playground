class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = []

    def add_grades(self, grades):
        self.grades.extend(grades)

    def get_average(self):
        if self.grades != []:
            return sum(self.grades)/len(self.grades)
        else:
            return 0.0

    def display_info(self):
        avg = self.get_average()
        avg = (avg if self.grades else "No Grades are given")
        print("----- Student Info -----")
        print(f"ID    : {self.student_id}")
        print(f"Name  : {self.name}")
        print(f"Course: {self.course}")
        print(f"Average Grade: {avg}")
        print("------------------------")

student1 = Student("2026-10001M","Tristan","BS Computer Science")
student1.add_grades([99,90,98,100])
student1.add_grades([99])
student1.display_info()
