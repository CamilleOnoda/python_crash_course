# Object-oriented programming
# 'Classes' represent real-world things and situations and we create 'objects' based on these classes
# With a class: we define the general behavior that a whole category of 'objects' can have.
# Making an 'object' from a 'class' is called 'instantiation' and we work with 'instances' of a class

# Creating and using a class
# Make an object representing a dog with general info: 'name' and 'age and general behavior 'sit' and 'roll over'


# By convention, class names are capitalized
class Dog:
    # The __init__ method (function part of class is a method)
    # The __init__ method is run automatically whenever we create a new instance based on the Dog class
    def __init__(self, name, age):
        # Initialize name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        # Simulate a dog sitting in response to a command
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # Simulate rolling over in response to commmand
        print(f"{self.name} rolled over!")