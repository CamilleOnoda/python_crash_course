cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# If-elif-else chain
admission_cost = ("$0", "$25", "$40")
age = 12
if age < 4:
    print(f"Your admission cost is: {admission_cost[0]}.")
elif age < 18:
    print(f"Your admission cost is: {admission_cost[1]}.")
else:
    print(f"Your admission cost is: {admission_cost[2]}.")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is: ${price}.")


#Multiple elif blocks
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
# An extra elif block is sometimes clearer than the general else block
#else:
    #price = 20
print(f"Your admission cost is: ${price}.")
print()

# Test multiple conditions with if statements and no elif or else blocks.
# If we need more than one block of code to run.
requested_toppings =['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("Your pizza is ready!")
print()

requested_toppings = ['mushrooms', 'extra cheese', 'pineapple', 'ham']
for requested_topping in requested_toppings:
    if requested_topping == 'pineapple':
        print("Pineapple? Are you out of your mind?")
    elif requested_topping == 'ham':
        print("Sorry we're out of ham right now.")
    else:
        print(f"Adding {requested_topping}")
print("Your pizza is ready!")