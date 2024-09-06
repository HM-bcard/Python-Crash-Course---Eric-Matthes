import random

age = random.randint(0,99)
print(f"You're {age} years old")
if age < 2:
    print("You're a baby")
elif age >= 2 and age < 4:
    print("you're a toddler")
elif age >= 4 and age < 13:
    print("you're a kid")
elif age >= 13 and age < 20:
    print("you're a teenager")
elif age >= 20 and age < 65:
    print("you're an adult")
elif age >= 65:
    print("you're an elder")
    
     