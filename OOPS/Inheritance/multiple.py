class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def talents(self):
        print("Mother: Painting")

class Child(Father, Mother):
    def hobby(self):
        print("Child: Playing")

c = Child()

c.skills()
c.talents()
c.hobby()