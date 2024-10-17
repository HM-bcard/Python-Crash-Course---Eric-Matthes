class Restaurant:
    """Method tha print's out restaurant's name and the cuisine they serve"""
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def describe_restaurant(self):
        print(f"The {self.name} restaurant sevrves {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open")

    def number_served(self,served):
        if served > self.served:
            self.served = served
        else:
            print("Can't serve negative clients ")

    def increment_number_served(self,new_customers):# call the 'self attribute 
        # errtime
        """increment the number of customers"""
        if new_customers >= 0:
            self.served += new_customers
        else:
            print("Can't serve negative customers")

