def greet_user():
    """Display a simple greeting""" # a docstring - used to document functions
    print("Hello User")
greet_user()

def square(a):
    print(a*a)

square(2)

def greet_user(username):
    """Display a simple greeting""" # a docstring - used to document functions
    print(f"Hello {username.title()}")
greet_user('mike')

