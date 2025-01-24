class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe(self):
        print(f"This restaurant is called {self.name} and it serves" 
              f" {self.cuisine} cuisine")
        