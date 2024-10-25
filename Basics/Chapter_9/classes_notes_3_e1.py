# Inheritance

#  electric car example of inheritance:

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:   
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# inheriting class :

class Battery:
    """Subclass to represent the battery in the ElectriCar class"""
    def __init__(self,battery_size=40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print battery size description"""
        print(f"This car has a {self.battery_size} kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize the attributes specific to an electric car
        """
        super().__init__(make, model, year) # super() function calls the 
        # .__init__ method from the parent class
        self.battery_size = 40
        self.battery = Battery()
        
        '''
    def describe_battery(self):
        """Print battery size description"""
        print(
        f"The {self.make.title()} {self.model.title()} has a "
        f"{self.battery_size}"  
        f"Ah battery" 
    )'''
        



 



my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.describe_battery() # calling the battery attribute and 
# describe function 
my_leaf.battery.get_range()
print(my_leaf.get_descriptive_name())

