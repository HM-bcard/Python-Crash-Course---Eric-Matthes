class Hexagon:
    def __init__(self,side):
        self.side = side
        pass
    def calculate_perimeter(self):
        perimeter = self.side*6
        print(f"The perimeter is {perimeter}")

    def calculate_area(self):
        area =  3/2 *3**1/2*self.side**2
        print(f"This hexagon area is {area}")



first_hexagon = Hexagon(6)

first_hexagon.calculate_perimeter()

first_hexagon.calculate_area()