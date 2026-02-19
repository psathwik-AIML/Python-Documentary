# class variable: it is placed in the outside of constructors and inside class they are applicable for all class objects 

# instance variable : it is placed in side of constructors and each object have unique values 

class Car:
    # class variable 
    wheels=4

    def __init__(self,name,color):
        self.name=name
        self.color=color

    # method to dispaly output 
    def display_data(self):
        print(f"Car Name is : {self.name}")
        print(f"Car Name is : {self.color}")
        print(f"Car Wheels: {self.wheels}")

# object creation 
car1=Car("Audi","Blue")
car2=Car("Range Rover","Black")

car1.display_data()
car2.display_data()