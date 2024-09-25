sandwich_orders = ['ruby','tuna','chicken','hamburger','ham&cheese']
finished_sandwiches = []
while sandwich_orders:
    sandwich_made = sandwich_orders.pop()
    print(f"I made you a {sandwich_made} sandwich")
    finished_sandwiches.append(sandwich_made)
for sandwich in finished_sandwiches:
    print(f"{sandwich} has been made")
