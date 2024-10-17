import restaurant_class

restaurant = restaurant_class.Restaurant('Ikigai','Japanese')
print (restaurant.served)

# incrementing manually
restaurant.served = 7
print(restaurant.served)

restaurant.number_served(666)
print(restaurant.served)

restaurant.increment_number_served(666)
print(restaurant.served)

