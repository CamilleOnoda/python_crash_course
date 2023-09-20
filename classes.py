# Object-oriented programming

# 'Classes' represent real-world things and situations and we create 'objects' based on these classes
# With a class: we define the general behavior that a whole category of 'objects' can have.
# Making an 'object' from a 'class' is called 'instantiation' and we work with 'instances' of a class

# Creating and using a class
# Make an object representing a dog with general info: 'name' and 'age and general behavior 'sit' and 'roll over'


# By convention, class names are capitalized
class Dog:
    # The __init__ method (function part of a class is a method)
    # The __init__ method is run automatically whenever we create a new instance based on the Dog class
    # The self parameter must always be included, in first position.
    # It refers to the instance of the class that is being used.
    # It gives access to the attributes and methods in the class.
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
# Accessing attributes 'my_dog.name'
print(f"My dog's name is {my_dog.name}. ", end="")
print(f"He is {my_dog.age} years old.")
# After we create an instance from the class Dog, we can use the dot notation to call any methods defined in Dog
my_dog.sit()
my_dog.roll_over()


# Creating multiple instances
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {your_dog.name}. ", end="")
print(f"He is {your_dog.age} years old.")
print()


# Working with classes and instances
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Set an default value.
        # When Python calls __init__, it will create a new attribute called 'odometer_reading'
        # And sets its inital value to 0.
        # Add an attribute that changes over time: the car overall mileage.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        """self.odometer_reading = mileage"""

    # Incrementing an attribute's value through a method
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
# Modify the attribute value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modify an attribute value through a method
my_new_car.update_odometer(30_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(500)
my_new_car.read_odometer()

