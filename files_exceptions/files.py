# Reading from a file
from pathlib import Path

# Create a Path object representing pi_digits.txt
path = Path('pi_digits.txt')
# Read the content and store in variable 'content'
content = path.read_text()
content = content.rstrip()
print(content)
print()

# Accessing a file's lines
path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
# Working with a file's content
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

