favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

people = ['Billy','Sarah','edward','Laila','Tony']

for person in people:
    if person.lower() in favorite_languages.keys():
        print(f"Hi {person.title()} seems that you have taken the poll and your "
              "favorite language is {favorite_languages[person]} ")
    else:
        print(f"Hi {person.title()} seems you haven't taken the poll, we encourage you" 
              " to.")
