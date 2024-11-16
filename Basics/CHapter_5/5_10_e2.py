current_users = ['Mike','Bob','Elvira','Billy','Cat']

new_users = ['Leyla','Bob','Honcho','Cat','Mark']


for user in current_users:
    if user in new_users:
        print('This username is taken, please enter a new username')
    else:
        print('Username available')

