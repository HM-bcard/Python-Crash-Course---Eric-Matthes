provide_a_number = int(input("please provide a number in digits here: "))

if provide_a_number % 10 == 0:
    print(f"{provide_a_number} is divisible by 10")
else:
    print(f"{provide_a_number} is not divisible by 10")

