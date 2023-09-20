from car import ElectricCar

my_hustler = ElectricCar('Suzuki', 'Hustler', 2023)
print(my_hustler.get_descriptive_name())
my_hustler.battery.describe_battery()
my_hustler.battery.get_range()