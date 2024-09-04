pizzas = ['Buffala',"Margharita","Hawaii","Frutti di Mare"]
for n in pizzas:
  print(f"I like  {n} pizza")
print(f"I like a lot of different pizza")  
  
pizzas.append('Marinara')

friend_pizzas = pizzas[:]

pizzas.append('Carbonara')
friend_pizzas.append('prosciutto')
print(pizzas)
print(friend_pizzas)
