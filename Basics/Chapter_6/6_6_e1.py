favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language_poll_names = ['jen','sarah','saul','mike','paul']

for name,language in favorite_languages.items():
    if name in language_poll_names:
        print(f"""Thank You for taking the poll {name.title()}, 
your favorite language seems to be {language}\n""")
    elif name not in language_poll_names:
        print(f"Seems that you haven't taken the poll {name.title()}, please consider " 
"taking it")





