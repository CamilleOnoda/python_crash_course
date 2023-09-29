# Writing to a file
from pathlib import Path

path = Path('programming.txt')
path.write_text('I looooooooooove programming with Python!')

contents = "Hi! I'm Camille and I'm living in Nagoya.\n"
contents += "I am a translator.\n"
contents += "I'm studying programming with Python and web development."
#When calling write text, it will erase the current content f the file already exists.
path.write_text(contents)