# Guest list. List of at least 3 people I would like to invite for dinner. Print a message to each person, inviting them to dinner

guests_list = ['Gimli', 'Gandalf', 'Sam']
#print(f"Dear {guests_list[0]}, I invite you for dinner in my humble home.")
#print(f"Dear {guests_list[1]}, I invite you for dinner in my humble home.")
#print(f"Dear {guests_list[2]}, I invite you for dinner in my humble home.")
for guest in guests_list:
    print(f"Dear {guest}, I invite you for dinner in my humble home.\n")


# Changing guest list.
guest_removed = 'Sam'
guests_list.remove(guest_removed)
print(f"I wish you googd luck {guest_removed}! All the best on your journey to carry this annoying little fellow up Mount Doom!")
guests_list.append('Aragorn')
#print(guests_list)
print(f"\nI'm delighted to announce that {guests_list[-1]} will be joining us for dinner!")


# More guests
print(f"\nMore people will be joining us!")
Fellowship = guests_list
print(f"\nLet's call ourselves, The Fellowship of the AnPanMan bread!\n")
Fellowship.insert(0, 'Legolas')
Fellowship.insert(2, 'BaikinMan')
Fellowship.append('Terminator')
for guest in Fellowship:
    print(f"Dear {guest}, join us for mighty dinner!")


# Shrinking guest list
print(f"\nI'm sorry to inform that I can only invite 2 people.")
print(Fellowship)
guest_pop1 = Fellowship.pop(-1)
guest_pop2 = Fellowship.pop(4)
guest_pop3 = Fellowship.pop(3)
print(f"I'm sorry {guest_pop1}, see you next time!")
print(f"I'm sorry {guest_pop2}, see you next time!")
print(f"I'm sorry {guest_pop3}, see you next time!")
print(Fellowship)
del Fellowship[0:3]
print(Fellowship)



