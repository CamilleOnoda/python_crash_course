yuzuki = {
    'first_name': 'yuzuki',
    'last_name': 'Onoda',
    'age': '2.5',
    'city': 'Nagoya'
    }
print(yuzuki['first_name'].title())
print(yuzuki['last_name'])
print(yuzuki['age'])
print(yuzuki['city'])
print()

favorite_numbers = {
    'Camille': '6',
    'Jin': '7',
    'Yuzuki': '2',
    'Marc': '15',
    'Leon': '8',
}
# Loop through a dictionary: for key, value in dictionary.items():
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is: {number}.")
print()

glossary = {
    'Argument': 'An argument is a way to provide more information to a function. The function can then use that information as it runs, like a variable.',
    'Bit':'The individual 1 and 0 you see in binary are called bits.',
    'For loops': 'For loops allow you to run a block of code repeatedly, just like while loops. However, for loops run a block of code a set number of times. (Remember, while loops run an unknown or unspecified amount of times.',
    'Linux': 'Linux is an open-source operating system designed to run on multiple types of devices, like laptops, phones, tablets, robots, and many others. In fact, the Android operating system is based on Linux!',
    'Main function': 'For a program to run, it must have a main function, which runs first each time you start your program. The main function is where the bulk of your code will go.',
}
for word, definition in glossary.items():
    print(f"{word}\n{definition}\n")
print()


rivers = {
    'rio grande': 'united states',
    'beni': 'bolivia',
    'northern salado': 'argentina',
}
for river, country in rivers.items():
    if country == ("united states"):
        print(f"The {river.title()} runs through the {country.title()}.\n")
    else:
        print(f"The {river.title()} runs through {country.title()}.\n")
print()


people = []
person = {
    'first_name': 'yuzuki',
    'last_name': 'Onoda',
    'age': '2.5',
    'city': 'ショベルカー町'
    }
people.append(person)

person = {
    'first_name': 'Camille',
    'last_name': 'Onoda',
    'age': '35',
    'city': 'Nagoya'
    }
people.append(person)

person = {
    'first_name': 'Jin',
    'last_name': 'Onoda',
    'age': '35',
    'city': 'Rubicon'
    }
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    location = person['city'].title()
    
    print(f"{name} lives in {location} and is {age} years old.")
print()

cities = {
    'tokyo': {
      'country': 'japan',
      'population': 125_000_000,
      'language': 'japanese', 
    },
    'paris': {
        'country': 'france',
        'population': 64_000_000,
        'language': 'french',
    },
    'new york': {
        'country': 'united states',
        'population': 8_400_000,
        'language': 'english',
    }
}
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    language = city_info['language'].title()
    if country == ('united states').title():
        print(f"{city.title()} is in the {country}.")
    else:
        print(f"{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  People speak {language.title()}.")

