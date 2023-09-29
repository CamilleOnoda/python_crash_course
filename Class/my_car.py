# Python can let you store classes in modules and then import the classes we need
# I use a file called 'car.py' containing the classes I want to import
# Files need to be in the same folder

from car import Car, ElectricCar

my_new_car = Car('Suzuki', 'Hustler', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 30
my_new_car.read_odometer()

my_mustang = ElectricCar('ford', 'mustang', 1995)
print(my_mustang.get_descriptive_name())
my_mustang.battery.describe_battery()
my_mustang.battery.get_range()
