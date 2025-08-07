class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def increaseAge(self):
        self.age += 1

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."