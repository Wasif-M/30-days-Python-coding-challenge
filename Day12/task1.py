class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        print(f"{self.name} the {self.species} says 'Hello!'")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Dog", age)

    def bark(self):
        print(f"{self.name} the Dog is barking.")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cat", age)

    def meow(self):
        print(f"{self.name} the Cat is meowing.")

dog = Dog("Bolognese", 3)
cat = Cat("Chartreux", 5)

dog.speak() 
dog.bark()  
cat.speak() 
cat.meow()  
