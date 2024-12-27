class Ferret:
    def __init__(self,name,age,coat):
        self.name = name
        self.age = age
        self.coat = coat
    def describe(self):
        print(f"My ferret is {self.age} it has a {self.coat} coat and is called "
              f"{self.name}")