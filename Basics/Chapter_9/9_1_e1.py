class Restaurant:
    """Method tha print's out restaurant's name and the cuisine they serve"""
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"The {self.name} restaurant serves {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open")



Sambucca = Restaurant('Sambucca','Italian')

Sambucca.describe_restaurant()



