# 18. File Handling in Python
# - File handling is used to store data permanently in files instead of keeping it only in program memory.

# 1. Opening Files
# Use open() to open a file.
# Syntax: file = open("filename.txt", "mode")
file = open("data.txt", "r")
print(file)
file.close()

# 2. Reading Files
# read(): Reads entire file.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
# readline(): Reads one line.
file = open("data.txt", "r")
print(file.readline())
print(file.readline())
file.close()
# readlines(): Returns list of lines.
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# 3. Writing Files
# Mode: "w"
# - Creates file if it doesn't exist.
# - Replaces existing content.
file = open("data.txt", "w")
file.write("Hello Python")
file.close()
# Output in file: Hello Python

# 4. Appending to Files
# Mode: "a"
# - Adds content at the end.
# - Does not delete old content.
file = open("data.txt", "a")
file.write("\nLearning File Handling")
file.close()

# 5. File Modes
# Mode -> Meaning
# "r" -> Read
# "w" -> Write
# "a" -> Append
# "x" -> Create file
# "r+" -> Read + Write
# "w+" -> Write + Read
# "a+" -> Append + Read
# "rb" -> Read binary
# "wb" -> Write binary
file = open("data.txt", "r")

# 6. with Statement
# - Automatically closes file.
with open("data.txt", "r") as file:
    data = file.read()
    print(data)
# No need for: file.close()

# 7. Context Managers
# - A context manager automatically manages resources.
with open("data.txt", "w") as f:
    f.write("Python")
# Benefits:
# - Auto close
# - Cleaner code
# - Prevents resource leaks

# Custom Context Manager:
class Demo:
    def __enter__(self):
        print("Opened")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closed")
with Demo():
    print("Working")
# Output:
# - Opened
# - Working
# - Closed

# 8. Text Files: Normal readable files such as: .txt, .csv, .json
with open("note.txt", "w") as file:
    file.write("Hello")

# 9. Binary Files: Stores data in binary format.
# Ex: .jpg, .png, .mp3, .pdf
# Write binary:
with open("image.jpg", "rb") as file:
    data = file.read()
# Copy file:
with open("image.jpg", "rb") as src:
    with open("copy.jpg", "wb") as dest:
        dest.write(src.read())

# 10. CSV Files: CSV = Comma Separated Values
# Example file:
# name,age
# Aman,25
# Rahul,26

# Reading CSV:
import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Output:
# ['name', 'age']
# ['Aman', '25']
# ['Rahul', '26']

# Writing CSV
import csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Aman", 25])

# 11. JSON Files: JSON = JavaScript Object Notation
# Python Dictionary
data = {
    "name": "Aman",
    "age": 25
}
# Write JSON
import json
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
# Output:
# {
#     "name": "Aman",
#     "age": 25
# }

# Read JSON
import json
with open("data.json", "r") as file:
    data = json.load(file)
print(data)
# Output: {'name': 'Aman', 'age': 25}

# 12. File Paths
# Relative Path:
open("data.txt")
# Current folder is searched.

# Absolute Path
# Windows:
open("C:\\Users\\Aman\\data.txt")
# or
open(r"C:\Users\Aman\data.txt")
# Linux
open("/home/aman/data.txt")

# 13. pathlib: Modern way to work with file paths.
from pathlib import Path
path = Path("data.txt")
print(path.exists())
print(path.name)
print(path.suffix)
# Create File
from pathlib import Path
path = Path("demo.txt")
path.touch()
# Create Folder
from pathlib import Path
Path("myfolder").mkdir(exist_ok=True)
# Join Paths
from pathlib import Path
path = Path("data") / "files" / "test.txt"
print(path)
# Output: data/files/test.txt

# Interview Questions
# Q1. Difference between w and a mode?
# - w -> overwrites file
# - a -> adds data at end

# Q2. Why use with?
# - Automatically closes file.

# Q3. Difference between read() and readline()?
# read()      -> whole file
# readline()  -> one line

# Q4. What is JSON? - A text format used to store and exchange data.

# Q5. Why use pathlib? - Provides an object-oriented and platform-independent way
# to handle file paths.

# Quick Revision
# open()          # Open file
# read()          # Read all data
# readline()      # One line
# readlines()     # List of lines
# write()         # Write data
# with            # Auto close file
# csv.reader()    # Read CSV
# csv.writer()    # Write CSV
# json.load()     # Read JSON
# json.dump()     # Write JSON
# Path()          # File path handling

# ✅ File Handling = Open → Read/Write → Close (or use with) → Work with Text, Binary, CSV, JSON, and Paths efficiently.

# ------------------------------------------- #
# 19. Modules (Python)
# 1. What is a Module?
# - A module is a Python file (.py) that contains code such as:
# Variables
# Functions
# Classes
# Statements
# - Modules help organize code and promote code reuse.
# math_utils.py
def add(a, b):
    return a + b
# - This file itself is a module named math_utils.

# 2. Creating Modules
# - Create a Python file and write reusable code inside it.
# greetings.py
def hello(name):
    print(f"Hello, {name}")
def bye(name):
    print(f"Goodbye, {name}")
# - Now this module can be used in another file.

# 3. import: Imports the entire module.
# main.py
import greetings
greetings.hello("Aman")
greetings.bye("Aman")
# Output:
# Hello, Aman
# Goodbye, Aman

# 4. from ... import
# - Imports specific items from a module.
from greetings import hello
hello("Aman")
# Import multiple items:
from greetings import hello, bye
hello("Aman")
bye("Aman")
# Import everything (not recommended):
from greetings import *
hello("Aman")

# 5. Aliases: Use as to give a shorter or custom name.
# Module Alias
import greetings as g
g.hello("Aman")
# Function Alias
from greetings import hello as h
h("Aman")
# Common example:
import numpy as np
import pandas as pd

# 6. __name__ : Every module has a special variable called __name__.
print(__name__)
# When file is run directly:
# test.py
print(__name__)
# Output:
# __main__

# When imported:
# main.py
import test
# Output:
test
# - __name__ tells Python how the file is being used.

# 7. __main__ : Used to execute code only when the file is run directly.
# greetings.py
def hello():
    print("Hello")
if __name__ == "__main__":
    hello()
# Run directly:
# python greetings.py
# Output: Hello

# Import from another file:
import greetings
# Output: # Nothing printed
# This is called the main guard.

# 8. Python Standard Library
# - Python comes with many built-in modules.
# Math
import math
print(math.sqrt(25)) # 5.0
# Random
import random
print(random.randint(1, 10))
# Datetime
from datetime import datetime
print(datetime.now())
# OS
import os
print(os.getcwd())
# Sys
import sys
print(sys.version)
# - Popular Standard Library Modules:
# math
# random
# datetime
# os
# sys
# json
# csv
# pathlib
# collections
# itertools

# 9. Module Search Path: When you import a module, Python searches in:
# 1. Current directory
# 2. Standard library directories
# 3. Installed packages (site-packages)
# 4. Directories listed in sys.path

# Example: import greetings
# Python searches these locations until it finds greetings.py.

# 10. sys.path: sys.path is a list of directories where Python looks for modules.
import sys
print(sys.path)
# Example Output:
# [
#  'D:\\Python',
#  'C:\\Python313\\Lib',
#  'C:\\Python313\\Lib\\site-packages'
# ]

# Add a path temporarily
import sys
sys.path.append("D:/my_modules")
# - Now Python can import modules from that folder.
import mymodule

# Quick Interview Questions
# Q1. What is a module?
# - A Python file containing reusable code.

# Q2. Difference between import and from ... import?
# import math
# math.sqrt(4)

# from math import sqrt
# sqrt(4)

# Q3. Why use aliases?
# - To shorten names and improve readability.
import numpy as np

# Q4. What is __name__?
# - A special variable indicating how a module is executed.

# Q5. What is the purpose of if __name__ == "__main__"?
# - To run code only when the file is executed directly.

# Q6. What is sys.path?
# - A list of directories Python searches for modules.

# Summary
# Import whole module
import module_name
# Import specific item
from module_name import function
# Alias
import module_name as mn
# Special variable
print(__name__)
# Main guard
if __name__ == "__main__":
    pass
# Search path
import sys
print(sys.path)

# ✅ Module = .py file
# ✅ import = import whole module
# ✅ from ... import = import specific items
# ✅ as = alias
# ✅ __name__ = module identifier
# ✅ __main__ = direct execution check
# ✅ sys.path = module search locations