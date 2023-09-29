# Reading from a file
from pathlib import Path

# Create a Path object representing pi_digits.txt
path = Path('pi_digits.txt')
# Read the content and store in variable 'content'
content = path.read_text()
content = content.rstrip()
print(content)


# Relative and absolute file Paths
