#Python is fun :D

message = "Hello Python world!!"
#print(message)

message = "パン食べたいな..."
#print(message)

name = "camille onoda"
#print(name.capitalize())
#print(name.title())
#print(name.upper())
#print(name.title())


first_name = "yuzuki"
last_name = "boulette"
aka = "テレビみたいよ!"
#print(f"{first_name.title()} {last_name.title()}, AKA: {aka}")

full_name = 'yuzuki boulette'
#print(f"{full_name.title()}<3 Aka: {aka}")

message = f"Bonjour, \n\t{full_name.title()}!\n\t\tAka: {aka}\n\t\t\t" +"<3" * 6
#print(message)



favorite_language = " python "
#print(favorite_language)

# Remove whitespace from the right
favorite_language = favorite_language.rstrip()

# Remove whitespace from the left
favorite_language = favorite_language.lstrip()

# Remove whitespace from both sides
favorite_language = favorite_language.strip()
#print(favorite_language)



nostarch_url = "https://nostarch.com"
no_prefix = nostarch_url.removeprefix("https://")
#print(no_prefix)

filename = "python_notes.txt"
no_suffix = filename.removesuffix(".txt")
#print(no_suffix)