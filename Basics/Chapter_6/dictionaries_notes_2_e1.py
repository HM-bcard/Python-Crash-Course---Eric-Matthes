alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


print(alien_0)

del alien_0['x_position']
print(alien_0)
# deletion is permanent



list_1 = [1,2,3]
list_2 = list_1

del list_2[0]

print(list_1)
print(list_2)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print(favorite_languages)
'''
favorite_languages + {
    'value1':'key1',
    'value2': 'key2',
    'value3': 'key3'
}
'''
print(f"Sarah's favourite language is {favorite_languages['sarah']}")

#print(alien_0['points'])

# How to check if there's an empty key/value:
point_value = alien_0.get('points', 'No value assigned')

print(point_value)




