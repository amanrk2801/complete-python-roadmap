# 27. Context Managers
# - Context Managers help manage resources automatically, such as files, database connections, locks, and network connections. They ensure that setup and cleanup code runs correctly, even if an exception occurs.

# 1. with Statement
# - The with statement automatically handles resource management.
# Without with
file = open("data.txt", "r")
content = file.read()
file.close()
# If an exception occurs before close(), the file remains open.

# With with
with open("data.txt", "r") as file:
    content = file.read()

print(content)
# ✅ File is automatically closed when the block exits.

# 2. Why Use Context Managers?
# Benefits:
# Automatic cleanup
# Prevent resource leaks
# Cleaner code
# Exception-safe
# Easier resource management
with open("data.txt", "w") as file:
    file.write("Hello")
# After leaving the block, the file is closed automatically.

# 3. Custom Context Managers
# - You can create your own context manager using a class.
# Basic Example
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext():
    print("Inside block")

# Output:
# Entering context
# Inside block
# Exiting context

# 4. __enter__()
# - Called automatically when entering the with block.
# Syntax
# def __enter__(self):
#     ...

# Example
class Demo:
    def __enter__(self):
        print("Resource acquired")
        return "Python"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

with Demo() as value:
    print(value)

# Output:
# Resource acquired
# Python
# Resource released

# The value returned from __enter__() is assigned to value.

# 5. __exit__()
# - Called automatically when leaving the with block.
# Syntax
# def __exit__(self, exc_type, exc_value, traceback):
#     ...

# Parameters:
# Parameter -> Description
# exc_type -> Exception type
# exc_value -> Exception object
# traceback -> Traceback information

# Example
class Test:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")

with Test():
    print("Working...")

# Output:
# Start
# Working...
# End

# Handling Exceptions in __exit__
class Demo:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception handled")
        return True

with Demo():
    x = 10 / 0

print("Program continues")

# Output:
# Exception handled
# Program continues

# return True suppresses the exception.

# 6. Real-Life Custom Context Manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed")

with FileManager("test.txt", "w") as f:
    f.write("Hello Python")

# Output: File closed

# 7. contextlib Module
# - Python provides the built-in contextlib module to create context managers more easily.
from contextlib import contextmanager
# Benefits:
# Less code
# More readable
# No need to create classes

# 8. @contextmanager Decorator
# - Using generators and yield.
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Enter")
    yield
    print("Exit")

with my_context():
    print("Inside")

# Output
# Enter
# Inside
# Exit

# 9. Resource Management with @contextmanager
from contextlib import contextmanager

@contextmanager
def open_file(filename):
    file = open(filename, "r")

    try:
        yield file

    finally:
        file.close()
        print("File closed")

with open_file("data.txt") as f:
    print(f.read())
# Output:
# (contents of file)
# File closed

# 10. Exception Handling with @contextmanager
from contextlib import contextmanager

@contextmanager
def manager():
    print("Start")

    try:
        yield

    except ZeroDivisionError:
        print("Division by zero")

    finally:
        print("End")

with manager():
    x = 10 / 0

# Output:
# Start
# Division by zero
# End

# Class vs @contextmanager
# Class-Based
class MyContext:
    def __enter__(self):
        print("Enter")

    def __exit__(self, a, b, c):
        print("Exit")

# Decorator-Based
@contextmanager
def my_context():
    print("Enter")
    yield
    print("Exit")

# Decorator-based context managers are shorter and more readable for simple cases.

# Interview Questions
# Q1: What is a Context Manager?
# - An object that manages resources and automatically performs setup and cleanup operations.

# Q2: What methods are required?
# __enter__()
# __exit__()

# Q3: What does with do?
# - It automatically calls:
# __enter__()
# - when entering the block and
# __exit__()
# - when leaving the block.

# Q4: Why use Context Managers?
# Automatic cleanup
# Exception safety
# Cleaner code
# Resource management

# Q5: What is the difference between __enter__ and __exit__?
# __enter__() → Acquire resource
# __exit__() → Release resource

# Summary
# Context Managers
# │
# ├── with statement
# ├── __enter__()
# ├── __exit__()
# ├── Custom Context Managers
# ├── Exception Handling
# ├── Resource Management
# ├── contextlib module
# └── @contextmanager decorator

# Most Important Exam/Interview Example
from contextlib import contextmanager

@contextmanager
def timer():
    print("Start")
    yield
    print("End")

with timer():
    print("Processing...")

# Output:
# Start
# Processing...
# End

# This example demonstrates with, contextlib, contextmanager, and the lifecycle of a context manager in one concise program.

# --------------------------------------------- #

# 28. Regular Expressions (re Module)
# Regular Expressions (Regex) are patterns used to search, match, extract, validate, and replace text.
# import re

# 1. Patterns
# - A pattern defines what text to search for.
import re

text = "Hello Python"

result = re.search("Python", text)

if result:
    print("Found")

# Output
# Found

# 2. Character Classes
# - Character classes match a set of characters.
# Pattern - Meaning
# [abc] -> a, b, or c
# [a-z] -> lowercase letters
# [A-Z] -> uppercase letters
# [0-9] -> digits
# \d -> digit
# \D -> non-digit
# \w -> letter, digit, _
# \W -> non-word character
# \s -> whitespace
# \S -> non-whitespace

import re

text = "abc123"

print(re.findall(r"\d", text)) # ['1', '2', '3']

# 3. Quantifiers
# - Quantifiers specify how many times a character appears.
# Symbol - Meaning
# * -> 0 or more
# + -> 1 or more
# ? -> 0 or 1
# {n} -> exactly n
# {n,m} -> n to m

import re

text = "aaa"

print(re.findall(r"a+", text)) # ['aaa']

# 4. Groups
# - Groups use parentheses () to group patterns.
import re

text = "John 25"

match = re.search(r"(\w+) (\d+)", text)

print(match.group(1)) # John
print(match.group(2)) # 25

# 5. Capturing Groups
# - Capturing groups store matched data.
import re

text = "Date: 12-05-2025"

match = re.search(r"(\d+)-(\d+)-(\d+)", text)

print(match.groups()) # ('12', '05', '2025')

# 6. Named Groups
# - Named groups make regex easier to read.
# Syntax - (?P<name>pattern)
import re

text = "John 25"

match = re.search(r"(?P<name>\w+) (?P<age>\d+)", text)

print(match.group("name")) # John
print(match.group("age")) # 25

# 7. Lookahead
# - Checks what comes next without including it in the match.
# Positive Lookahead (?=...)
import re

text = "100USD"

print(re.findall(r"\d+(?=USD)", text)) # ['100']

# Negative Lookahead (?!...)
import re

text = "100USD 200INR"

print(re.findall(r"\d+(?!USD)", text)) # ['20']

# 8. Lookbehind
# - Checks what comes before the match.
# Positive Lookbehind (?<=...)
import re

text = "$500"

print(re.findall(r"(?<=\$)\d+", text)) # ['500']
# Negative Lookbehind (?<!...)
import re

text = "$500 600"

print(re.findall(r"(?<!\$)\d+", text)) # ['600']

# 9. match()
# - Matches only at the beginning of the string.
import re

text = "Python is awesome"

print(re.match("Python", text)) # <re.Match object>

# 10. search()
# - Searches the entire string.
import re

text = "I love Python"

print(re.search("Python", text)) # <re.Match object>

# 11. findall()
# - Returns all matches as a list.
import re

text = "123 abc 456"

print(re.findall(r"\d+", text)) # ['123', '456']

# 12. finditer()
# - Returns an iterator of match objects.
import re

text = "123 abc 456"

for match in re.finditer(r"\d+", text):
    print(match.group()) # 123 456

# 13. sub()
# - Replaces matching text.
import re

text = "Python is good"

result = re.sub("good", "awesome", text)

print(result) # Python is awesome

# Replace all digits:
import re

text = "A1 B2 C3"

print(re.sub(r"\d", "*", text)) # A* B* C*

# 14. split()
# - Splits a string using a regex pattern.
import re

text = "apple,banana;orange"

print(re.split(r"[,;]", text)) # ['apple', 'banana', 'orange']

# Most Important Interview Patterns
# \d+          # digits
# \w+          # words
# [a-z]+       # lowercase letters
# [A-Z]+       # uppercase letters
# [a-zA-Z]+    # letters only
# \s+          # spaces
# ^start       # starts with
# end$         # ends with
# .            # any character
# .*           # anything

# Email Validation
import re

email = "test@gmail.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

print(bool(re.match(pattern, email)))

# Mobile Number Validation
import re

mobile = "9876543210"

pattern = r"^[6-9]\d{9}$"

print(bool(re.match(pattern, mobile)))

# Extract Numbers
import re

text = "Price is 250 and tax is 50"

print(re.findall(r"\d+", text)) # ['250', '50']

# Summary
# re.match()     # Check beginning of string
# re.search()    # Find first match
# re.findall()   # Return all matches
# re.finditer()  # Iterator of matches
# re.sub()       # Replace text
# re.split()     # Split text
#
# \d             # Digit
# \w             # Word character
# \s             # Whitespace
#
# *              # 0 or more
# +              # 1 or more
# ?              # Optional
# {n,m}          # Range
#
# ()             # Group
# (?P<name>)     # Named group
# (?=...)        # Lookahead
# (?<=...)       # Lookbehind

# Practice Task: Extract all email IDs from:
text = "Contact: aman@gmail.com, support@yahoo.com, admin@company.org"
# Using:
re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)