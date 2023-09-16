# 'import pizza' tells Python to open the file pizza.py and copy all the functions from it into this program.
# If we import an entire module, each function is available through the following syntax:
# module_name.function_name()

import pizza

pizza.make_pizza(10, "pepperoni")
pizza.make_pizza(45, "mushrooms", "extra cheese")


# We can also import specific functions, as many as we want, sperating each function with a comma
# No need to use the dot notation
from pizza import make_pizza
make_pizza(30, "pepperoni")


# Using as to give a function an alias
# If the name of a function might conflict with an existing name in the program,
# or if the function anme is long, we can use a short, unique alias
from pizza import make_pizza as mp
mp(16, "pepperoni")


# Using as to give a module an alias. Better readability of the code
import pizza as p
p.make_pizza(10, "cheese")


# Importing all functions in a module
# Tell Python to import every function in a module by using *
# We don't need the dot notation. 
# Best to use this approach. 
# Python may see several functions or variables with the same name and instead of importing the functions seperately, it will overwrite the functions.


