class Restaurant:
    def __init__(self,name,cuisine,number_served = 0):
        self.name = name
        self.cuisine = cuisine
        self.number_served = number_served
    def describe(self):
        print(f"This restaurant is called {self.name} and it serves" 
              f" {self.cuisine} cuisine")
    def customers_served(self):
        print(f" The restaurant served {self.number_served} customers")



restaurant = Restaurant('Cevapici','Greek',10)
restaurant.customers_served()

