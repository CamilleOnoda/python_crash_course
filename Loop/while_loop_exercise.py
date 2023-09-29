#Pizza toppings
"""prompt = "Enter your pizza toppings:\n"
prompt += "(Enter 'quit' when you're finished.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"{topping.title()} will be added to your pizza.")"""


# Movie tickets
"""prompt = "How old are you? "
while True:
    age = int(input(prompt))
    if age <= 3:
        print("The ticket is free.")
        break
    elif 3 < age <= 12:
        print("The ticket is $10.")
        break
    else:
        print("The ticket $15.")
        break"""


# Three exits
"""prompt = "How old are you? "
active = True
while active:
    age = int(input(prompt))
    if age <= 3:
        print("The ticket is free.")
        active = False
    elif 3 < age <= 12:
        print("The ticket is $10.")
        active = False
    else:
        print("The ticket $15.")
        active = False"""

    
prompt = "Enter your pizza toppings:\n"
prompt += "(Enter 'quit' when you're finished.)"

while prompt != 'quit':
    topping = input(prompt)
    print(f"{topping.title()} will be added to your pizza.")
    break