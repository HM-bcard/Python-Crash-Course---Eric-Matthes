sandwich_orders = ['ruby','tuna','pastrami','chicken','hamburger','ham&cheese','pastrami'
                   ,'pastrami','ham & mayo']
print('The deli has run out of pastrami, we apologize')
while 'pastrami' in sandwich_orders:
    print(f"We're sorry, we don't have pastrami")
    sandwich_orders.remove('pastrami')
finished_sandwiches = []


while sandwich_orders:

    sandwich_made = sandwich_orders.pop()
    print(f"I made you a {sandwich_made} sandwich")
    finished_sandwiches.append(sandwich_made)
for sandwich in finished_sandwiches:
    print(f"{sandwich} has been made")

