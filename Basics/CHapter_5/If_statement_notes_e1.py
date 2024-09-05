cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#evaluation:
car == car # checks whether the value is true ( the same in this case)

# comparison without affecting the variable - temporary conversion:

car = 'Audi'
print(car.lower() == 'audi')

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # doesn't equal
    print("Hold the anchovies!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
#False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
#True

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a \
response if you wish.")


long_string = (
    "This is a very long string "
    "that can be split over multiple lines "
    "and will be concatenated automatically."
)
print(long_string)

