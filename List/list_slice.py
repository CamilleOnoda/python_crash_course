players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1 : 5]) # [inclusive : exclusive]
print(players[:3]) # All items from the beginning up until index 2
print(players[2:]) # From index 2 until the end of the list
print(players[-2:]) # Start from the end of the list up until a certain distance from the list. Here from index -2(4) until the end.
print(players[0 : 4 : 2]) # Add a third value in the slice to tell python how many items to skip. Here print every 2 items

# Loop through a slice
print("\nHere are the first players on my team:")
for player in players[0 : 3]:
    print(player.title())


# Copy a list and add item to each list.
# If we assign a list equal to another list: \ex friend_foods = my_foods, we associate the variable 'friend_foods' to a list already associated with 'my_foods'
# Both list then point to same direction and if we add one item to 'friend_foods' it will also appear in 'my_foods'
my_foods = ['pizza', 'ramen', 'natto', 'onigiri']
friend_foods = my_foods[:]
print()
print("My favorite foods are:")
print(my_foods)
print("\nMy friends' favorite foods are:")
print(friend_foods)

my_foods.append('ice cream')
friend_foods.append('burger')
print(my_foods)
print(friend_foods)