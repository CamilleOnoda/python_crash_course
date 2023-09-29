# Deli
sandwich_orders = ['ham', 'cheese', 'bacon', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("We ran out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you a {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print(f"Sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)















# Dream vacation. Program that polls the users for their dream vacation.
"""responses = {}
polling_active = True

while polling_active:
    # Prompt user for name and response
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    # Store reponse in the dictionary
    responses[name] = response

    # Ask if anyone else can take the poll
    repeat = input("Would you like anyone else to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# Show the results
print(f"--- Poll reuslts ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}")"""