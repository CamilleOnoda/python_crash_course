# List comprehension combine the for loop and the creation of new elements into one line and automatically append each new element.

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
#print(squares)

# Same with a list comprehension.
squares = [value ** 2 for value in range(1, 11)] # The value we want to store in 'squares' is 'value ** 2'. We then write the for loop to generate the numbers.
#print(squares)

numbers = []
for number in range(1, 1_000_001):
    numbers.append(number)
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))


odd_numbers = [number for number in range(1, 20, 2)]
print(odd_numbers)

cubes = [value ** 3 for value in range(1, 10)]
print(cubes)

cubes = []
for value in range(1, 10):
    cubes.append(value ** 3)
print(cubes)
