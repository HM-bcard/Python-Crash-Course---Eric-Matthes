from pathlib import Path
import os
print(os.getcwd())

path = Path("pi_digits.txt")
contents = path.read_text()
contents = contents.rstrip()# method chaining
print(contents)

lines = contents.splitlines()
pi_string = ''
for line in lines:
    #print(line)
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

pi_float = float(pi_string)

for i in pi_string:
    if i == 1:
        print(int(i))
    else:
        continue


path = Path('programming.txt')
path.write_text("I love programming")

