class user:
    def __init__(self,first_name,last_name,username,creation_date,active):
        """initializing attributes to create a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.creation_date = creation_date
        self.active = active

    def describe_user(self):
        if self.active == True:
            print(f"This user's first name is {self.first_name.title()}, surname "
                  f"{self.last_name.title()}, has a username {self.username} "
                  f"created the account on {self.creation_date} "
                  f" and is active")
        else:
            print(f"This user's first name is {self.first_name.title()}, surname "
                  f"{self.last_name.title()}, has a username {self.username}"
                  f"created the account on {self.creation_date} "
                  f" and is inactive")


user_1 = user('mark','markovich','user_1','11-11-2011',True)

user_1.describe_user()