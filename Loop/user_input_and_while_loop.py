"""
message = input("Tell me something and I will repeat it back to you: ")
print(message)

name = input("Please, enter your name: ")
print(f"Hello {name}!")"""


# Prompt that is longer than one line
"""prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your name? "
name = input(prompt)
print(f"Hello {name}!")"""


# Use int() to accept numerical input
"""age = int(input("How old are you? "))
print(type(age))"""


# The modulo operator %
"""modulo = 7 % 3
print(modulo)

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")"""


# While loops
"""current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1"""


# Let the user decide when to quit
"""prompt = "\nTell me something and I will repeat it back to you! "
prompt += "\nEnter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)"""


# Using a Flag
# For a programm that should run only as long as many conditions are True,
# We can define on variable (a flag) that determines if the entire program is active.
# Useful when many events can make a program stop running.


"""active = True
while active:
    prompt = "\nTell me something and I will repeat it back to you! "
    prompt += "\nEnter 'quit' to end the program: "

    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)"""


# Using break to exit a loop
"""prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city}!")"""


# Using continue in a loop. Return to the begining of the loop based on the result
# of a conditional test.
current_number = 0
# Here, a loop that counts from 1 to 10 and prints only the odd numbers.
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
