# Loop through an entire list
magicians = ['alice', 'david', 'camille', 'yuzuki', 'jin']
for magician in magicians:
    #print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"Can't wait to see you again {magician.title()}!\n")
print("Thank you everyone, see you next time!\n")


# Pizza
pizzas = ['4 fromages', 'chèvre', 'margarita']
for pizza in pizzas:
    print(f"I like {pizza.title()}")
print("\nI really love pizza!\n")


# Animals
animals = ['Horse', 'Zebra', 'Donkey', 'Lama']
for animal in animals:
    print(f"A {animal.lower()} would make a great pet!")
print("\nAny of them would make a great pet!")