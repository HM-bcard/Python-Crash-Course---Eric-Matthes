class Cat:

    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def sit(self):
        """simulating a cat ignoring the owner"""
        print(f"{self.name} ignored you")

