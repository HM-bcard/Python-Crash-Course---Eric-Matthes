try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

print("Give me two numbers, i'll divide them.")
print("Enter 'q' to quit")

try:

    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        answer = int(first_number) / int(second_number)
        print(answer)
except ZeroDivisionError:
    print('Provide a number other than 0 as the denominator')



while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print('Provide a number other than 0 as the denominator')
        print(answer)