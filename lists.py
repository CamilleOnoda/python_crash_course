            # Lists are created using square brackets, single quotes and seperated by a comma


family_members = ['Jin', 'Yuzuki', 'Isabelle', 'Christian', 'Charlotte', 'Carole', 'Shunji', 'Atsuko', 'Kanjiro']
message = f"My husband is {family_members[0]}. We have a daughter called {family_members[1]}. My mother's name is {family_members[2]} and my father's name is {family_members[3]}. I have two sisters: {family_members[4]} and {family_members[5]}. {family_members[6]} and {family_members[7]} are {family_members[0]}'s parents and {family_members[-1]} is his brother."
#print(message)
#for member in family_members:
    #print(f"Hi {member}! How are you today?")

bicycles = [' giant', 'cannondale', 'treck', 'specialized']
#print(bicycles[1].upper())
#print(bicycles[-1])
#print(bicycles[-2].capitalize())
#print(bicycles[0].strip().title())
#print(f"My first bicyle was a {bicycles[0].title().strip()}.")


            # MODIFY elements in a list
bicycles[-1] = 'BMC'
#print(bicycles)


            # ADD elements to a list. Append method takes one argument and append it at the end of the list.
bicycles.append('specialized')
bicycles[0] = bicycles[0].strip()
#print(bicycles)


            # INSERT elements to a list at any position in the list by specifying the index.
bicycles.insert(0, 'Chocolate')
#print(bicycles)


            # DELETE elements from a list, if we know its position. Value can't be accessed anymore afterwards.
del bicycles[0]
#print(bicycles)


            # POP items with pop() method. If no index is specified: removes by default the last item from the list. The value is still accessible.
bicycles_popped = bicycles.pop()
#print(bicycles)
#print(bicycles_popped)


            # pop() method can be useful if the list is in chronological order and for example, here, I want to print the last bicycle I owned:
#print(bicycles)
#last_owned = bicycles.pop()
#print(f"The last bicycle I owned was a {last_owned.upper()}.")
#print(bicycles)


            # Popping item from any position
first_owned = bicycles.pop(0)
#print(f"The first bicycle I owned was a {first_owned.upper()}.")
#print(bicycles)


            # REMOVE an item by value. remove() only the first occurence of the item. Use a loop to remove every occurences.
bikes = ['Giant', 'Cannondale', 'BMC', 'Specialized', 'Treck']
too_expensive = 'Specialized'
bikes.remove(too_expensive)
#print(bikes)
#print(f"A {too_expensive} is too exepensive for me.")


            # SORT a list permanently with sort() method
cars = ['bmw', 'toyota', 'audi', 'suzuki']
#cars.sort()
print(cars)
#cars.sort(reverse=True)
#print(cars)


            # SORT temporarily with sorted() function
print("\nHere is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("here is the original list again:")
print(cars)


            #REVERSE()method. Reverse the order a list permanently.
cars.reverse()
print(cars)


            # LENGTH of a list
#print(len(cars))


            # RANGE function
for value in range(1, 6):
    print(value)
print()
for value in range(10):
    print(value)


            # Make a list of numbers with range()
numbers = list(range(1, 7))
print(numbers)
print()


            # Skip numbers with range(). The third argument is used as a step size
odd_numbers = list(range(1, 52, 2))
print(odd_numbers)


            # List of the first 10 square numbers
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    #square = value ** 2
    #squares.append(square)
print(squares)


digits = [1, 2, 3, 4, 5, 50, 89, 10, 569, 89]
print(min(digits))
print(max(digits))
print(sum(digits))
