usernames = ['admin','bob','bot','mailer','generic']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username} would you like to see logs?")
    elif username != 'admin':
        print(f"Hello {username} have a productive day :)")


