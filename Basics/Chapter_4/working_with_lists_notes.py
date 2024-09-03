
magicians = ['alice','david','derren']
for magician in magicians:
    print(f"Thank you {magician.title()} for the great performance.") # so it carries on the temporary variable
    print(f"Please give a round of applause to {magician.upper()}\n")
print("Thanks You Everyone for coming".title())

digits = list(range(0,11))
print(min(digits))
print(max(digits))
print(sum(digits))

for i in range (10):
    print(digits[i]**2)
    