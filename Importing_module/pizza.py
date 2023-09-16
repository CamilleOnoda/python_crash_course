def make_pizza(size, *toppings):
    print(f"\nMaking a {size}cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("30", "pepperoni")
make_pizza("20", "mushrooms", "extra cheese", "green peppers")