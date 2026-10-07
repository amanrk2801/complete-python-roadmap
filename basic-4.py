### 7. Strings in Python
# Strings are used to store text data in Python. A string is a sequence of characters enclosed in quotes.
# 1. Creating Strings
name = "Aman"
city = 'Nagpur'
message = """This is
a multi-line
string"""
print(name)
print(city)
print(message)

# 2. Single, Double, and Triple Quotes
# Single Quotes
text1 = 'Hello 1'
# Double Quotes
text2 = "Hello 2"
# Triple Quotes
# Used for multi-line strings.
text3 = """Python
is
awesome"""
print(text1)
print(text2)
print(text3)

# 3. String Indexing
# Every character has an index.
word1 = "Python"
# Character  Index  Negative Index
# P        -> 0   -> -6
# y        -> 1   -> -5
# t        -> 2   -> -4
# h        -> 3   -> -3
# o        -> 4   -> -2
# n        -> 5   -> -1
word = "Python"
print(word[0]) # P
print(word[1]) # y
print(word[-1]) # n

# 4. String Slicing
# Syntax: string[start:end:step]
word = "Python"
print(word[0:3]) # Pyt
print(word[2:5]) # tho
print(word[:4]) # Pyth
print(word[3:]) # hon
print(word[::-1]) # nohtyP

# 5. String Concatenation
# Joining strings using +.
first = "Hello"
second = "World"
result = first + " " + second
print(result) # Hello World

# 6. String Repetition
# Using *.
print("Python " * 3) # Python Python Python

# 7. String Immutability
# Strings cannot be changed after creation.
# ❌ Wrong
name = "Python"
# name[0] = "J" # TypeError: 'str' object does not support item assignment
# ✅ Correct
name1 = "Python"
name1 = "J" + name1[1:]
print(name1) # Jython

# 8. String Methods
# lower(): Converts to lowercase.
text = "PYTHON"
print(text.lower()) # python

# upper(): Converts to uppercase.
text = "python"
print(text.upper()) # PYTHON

# strip(): Removes spaces from both ends.
text = "  Python  "
print(text.strip()) # Python

# split(): Converts string into a list.
text = "apple,banana,mango"
print(text.split(",")) # ['apple', 'banana', 'mango']

# join(): Joins elements of a list.
items = ["apple", "banana", "mango"]
print("-".join(items)) # apple-banana-mango

# replace()
text = "I like Java"
print(text.replace("Java", "Python")) # I like Python

# find(): Returns position if found else -1.
text = "Python Programming"
print(text.find("Pro")) # 7

# index(): Same as find but gives error if not found.
text = "Python"
print(text.index("t")) # 2

# startswith()
text = "Python"
print(text.startswith("Py")) # True

# endswith()
text = "Python"
print(text.endswith("on")) # True

# count(): Counts occurrences.
text = "banana"
print(text.count("a")) # 3

# capitalize(): First letter uppercase.
text = "python"
print(text.capitalize()) # Python

# title(): First letter of every word uppercase.
text = "python programming"
print(text.title()) # Python Programming

# swapcase(): Upper ↔ Lower
text = "PyThOn"
print(text.swapcase()) # pYtHoN

# isdigit(): Checks only digits.
print("123".isdigit()) # True
print("12a".isdigit()) # False

# isalpha(): Checks only letters.
print("Python".isalpha()) # True
print("Python123".isalpha()) # False

# isalnum(): Checks letters and numbers only.
print("Python123".isalnum()) # True
print("Python 123".isalnum()) # False

# 9. Raw Strings: Treats backslashes as normal characters.
path = r"C:\Users\Aman\Documents"
print(path) # C:\Users\Aman\Documents # correct
# Without raw string:
print("C:\new") # \n becomes a newline. # wrong

# 10. Unicode: Python supports Unicode characters.
text = "नमस्ते"
print(text) # नमस्ते
emoji = "😊"
print(emoji) # 😊

# 11. Encoding: Converting string → bytes.
text = "Python"
encoded = text.encode()
print(encoded) # b'Python'

# 12. Decoding: Converting bytes → string.
data = b'Python'
decoded = data.decode()
print(decoded) # Python

# 13. Regular Expressions (Regex): Used for pattern matching.
# Find a word
import re
text = "Python is easy"
result = re.search("easy", text)
print(result.group()) # easy

# Find all digits
import re
text = "Age is 25 and roll is 101"
print(re.findall(r"\d+", text)) # ['25', '101']

# Validate Email
import re
email = "test@gmail.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
print(bool(re.match(pattern, email))) # True

# Interview Questions
# Q1. Difference between find() and index()?
text = "Python"
print(text.find("z"))     # -1
# print(text.index("z"))    # ValueError
# find() → returns -1 if not found
# index() → raises error if not found

# Q2. Difference between split() and join()?
text = "a,b,c"
print(text.split(",")) # ['a', 'b', 'c']
items = ['a', 'b', 'c']
print("-".join(items)) # a-b-c
# split() → String → List
# join() → List → String

# Practice Programs
# 1. Reverse a String
text = input("Enter string: ")
print(text[::-1])
# 2. Count Vowels
text = input("Enter string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)
# 3. Check Palindrome
text = input("Enter string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# 4. Count Characters
text = input("Enter string: ")
print(len(text))
# 5. Count Words
text = input("Enter sentence: ")
print(len(text.split()))
# Remember: Strings are one of the most important topics in Python and are heavily used in interviews, automation, web development, APIs, file handling, and data processing.

# ------------------------------------------------------- #


