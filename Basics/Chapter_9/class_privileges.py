class Privileges:
    def __init__(self):
        """Just a class to assign privileges"""
        self.privileges = ('Can delete posts','Can ban users','Can add posts')

    def show_privileges(self):
        print(f"This users privileges are :{self.privileges}")

        