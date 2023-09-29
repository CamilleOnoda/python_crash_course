# Message
def display_message():
    print("I'm learning about functions! This is Chapter 8 of Python Crash Course.")

display_message()


# Favorite book
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")

favorite_book("jojos Bizarre Adventures")


# T-shirt
def make_shirt(size="L", message="I Love Python"):
    print(f"\nThe size of this T-shirt is {size} and the message: {message}")

make_shirt(message="Hello, World!", size="S")
make_shirt()
make_shirt(size="M")


# Cities
def describe_city(name, country="Japan"):
    print(f"{name} is in {country}")

describe_city("Tokyo")
describe_city("Sapporo")
describe_city("Paris")


# Album
def make_album(artist_name, album_title, number_songs=None):
    album = {'Artist': artist_name, 'Album title': album_title}
    if number_songs:
        album['Number of songs'] = number_songs
    return album

music = make_album("Noel Gallagher", "Council Skies", "14")
print(music)



# Messages
messages = {'LOL', 'IDK', 'ASAP'}
sent_messages = []

def show_messages(messages):
    for msg in messages:
        print(f"{msg}")
        print()


def send_messages(messages):
    while messages:
        current_msg = messages.pop()
        print(current_msg)
        sent_messages.append(current_msg)
        print(sent_messages)


show_messages(messages)
send_messages(messages)
