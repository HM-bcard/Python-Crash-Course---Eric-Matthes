cubes = []
for i in range(10):
    cubes.append( i**3)
print(cubes)

print(f"The first three items in this list are {cubes[:3]}")
print(f"The middle four items in this list are {cubes[4:8]}")
print(f"The last three items in the list are: {cubes[-3:]}")

