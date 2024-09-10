current_users = ['Kool_aid','KREE','mike77','bob','bothy','mailer1','generic']

new_users = ['godot','kree','shosho','mikey_mike','kool_aid']

for new_user in new_users:
    if new_user in current_users:
        print(f"""The username{new_user} is taken, please select a different 
              username""")
    elif new_user not in current_users:
        print(f"The username {new_user} is available")


for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() != current_user.lower():            
            print(f"""The username{new_user} is taken, please select a 
                  different username""")
        elif new_user.lower() == current_user.lower():
            print(f"The username {new_user} is available")

new_users = ["john", "Alice", "BOB"]
current_users = ["alice", "bob", "charlie"]

for new_user in new_users:
    # Flag to check if username is taken
    username_taken = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            username_taken = True
            break  # Stop checking further once a match is found

    if username_taken:
        print(f"The username {new_user} is taken, please select a different username.")
    else:
        print(f"The username {new_user} is available.")