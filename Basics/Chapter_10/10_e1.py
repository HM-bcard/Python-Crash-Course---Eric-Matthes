from pathlib import Path

path = Path('learning_python.txt')

#contents = Path.read_text()
#path = Path("pi_digits.txt")
contents = path.read_text()
contents = contents.rstrip()# method chaining
print(contents)
print(contents)

lines = contents.splitlines()
full_text = ''
for line in lines:
    #print(line)
    full_text += line.lstrip()

print(full_text)

