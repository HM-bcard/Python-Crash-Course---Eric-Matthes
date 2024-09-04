players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:])

# looping thropugh a slice

for player in players[:3]:
    print(f"{player.title()} is a top player in my team!")



my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannolli')

print(my_foods)
print(friend_foods)
friend_foods.pop()

print(my_foods)
print(friend_foods)

# so if you alter the second list you alter the first



