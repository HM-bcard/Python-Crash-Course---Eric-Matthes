from pathlib import Path

path = Path("cats.txt")
cats = ''

cats += 'sparky \n'
cats += 'mellow \n'
cats += 'blacko \n'

path.write_text(cats)


path1 = Path("dogs.txt")
dogs = ''

dogs += 'Woofred \n'
dogs += 'Buster \n'
dogs += 'Morrow \n'

path1.write_text(dogs)

