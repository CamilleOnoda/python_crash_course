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
