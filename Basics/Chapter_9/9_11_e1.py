from user_class import *
from class_privileges import Privileges
from admin_class import Admin

'''
class Admin(User):
    def __init__(self,first_name,last_name,role,created_date,active):
        """ assigning attributes to the parent class"""
        super().__init__(first_name,last_name,role,created_date,active)
     #   self.privileges = Privileges()
'''
   


Mike = Admin('Mike','Mikovitz','Admin','12-12-1992',True)

Mike.describe_user()

Mike.show_privileges()

#Mike.show_privileges_2()




