# Tuple = list of items that can't change. Immutable. Access elements with their index.
# Tuples are technically defined by a comma. 
# The parentheses make them look neater and easier to read.

dimension = (200, 50)
dimensions = 200, 100
print(type(dimensions))
print(dimensions)
print(dimensions[0])
print(dimensions[1])
print()
print(type(dimension))
print(dimension)
print(dimension[0])
print(dimension[1])
print()
#dimension[0] = 250 # Can't support item assignment because a tuple is immutable.


# Loop through all values in a tuple
for dimension in dimensions:
    print(dimension)


# Overwrite a tuple. We can't modify a tuple but we can assign a new value 
# to a variable that represents a tuple.
print()
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print()
dimensions = (100, 150)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
print()


# Exercise
basic_food = ('pizza', 'steak', 'rizotto', 'salad', 'pasta')
for food in basic_food:
    print(food)
print()
#basic_food[0] = 'onigiri'
basic_food = ('onigiri', 'steak', 'rizotto', 'corn soup', 'pasta')
for food in basic_food:
    print(food)
