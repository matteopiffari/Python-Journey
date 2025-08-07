# -----------------------------------
#            Inheritance
# -----------------------------------
from Person import Person

class Student(Person):
    # You can use the "pass" keyword if you don't want to implement any additional methods or properties.

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def getStudentID(self):
        return self.student_id

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}."