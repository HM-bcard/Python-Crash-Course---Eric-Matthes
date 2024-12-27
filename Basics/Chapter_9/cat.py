from random import *

class cat:
    def __init__(self,name,age):
        """initialize the cat attributes"""
        coat_colors = choice(['black','white','grey','orange'])
        self.name = name
        self.coat = coat_colors

    
    def coats(self):
        print(f"My cat has a {self.coat} coat")

