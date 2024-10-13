class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")
