from pathlib import Path 

path = Path('users_name.txt')

users_name = input("Hi, what's your name?")
path.write_text(users_name)


