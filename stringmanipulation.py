#  Removing Whitespace
# strip(): Removes leading and trailing whitespace (including \n).
# lstrip(): Removes leading whitespace.
# rstrip(): Removes trailing whitespace.

text = "  Hello, World!  \n"
print(text.strip())   # "Hello, World!"
print(text.lstrip())  # "Hello, World!  \n"
print(text.rstrip())  # "  Hello, World!"

#  Changing Case
# upper(): Converts all characters to uppercase.
# lower(): Converts all characters to lowercase.
# capitalize(): Capitalizes the first character of the string.
# title(): Capitalizes the first character of each word.
# swapcase(): Swaps the case of all characters.

text = "hello, World!"
print(text.upper())       # "HELLO, WORLD!"
print(text.lower())       # "hello, world!"
print(text.capitalize())  # "Hello, world!"

#  Splitting and Joining Strings
# split(): Splits a string into a list based on a delimiter (default is whitespace).
# splitlines(): Splits a string into a list of lines.
# join(): Joins a list of strings into a single string with a specified delimiter.
text = "apple,banana,cherry"
print(text.split(","))  # ['apple', 'banana', 'cherry']

lines = "line1\nline2\nline3"
print(lines.splitlines())  # ['line1', 'line2', 'line3']

words = ['apple', 'banana', 'cherry']
print(", ".join(words))  # "apple, banana, cherry"

#  Replacing Substrings
# replace(): Replaces occurrences of a substring with another substring.
text = "I like apples"
print(text.replace("apples", "bananas"))  # "I like bananas"


#  String Slicing
# Extract parts of a string using slicing.

text = "Hello, World!"
print(text[0:5])   # "Hello"
print(text[8:])    # "orld!" excluding first 8 characters
print(text[-4:])   # "World!" last 4 characters