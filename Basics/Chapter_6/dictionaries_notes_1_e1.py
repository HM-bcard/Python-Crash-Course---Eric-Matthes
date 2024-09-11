'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(alien_0['x_position'])
print(alien_0)
'''

alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
for value in alien_0:
    print(alien_0[value])

alien_0['color'] = 'yellow'

for key in alien_0:
    print(f"the value for key '{key}' is '{alien_0[key]}'")

    

          

