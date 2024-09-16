dog = {'species':'dog', 'legs':4, 'fur':'black', 'owner':'John'}
cat = {'species':'cat', 'legs':'4', 'fur': 'brown', 'owner':'Mike'}
parrot = {'species':'bird', 'legs':2,'fur':'none','owner':'Saul'}

pets = [dog,cat,parrot]

for pet in pets:
    print(f"This pet's species is {pet['species']},it has {pet['legs']} "
          f"it has {pet['fur']} coloured fur and it's owner is {pet['owner']}")
