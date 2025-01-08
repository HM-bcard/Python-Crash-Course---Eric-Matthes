class Canid:
    def __init__(self,size,paws,tail,fur):
        self.size = size
        self.paws = paws
        self.tail = tail
        self.fur = fur
    def describe(self):
        print(f"This canid is {self.size} has {self.paws} paws a {self.tail} tail"
              f" and a {self.fur} coat.")
        
