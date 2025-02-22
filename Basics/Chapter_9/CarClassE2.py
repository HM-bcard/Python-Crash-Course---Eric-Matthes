class Car:
    """ a docstring - remember to docstring"""
    def __init__(self,make,model,year):
        """ more docstrings"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Show the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        """ a condition to not allow the rollback of the odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer")
    def increment_odometer(self,miles):
        """adding some miles to the odometer"""
        self.odometer_reading += miles
    
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 27
my_new_car.read_odometer()

my_new_car.update_odometer(-20000)
my_new_car.read_odometer()
my_new_car.update_odometer(51000)
my_new_car.read_odometer()
my_new_car.increment_odometer(-200)

my_new_car.read_odometer()

