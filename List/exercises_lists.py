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
    print(f"Dear {guest}, join us for a mighty dinner!")


# Shrinking guest list
print(f"\nI'm sorry to inform that I can only invite 2 people.\n")
print(Fellowship)
guest_pop1 = Fellowship.pop(-1)
guest_pop2 = Fellowship.pop(4)
guest_pop3 = Fellowship.pop(3)
print(f"I'm sorry {guest_pop1}, see you next time!")
print(f"I'm sorry {guest_pop2}, see you next time!")
print(f"I'm sorry {guest_pop3}, see you next time!")
print(Fellowship)
#del Fellowship[0:3]
#print(Fellowship)


# Seeing the world. Think of at least 5 places you'd like to visit
places = ['Jasper', 'Mongolia', 'Yellowstone National Park', 'New Zealand', 'Hokkaido']
print()
print("\nHere is the original list:")
print(places)
print("Here is the sorted list:")
x = sorted(places)
print(x)
print("Here is the original list again:")
print(places)

print("\nHere is the list in reverse order:")
places.reverse()
print(places)
print("Here is the list in the original order:")
places.reverse()
print(places)

print("\nHere is the list in alphabetical order:")
places.sort()
print(places)
print("Here is the list in reverse-alphabetical order:")
places.sort(reverse=True)
print(places)


# Dinner guests
print()
print(Fellowship)
number_guests = len(Fellowship)
print(f"\nI invited {number_guests} people for dinner.")


# Every function
mtg_card = ['Wrenn and Six', 'Mycosynth Golem', 'Land Tax', 'Cruel Tutor', 'Primal Vigor', 'Phyrexian Tower', 'Brazen Borrower', 'The Chain Veil', 'Emeria, the Sky Ruin', 'Food Chain']
for card in range(len(mtg_card)):
    mtg_card[card] = mtg_card[card].lower()
print()
print(mtg_card)

card_popped = mtg_card.pop(-1)
print(card_popped)
print(mtg_card)

print(sorted(mtg_card))
mtg_card.reverse()
print(mtg_card)
mtg_card.reverse()
print(mtg_card)

mtg_card.sort(reverse=True)
print(mtg_card)
mtg_card.reverse()
print(mtg_card)
print(len(mtg_card))
print(mtg_card[-4])