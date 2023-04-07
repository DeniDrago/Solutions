class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = None

    def __str__(self):
        return f'{self.name}, {self.age}'

    def add_dog(self, dog):
        if isinstance(dog, Dog):
            self.dog = dog
        else:
            raise ValueError("Invalid input. Dog instance is expected.")


class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} the {self.breed} is barking!")


person1 = Person("John", 30, "male")
dog1 = Dog("Fido", "Labrador Retriever", 3)

person1.add_dog(dog1)

person1.dog.bark()
