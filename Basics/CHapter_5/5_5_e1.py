import random

alien_colors = ["green","red","yellow"]
alien_color = random.choice(alien_colors)
print(f"This week's alien's color is {alien_color}")
if alien_color.lower() == 'green':
    print(f"You've just earned 5 points")
elif alien_color.lower() == "yellow":
    print(f"You've just earned 10 points")
elif alien_color.lower() == "red":
    print(f"You've just earned 15 points")


