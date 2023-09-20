# Import an entire module
# We can access the classes we need through this syntax: module_name.ClassName

import car

my_mustang = car.Car('ford', 'mustang', 2023)
print(my_mustang.get_descriptive_name())

my_hustler = car.ElectricCar('suzuki', 'hustler', 2022)
print(my_hustler.get_descriptive_name())