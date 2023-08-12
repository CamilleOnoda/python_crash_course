alien_color = 'green'
if alien_color == 'green':
    print("You won 5 points!")
elif alien_color == 'yellow':
    print("You won 10 points!")
else:
    print("You won 15 points!")


alien_color = 'red'
if alien_color == 'green':
    print("You won 5 points!")
elif alien_color == 'yellow':
    print("You won 10 points!")
else:
    print("You won 15 points!")


alien_color = 'yellow'
if alien_color == 'green':
    print("You won 5 points!")
elif alien_color == 'yellow':
    print("You won 10 points!")
else:
    print("You won 15 points!")
print()


age = 1
if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")


favorite_fruits = ['banana', 'apple', 'kiwi']
for favorite_fruit in favorite_fruits:
    if favorite_fruit == 'banana':
        print("\nBANANANANANANAAAAAAA!!")
    if favorite_fruit == 'apple':
        print("\nI love apples!")
    if favorite_fruit == 'kiwi':
        print("\nI love kiwi!")
print()


# Check that a list is not empty:
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("Your pizza is ready!")
else:
    print("Are you sure you want a plain pizza?")


# Use multiple lists:
requested_toppings = ['mushrooms', 'extra cheese', 'pineapple', 'ham']
available_toppings = ['mushrooms', 'extra cheese', 'pepperoni', 'olives']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we're out of {requested_topping}.")
print("\nYou're pizza is ready!")
print()