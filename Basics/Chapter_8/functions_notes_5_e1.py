# passing an arbitrary number of arguments

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size,*toppings):
    """blablabla"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','cream','red onions','guanciale')

'''
In the function definition, Python assigns the first value it receives to
the parameter size. All other values that come after are stored in the tuple
toppings.

generic parameter name often seen: *args

'''

def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# Storing your functions in modules

