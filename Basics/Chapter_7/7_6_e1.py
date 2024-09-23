not_done = True

while not_done:
    age = (f"Please provide your age in numbers here:")
    age += (f" \nInput 'quit' when you're done ")
    age = input(age)


    if age == 'quit':
        not_done = False
    elif 3 <= int(age) < 12 :
        print(f"The ticket costs 10$ for people between 3 and 12")
    elif int(age) > 12:
        print(f"The regular ticket costs 15$")
    elif int(age) < 3:
        print(f"The ticket is free for people under {age} years old")

