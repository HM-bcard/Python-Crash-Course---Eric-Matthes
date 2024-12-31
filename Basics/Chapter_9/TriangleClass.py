class Triangle:
    def __init__(self,height,base):
        self.height = height
        self.base = base
    def area(self):
        area_1 = self.height*self.base
        print(f"The are of this triangle is {area_1}.")