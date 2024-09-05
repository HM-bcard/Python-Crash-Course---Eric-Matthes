number = 'Thirteen'
print("Is number == 'thirteen' I predict yes.")
if number.lower() == 'thirteen':
    print('Yes')

print("Is number != 'fourteen' I predict yes.")
if number.lower() != 'fourteen':
    print('yes')




numbers = ['fourteen','fifteen','sixteen','seventeen','eighteen','nineteen', 
           'twenty']

for number in numbers:
    if number.title() == 'Seventeen':
        print(17)
    else:
        print(number)

numbers_1 = [14,15,16,17,18,19,20]

for number_1 in numbers_1:
    for number in numbers:
        if (len(number) > number_1 or len(number) == number_1):
            print("It's higher or equal")
        else:
            print("It's lower")


if number in numbers:
    print("It's a numbers game")

    