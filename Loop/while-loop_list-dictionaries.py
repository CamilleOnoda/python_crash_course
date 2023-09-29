# users that need to be verified and an empty list for confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until no more unconfirmed users.
# Move each verified users into the list of confirmed users

"""while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)"""

# Display all confirmed users
"""print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())"""


# Removing all instances of specific values from a list
"""pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' and 'dog' in pets:
    pets.remove('cat')
    pets.remove('dog')
print(pets)"""


# Filling a dictionary with user input
responses = {}
# Set a flag to indicate the poll is active
polling_active = True

while polling_active:
    # Prompt for the person'name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")