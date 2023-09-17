# Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called: {self.restaurant_name}.")
        print(f"The cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurant = Restaurant("Kurazushi", "japanese")
restaurant.describe_restaurant()
restaurant.open_restaurant()


# Users
class Users:
    def __init__(self, first_name, last_name, email_address, phone_nb, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_nb = phone_nb
        self.dob = dob

    def describe_user(self):
        print(f"First name: {self.first_name}.")
        print(f"Last name: {self.last_name}.")
        print(f"E-mail address: {self.email_address}.")
        print(f"Phone number: {self.phone_nb}.")
        print(f"Date of birth: {self.dob}.")
        print()

    def greet_user(self):
        print(f"Hello {self.first_name}! Happy to have you join us!")


user1 = Users("Camille", "XYZ", "camille@address.com", "0123456789", "15/09/1988")
user2 = Users("Marc", "ABC", "marc@address.com", "987654321", "15/12/1990")
user3 = Users("Julie", "POM", "julie@address.com", "0123456789", "20/12/1996")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
