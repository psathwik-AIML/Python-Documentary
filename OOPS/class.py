class Car:
    name="audi"
    color="black"

    def __init__(self,n,c):
        self.name=n
        self.color=c

    def display_car_data(self):
        print(f"car name is : {self.name}")
        print(f"car color is : {self.color}")

car1=Car("swift","grey")
car2=Car("bmw","red")
car1.display_car_data()
car2.display_car_data()