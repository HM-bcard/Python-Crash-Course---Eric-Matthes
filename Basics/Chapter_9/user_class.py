class User:
    """A class for automatically assigning typical profile data to a 
    user"""
    def __init__(self,first_name,last_name,role,created_date,active):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.created = created_date
        self.active = active
 
    def describe_user(self):#remember to pass the 'self'
        if self.active == True:
            print(f"Hello {self.first_name} {self.last_name}")
            print(f"It seems that you have been assigned the role of an "
                f"{self.role} and created Your account on {self.created}")
            print(f"Your account seems to be active\n")
        else:
            print(f"Hello {self.first_name} {self.last_name}")
            print(f"It seems that you have been assigned the role of an "
                f"{self.role} and created Your account on {self.created}")
            print(f"Your account seems to be inactive\n")
        

        