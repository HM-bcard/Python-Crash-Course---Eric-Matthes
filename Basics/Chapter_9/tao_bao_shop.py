from restaurant_class import Restaurant

class TaoBaoShop(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.menu = ['Fried dumplings','taobao']
    def print_menu(self):
        print(f"The first item on the menu is {self.menu[0]}, "
              f" the second item on the menu is {self.menu[1]}")
        
WonTonSHop = TaoBaoShop('WonTonSHop Hsiuhs','Cantonese')

WonTonSHop.print_menu()

WonTonSHop.describe_restaurant()

