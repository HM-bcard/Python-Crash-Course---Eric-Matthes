
while True:
    try:
        numer_one = int(input("Please provide a number here:"))
        number_two = int(input("Please provide a second number here:"))
    except ValueError:
        print("Please provide a numerical value")
    else:
        print(numer_one+number_two)

