while True:
    first_number = int(input("First number:"))
    second_number = int(input("Second number"))
    try:
        print(f"Your answer is {first_number/second_number}")
    except ZeroDivisionError:
        print("You can't divide by zero")