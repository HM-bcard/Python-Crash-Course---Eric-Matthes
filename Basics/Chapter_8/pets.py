def describe_pet(animal_type = 'harry',pet_name = 'hamster'):
    """Display information about a pet"""
    print(f"I have a {animal_type}")
    print(f"My animal's name is {pet_name.title()}\n")
describe_pet()

describe_pet(pet_name='Madam', animal_type='Molos')

def describe_pet(pet_name,animal_type = 'harry'):
    """Display information about a pet"""
    print(f"I have a {animal_type}")
    print(f"My animal's name is {pet_name.title()}\n")

describe_pet('john')

# equivalent function calls

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"I have a {animal_type}")
    print(f"My animal's name is {pet_name.title()}\n")
#A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet() # should provide arguments

