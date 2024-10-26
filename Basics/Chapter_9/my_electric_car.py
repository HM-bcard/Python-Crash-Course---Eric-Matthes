from car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.describe_battery() # calling the battery attribute and 
# describe function 
my_leaf.battery.get_range()
print(my_leaf.get_descriptive_name())