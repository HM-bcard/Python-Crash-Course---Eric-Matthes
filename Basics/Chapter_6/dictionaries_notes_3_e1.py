user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key,value in user_0.items():
    print(f"\nKey : {key}")
    print(f"Value : {value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

for name in sorted(favorite_languages.values()):
    print(f"{name.title()}, thank you for taking the poll")

