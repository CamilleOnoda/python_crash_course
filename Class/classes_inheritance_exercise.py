class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called: {self.restaurant_name}.")
        print(f"The cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def describe(self):
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type}!")

    def show_flavors(self):
        print(f"We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


restaurant = Restaurant("Kurazushi", "japanese")
restaurant.describe_restaurant()
restaurant.open_restaurant()

thirty_one = IceCreamStand("31 Ice Cream")
thirty_one.flavors = ["vanilla", "chocolate", "matcha", "raspberry"]
thirty_one.describe()
thirty_one.show_flavors()
print()



# Admin
class Users:
    def __init__(self, first_name, last_name, email_address, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.username = username
        self.location = location

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"E-mail address: {self.email_address}")
        print(f"Usernamer: {self.username}")
        print(f"Location: {self.location}")
        print()

    def greet_user(self):
        print(f"Hello {self.first_name}! Happy to have you join us!")


class Admin(Users):
    """A user with administrative privileges."""
    def __init__(self, first_name, last_name, email_address, username, location):
        super().__init__(first_name, last_name, username, email_address, location)
        self.privileges = Privileges()
"""        self.privileges = [
            'can add post',
            'can can delete post',
            'can ban users',
            'can throw stuff at will',
            'can take shower with Deep Purple music'
            ]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")"""


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This user has no privileges.")



yuzuki = Admin('Yuzuki', 'Boule', 'Madame Boule', 'bouboule@違うでしょう.com', 'おばけLand')
yuzuki.describe_user()
yuzuki.privileges.show_privileges()
print("\nAdding privileges...")
yuzuki_privileges = [
    'can add post',
    'can can delete post',
    'can ban users',
    'can throw stuff at will',
    'can take shower with Deep Purple music'
]

yuzuki.privileges.privileges = yuzuki_privileges
yuzuki.privileges.show_privileges()

