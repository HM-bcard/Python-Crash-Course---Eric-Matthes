class Feline:
    def __init__(self,size,species,fur):
        self.size = size
        self.species = species
        self.fur = fur
    def describe(self):
        print(f"It's a {self.species}")
    def __call__(self, *args, **kwds):
        print(f"Calling the function?")