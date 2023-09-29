"""A class representing a restaurant."""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called: {self.restaurant_name}.")
        print(f"The cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")