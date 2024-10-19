import user_class

class Admin(user_class.User):
    def __init__(self,first_name,last_name,role,created_date,active):
        """ assigning attributes to the parent class"""
        super().__init__(first_name,last_name,role,created_date,active)
        self.privileges = ('Can delete posts','Can ban users','Can add posts')

    def show_privileges_1(self):
        """Listing the admin privileges implicitly"""
        return self.privileges
    
    def show_privileges_2(self):
        """Listing admin privileges explicitly"""
        print(f"Mike's privileges are {self.privileges}")


Mike = Admin('Mike','Mikovitz','Admin','12-12-1992',True)

Mike.describe_user()

print(Mike.show_privileges_1())

Mike.show_privileges_2()



