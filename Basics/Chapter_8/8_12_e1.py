# sanwiches

def sandwiches(*ingredients):
    print(f"You want a sandwich with these ingredients:")
    for ingredient in ingredients:
        print(f"-{ingredient}")

sandwiches('mayo','lettuce','ham','pepperoni')

sandwiches('sausage','cheese','relish')

sandwiches('plain')
