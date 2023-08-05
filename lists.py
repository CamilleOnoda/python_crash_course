            # Lists are created using square brackets, single quotes and seperated by a comma
            # Accessed by index


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


            # Modify elements in a list
bicycles[-1] = 'BMC'
#print(bicycles)


            # Add elements to a list. Append method takes one argument and append it at the end of the list.
bicycles.append('specialized')
bicycles[0] = bicycles[0].strip()
#print(bicycles)


            #Insert elements to a list at any position in the list by specifying the index.
bicycles.insert(0, 'Chocolate')
#print(bicycles)


            # Deleting elements from a list, if we know its position. Value can't be accessed anymore afterwards.
del bicycles[0]
#print(bicycles)


            # Removing items with pop() method. If no index is specified: removes by default the last item from the list. The value is still accessible.
bicycles_popped = bicycles.pop()
#print(bicycles)
#print(bicycles_popped)

            # Pop() method can be useful if the list is in chronological order and for exemple, here, I want to print the last bicycle I owned:
last_owned = bicycles.pop()
#print(f"The last bicycle I owned was a {last_owned.upper()}.")

            # Popping item from any position
first_owned = bicycles.pop(0)
#print(f"The first bicycle I owned was a {first_owned.upper()}.")

            # Removing an item by value. remove() only the first occurence of the item. Use a loop to remove every occurences.
bikes = ['Giant', 'Cannondale', 'BMC', 'Specialized', 'Treck']
too_expensive = 'Specialized'
bikes.remove(too_expensive)
print(bikes)
print(f"A {too_expensive} is too exepensive for me.")

