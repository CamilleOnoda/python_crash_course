# Define a function
def greet_user():
    # This is a docstring which describes what the function does. 
    # When Python generates documentation for the functions, 
    # it looks for a string immediately after the function definition.
    """Display a greeting message"""
    print("Hello!")

# Call the function to be able to use it
greet_user()


# Pass information to a function
def greet_user(username):
    print(f"Hello {username.title()}!")

greet_user('camille')


# Arguments and parameters
# The variable 'username' above is a parameter: 
# a piece of info the function needs to do its job.
# The value 'camille' is an argument: a piece of info passed from a function 
# call to a function.
# The argument 'camille' was passed to the function greet_user() 
# and the value was assigned to the parameter 'username'.


# Positional arguments. Python must match each argument in the function call 
# with a parameter in the function definition.
# Based on the order of the arguments provided
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Multiple function calls
describe_pet('T-rex', 'Fred')
describe_pet('rabbit', 'Marie')


# Keyword Arguments
# name-value pair passed to a function. We don't have to correctly order
# the arguments in the function call and clarify the role of each value in the function call
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Multiple function calls
describe_pet(pet_name='Marie', animal_type='bear')


# return values
def get_formatted_name(first_name, last_name):
    # return a neatly formatted full name
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("noel", "gallagher")
print(musician)


# Making an argument optional. 
# The optional argument here is set as an empty string at the end of the list of parameters
# Introduce of while loop

"""def get_formatted_name(first_name, last_name, middle_name=""):
    # return a neatly formatted full name
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit.)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        print(f"Hello, {f_name}!")
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")"""
    

# Passing a list

users = ["Camille", "Jin", "Yuzuki"]
def greet_users(users):
    for user in users:
        print(f"Hello, {user.title()}!")
    
greet_users(users)

# Returning a dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', '27')
print(musician)
print()


# Modify a list in a function
unprinted_designs = ['phone case', 'roboy pendant', 'dodecahedron']
completed_models = []

def printing_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(f"- {completed_model}")


printing_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print()


# Passing a copy of a list to a function with the slice notation

# To be used only if we have a specific reason to pass a copy of a list
# More efficient for a function to work with an existing list than using the time
# and memory to create a new one, especially for large lists.
"""function_name(list_name[:])"""

"""print_models(unprinted_designs[:], completed_models)"""



# Passing an arbitrary number of arguments
# Python allows a function to collect an arbitrary number of arguments from the calling statement.

# The * in the parameter name tells python to make a tuple called 'toppings'
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("30", "pepperoni")
make_pizza("20", "mushrooms", "extra cheese", "green peppers")


# Mixing positional and arbitrary arguments
# The parameter that accepts an arbitrary number of arguments must be placed last in the function defintion (See above!)