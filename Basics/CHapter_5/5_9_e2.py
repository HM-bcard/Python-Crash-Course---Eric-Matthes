usernames = ['admin','bob','bot','mailer','generic']
if usernames == []:
    print("We need more users")

else:    
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()} would you like to see logs?")
        elif username != 'admin':
            print(f"Hello {username.title()} have a productive day :)")


usernames = []
if usernames == []:
    print("We need more users")

else:    
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username} would you like to see logs?")
        elif username != 'admin':
            print(f"Hello {username} have a productive day :)")