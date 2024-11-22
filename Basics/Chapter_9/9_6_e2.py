from restaurant_class import Restaurant



class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine): 
        """Initializing the restaurant class"""
        super().__init__(name,cuisine)
        self.flavors = ('chocolate','vanilla','pistacchio','cream')

    def show_flavors(self):
        print(self.flavors)

Uncle_Micks = IceCreamStand('Uncle Micks','Gelato')

Uncle_Micks.show_flavors()

Uncle_Micks.describe_restaurant()


