"""This module only holds the admin class """

from user_class import *
from class_privileges import *

class Admin(User):
    def __init__(self,first_name,last_name,role,created_date,active):
        """ assigning attributes to the parent class"""
        super().__init__(first_name,last_name,role,created_date,active)
        self.privileges = Privileges()
    
    def show_privileges(self):
        self.privileges.show_privileges()
