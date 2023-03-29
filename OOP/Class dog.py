class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} the {self.breed} is barking!")


dog1 = Dog("Buddy", "Golden Retriever", 5)
dog2 = Dog("Max", "German Shepherd", 3)

dog1.bark()
dog2.bark()
