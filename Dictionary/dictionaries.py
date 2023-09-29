# A dictionary is a collection of key-value pairs.
# Use the key to access the value.
# A value can be any object that we can create in python.

# Inside the braces, the key is connected to its value by a colon.
# Individual key-value pairs are separated by a comma.
alien_0 = {'color': 'green', 'points': 5}

# Access the value associated with a key.
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Add a new key-value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Start with an empty dictionary
alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)

# Modify values in a dictionary
alien_1['color'] = 'red'
print(f"The alien is now {alien_1['color']}.")
print(alien_1)
print()


alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#alien_1['speed'] = 'fast'
print(f"Original position: {alien_1['x_position']}")

# Move the alien to the right
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New position: {alien_1['x_position']}")


# Remove key-value pair !permanently!
del alien_0['points']
print(alien_0)


# Dictionary of similar objects. Here, each key is the name of a person
# and each value is their language choice.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")


# Use get() to access values. 
# Set a default value that will be returned if the requested key doesn't exist.
# If we don't enter the second argument, python will return 'None'.
# Avoid getting an error.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


# Loop through a dictionary: for key, value in dictionary.items():
favorite_numbers = {
    'Camille': '6',
    'Jin': '7',
    'Yuzuki': '2',
    'Marc': '15',
    'Leon': '8',
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is: {number}.")
print()



# Loop through all the keys in a dictionary.
# Looping through the keys is the default behavior so omitting .keys() would 
# produce the same result. It just makes the code easier to read.
for name in favorite_languages.keys():
    print(name.title())
print()

friends = ['sarah', 'phil']
for name in favorite_languages:
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!\n")


# Loop through a dictionary's keys in a particular order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.\n")


# Loop through all values
print("The following languages have been mentionned:")
for language in favorite_languages.values():
    print(language.title())
print()


# Wrap a collection of values that contains duplicate with set() to ask python to identify unique items.
print("The following languages have been mentionned:")
for language in set(favorite_languages.values()):
    print(language.title())
print()


# Build a set directly and loop through
languages = {'python', 'c', 'rust', 'python'}
print(languages)
print()
for x in languages:
    print(x.title())
print()


# Nesting

# A list of dictionaries.
# Common when each dictionary contain mani kinds of information about one object. 
# All the dictionaries in the list should have
# identical structure to allow looping through the list.

alien_0['points'] = 5
del alien_0['x_position']
del alien_0['y_position']
print(alien_0)
print()

alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print()

# Empty list to store aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the characteristics of the first 3 aliens.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many have been created.
print(f"The total number of aliens is: {len(aliens)}.")
print()


# A list in a dictionay
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t--{topping}")

# List of languages in a dictionary.
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'javascript'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


# A dictionary in a dictionary
users = {
    'yuzuB': {
        'first': 'Yuzuki',
        'last': 'Bouboule',
        'location': 'ショベルカー町'
    },

    'jB': {
        'first': 'Jon',
        'last': 'Bovi',
        'location': 'Rubicon'
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFullname: {full_name}")
    print(f"\tLocation: {location}")

# Do not nest lists and dictionaries too deep. There's likely a simpler way to do.