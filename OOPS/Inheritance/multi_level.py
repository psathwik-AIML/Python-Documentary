class Animal:
    def sleep(self):
        print("Animal is sleeping")
    
class Dog(Animal):
    def bark(self):
        print("it can bark")
class Puppy(Dog):
    def details(self):
        print("iam small")


pup=Puppy()
pup.details()
pup.sleep()
pup.bark()