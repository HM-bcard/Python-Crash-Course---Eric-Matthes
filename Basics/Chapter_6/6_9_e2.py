favorite_places = {'Bob':['Burger joint','Kebab','Pizzeria'],
                  'Tony':['Bada bing','Satriales','Jersey'],
                  'Charles':['Mansion']}

for person in favorite_places:
    for place in favorite_places[person]:
        print(f"{person}s favorite place is {place}")


favorite_places = {
    'Bob': ['Burger joint', 'Kebab', 'Pizzeria'],
    'Tony': ['Bada bing', 'Satriales', 'Jersey'],
    'Charles': 'Mansion'
}

for person in favorite_places:
    places = favorite_places[person]
    # Ensure the value is treated as a list
    if isinstance(places, str):
        places = [places]
    for place in places:
        print(f"{person}'s favorite place is {place}")


list_new = ['a','b','c','d']

for letter in list_new:
    favorite_places[letter] = 'null'

print(favorite_places)