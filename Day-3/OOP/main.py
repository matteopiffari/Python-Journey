from Person import Person

def main():
    person1 = Person("Mario", 30)
    print(person1.getName())
    print(person1.getAge())
    person1.increaseAge()
    print(person1.getAge())
    print(person1.introduce())


if __name__ == "__main__":
    main()
