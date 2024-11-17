prompt = "\nPlease enter a topic you woulkd like to have on your pizza"
prompt += "\nIf you have enterd all the toppings, please input 'quit'"

toppings = input(prompt)
toppings_list = []

while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print(f"We will add {toppings} to your order")
        toppings_list.append(toppings)
    else:
        break

print(toppings_list)

turnip = 0
toppings = input(prompt)
toppings_list = []
while toppings != 'quit' and turnip != 10:
    turnip += 1
    toppings = input(prompt)
    if toppings != 'quit':
        print(f"We will add {toppings} to your order")
        toppings_list.append(toppings)
    else:
        break

print(toppings_list)

