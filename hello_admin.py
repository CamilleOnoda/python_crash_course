# Exercise
username = ['admin', 'Kami63', 'Yukette007', 'Jon Bovi', 'Terminator63']
# Make sure the list is not empty
if username:
    for name in username:
        if name == 'admin':
            print("Hello admin! Would you like to see a status report?")
        else:
            print(f"Hi {name}! Thank you for logging in again.")
else:
    print("We need to find some users!")


current_users = ['Terminator63', 'Kami63', 'Yukette007', 'Jon Bovi', 'Harvey']
new_users = ['YUKETTE007', 'Jon Bovi', 'Camille', 'Jin', 'Yuzuboule']


current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"'{new_user}' is already used. Find a new username!")
    else:
        print(f"'{new_user}' is available.")


numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print((f"{number}th"))