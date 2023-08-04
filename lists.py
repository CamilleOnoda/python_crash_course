# Lists are created using square brackets, single quotes and seperated by a comma
# Accessed by index

bicyles = [' giant', 'cannondale', 'treck', 'specialized']
#print(bicyles[1].upper())
#print(bicyles[-1])
#print(bicyles[-2].capitalize())
#print(bicyles[0].strip().title())
#print(f"My first bicyle was a {bicyles[0].title().strip()}.")

# Modify elements in a list
bicyles[-1] = 'BMC'
#print(bicyles)

# Add elements to a list. Append method takes one argument and append it at the end of the list.
bicyles.append('specialized')
bicyles[0] = bicyles[0].strip()
#print(bicyles)

#Insert elements to a list at any position in the list by specifying the index.
bicyles.insert(0, 'Chocolate')
#print(bicyles)


# Deleting elements from a list, if we know its position. Value can't be accessed anymore afterwards.
del bicyles[0]
#print(bicyles)

# Removing items with pop() method. Removes the last item from the list. The value is still accessible.
bicyles_popped = bicyles.pop()
print(bicyles)
print(bicyles_popped)



family_members = ['Jin', 'Yuzuki', 'Isabelle', 'Christian', 'Charlotte', 'Carole', 'Shunji', 'Atsuko', 'Kanjiro']
message = f"My husband is {family_members[0]}. We have a daughter called {family_members[1]}. My mother's name is {family_members[2]} and my father's name is {family_members[3]}. I have two sisters: {family_members[4]} and {family_members[5]}. {family_members[6]} and {family_members[7]} are {family_members[0]}'s parents and {family_members[-1]} is his brother."
#print(message)
#for member in family_members:
    #print(f"Hi {member}! How are you today?")


#Removing
