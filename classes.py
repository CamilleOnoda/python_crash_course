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
    # The self parameter must always be included, in first position.
    # It gives access to the attributes and methods in the class
    def __init__(self, name, age):
        # Initialize name and age attributes
        # Variable accessible through instances are called 'attribute'
        # Any variable created with self. is available to every method in the class
        self.name = name
        self.age = age

    def sit(self):
        # Simulate a dog sitting in response to a command
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # Simulate rolling over in response to commmand
        print(f"{self.name} rolled over!")



# Making an instance of a class
# A class is a set of isntructions for how to make an instance
# Instance representing a specific dog:

my_dog = Dog('Catou', 4)

print(f"My dog's name is {my_dog.name}. ", end="")
print(f"He is {my_dog.age} years old.")