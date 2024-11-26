from pathlib import Path
import os
print(os.getcwd())

path = Path("pi_digits.txt")
contents = path.read_text()
contents = contents.rstrip()# method chaining
print(contents)

