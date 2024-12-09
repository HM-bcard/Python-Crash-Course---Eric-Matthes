import os

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "pi_digits.txt")

# Open the file
with open(file_path) as file:
    contents = file.read()
    print(contents)
    print(script_dir)