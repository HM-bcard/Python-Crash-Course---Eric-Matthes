from car import Car
from car import Battery

class ElectricCar(Car,Battery):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize the attributes specific to an electric car
        """
        super().__init__(make, model, year) # super() function calls the 
        # .__init__ method from the parent class
        #self.battery_size = Battery.battery_size
        self.battery = Battery()

    def BatteryUpgrade(self):
        if self.battery.battery_size < 65:
            self.battery.battery_size = 65
        else:
            pass

Cora = ElectricCar('Honda','Cora','2021')

#Cora.battery_size()

Cora.BatteryUpgrade()

print(Cora.battery.battery_size)

Cora.get_range



