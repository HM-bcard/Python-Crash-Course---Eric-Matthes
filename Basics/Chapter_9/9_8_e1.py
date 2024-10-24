import user_class
import class_privileges

class Admin(user_class.User):
    def __init__(self,first_name,last_name,role,created_date,active):
        """ assigning attributes to the parent class"""
        super().__init__(first_name,last_name,role,created_date,active)
        self.privileges = class_privileges.Privileges()

   


Mike = Admin('Mike','Mikovitz','Admin','12-12-1992',True)

Mike.describe_user()

Mike.privileges.show_privileges()

#Mike.show_privileges_2()



