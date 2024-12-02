from pathlib import Path

path = Path('users_list.txt')

users_list = ''
users_name = ''
while users_name != 'quit':
    users_name = input('Please enter your name here, input "quit" to quit: \n')
    if users_name != 'quit':
        users_list += users_name+'\n'
    else:
        continue

path.write_text(users_list)

