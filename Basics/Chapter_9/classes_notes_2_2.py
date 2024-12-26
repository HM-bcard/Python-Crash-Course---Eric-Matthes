class Dog:
    def __init__(self,name,breed):
        """initializing variable attributes"""
        self.name = name
        self.breed = breed

    def sit(self):
        """Simulate a sitting dog after a command"""
        print(f"{self.name} has sat.")
    
    def roll_over(self):
        """simulating a dog rolling over"""
        print(f"{self.name} is rolling over")
