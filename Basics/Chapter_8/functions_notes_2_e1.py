def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}")
    print(f"My animal's name is { pet_name.title()}\n")
describe_pet('hamster','harry')
describe_pet('harry','hamster')


def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {pet_name}")
    print(f"My animal's name is {animal_type.title()}\n")

describe_pet('hamster','harry')
describe_pet('harry','hamster')


# So the position is realted to the actual function mechanics, 
# not the posisiton itself

# Multiple fiunction calls:

describe_pet('molly','molusk')

describe_pet('sean','sheep')


