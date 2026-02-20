# inheritance : child class will inherit all properties from their parent class 
class Animal:
    alive=True

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")
    

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog=Dog()
dog.bark()

dog.eat()