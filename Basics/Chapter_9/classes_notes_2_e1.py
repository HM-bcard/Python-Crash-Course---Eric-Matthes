class Car:
    """a class containing several information about a car"""
    def __init__(self,make,model,year):
        """initializing the car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """creating a combined name of the year make and model"""
        long_name = f"A {self.year} {self.make.title()} {self.model.title()} "
        return long_name
    
    def read_odometer(self):
        """print the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    



car1 = Car('chevy','impala',1999)
print(car1.get_descriptive_name())
car1.read_odometer()


car1.odometer_reading = 166000 # changing the instances value
car1.read_odometer()



# updating an attribute's value through a method:

class Car:
    """a class containing several information about a car"""
    def __init__(self,make,model,year):
        """initializing the car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """creating a combined name of the year make and model"""
        long_name = f"A {self.year} {self.make.title()} {self.model.title()} \n"
        return long_name
    
    def read_odometer(self):
        """print the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it\n")

    def update_odometer(self,mileage): # always 'self'
        """set the odometer to a new value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

        # incrementing a value:
    def increment_odometer(self,miles):
        """adding mileage to the odometer"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
             print("You can't roll back an odometer")


car1 = Car('chevy','impala',1999)
print(car1.get_descriptive_name())
car1.read_odometer()

car1.update_odometer(199000)

car1.increment_odometer(166)


car1 = Car('chevy','impala',1999)
car1.update_odometer(199000)
car1.increment_odometer(-666)
print(car1.get_descriptive_name())
car1.read_odometer()

