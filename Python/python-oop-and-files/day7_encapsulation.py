class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__grades = []

    def add_grades(self, grades):
        for grade in grades:
           if 0 <= grade <= 100:
                self.__grades.append(grade)
                print(f"Successfully added grade: {grade}")
           else:
               print(f"Invalid grade: {grade}. Must be between 0 to 100")

    def get_grades(self):
        return self.__grades

    def get_average(self):
        return (sum(self.__grades)/len(self.__grades) if self.__grades else 0.0)

    def display_info(self):
        avg = (round(self.get_average(),2) if self.__grades else "No Grades are given")

        print("----- Student Info -----")
        print(f"ID    : {self.student_id}")
        print(f"Name  : {self.name}")
        print(f"Course: {self.course}")
        print(f"Current Valid Grades: {self.get_grades()}")
        print(f"Average Grade: {avg}")
        print("------------------------")

student1 = Student("2026-10001M","Tristan","BS Computer Science")
student1.add_grades([90, 90, 101, 90])
student1.display_info()
