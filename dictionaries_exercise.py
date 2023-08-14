yuzuki = {
    'first_name': 'yuzuki',
    'last_name': 'Onoda',
    'age': '2.5',
    'city': 'Nagoya'
    }
print(yuzuki['first_name'])
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
#Loop through a dictionary: for key, value in dictionary.items():
for key, value in favorite_numbers.items():
    print(f"{key}'s favorite number is: {value}.")
print()


glossary = {
    'Argument': 'An argument is a way to provide more information to a function. The function can then use that information as it runs, like a variable.',
    'Bit':'The individual 1 and 0 you see in binary are called bits.',
    'For loops': 'For loops allow you to run a block of code repeatedly, just like while loops. However, for loops run a block of code a set number of times. (Remember, while loops run an unknown or unspecified amount of times.',
    'Linux': 'Linux is an open-source operating system designed to run on multiple types of devices, like laptops, phones, tablets, robots, and many others. In fact, the Android operating system is based on Linux!',
    'Main function': 'For a program to run, it must have a main function, which runs first each time you start your program. The main function is where the bulk of your code will go.',
}
for word, definition in glossary.items():
    print(f"{word}: {definition}\n")