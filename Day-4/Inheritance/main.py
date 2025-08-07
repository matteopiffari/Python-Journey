from Person import Person
from Student import Student

person1 = Person("John", 30)
student1 = Student("Bob", 20, "S12345")


print(person1.introduce())
print(student1.introduce())
print(f"Student ID: {student1.getStudentID()}")