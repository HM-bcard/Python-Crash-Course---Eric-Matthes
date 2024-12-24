class Furniture:
    def __init__(self,type,name,legs,cover,material):
        self.legs = legs
        self.cover = cover
        self.material = material
        self.type = type
    def describe_furniture(self):
        print(f"This furniture is a{self.type}")