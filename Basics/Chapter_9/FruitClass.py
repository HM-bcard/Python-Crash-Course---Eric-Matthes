import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area_calc = (self.radius*2*math.pi)
        print(f'This circle has an area of {area_calc}')

circle_one = Circle(2)

circle_one.area()

