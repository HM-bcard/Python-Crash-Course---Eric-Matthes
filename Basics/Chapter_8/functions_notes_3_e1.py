def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# return values

def build_person(first_name,last_name,age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last':last_name, }
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',69)
print(musician)


