# 1. What is Python?
#
# Python is a high-level, interpreted, and easy-to-learn programming language created by Guido van Rossum in 1991.
#
# Features
# Simple syntax
# Easy to read and write
# Platform independent
# Large community support
# Used in:
#   Web Development
#   Data Science
#   AI/ML
#   Automation
#   CyberSecurity

print("Hello World")

# 2. Python Installation
# Windows
# 1. Download Python from python.org
# 2. Run installer
# 3. Check ✅ "Add Python to PATH"
# 4. Click Install

# python --version

# 3. Python Interpreter
# The interpreter reads and executes Python code line by line.

print("Hello")

# Unlike C/C++, Python does not require compilation before execution.

# 4. IDE vs Editor
# Editor
# Provides: Used only for writing code.
# Examples: VS Code, Sublime, Text, Notepad++

# IDE
# Provides: Code editor, Debugger, Terminal, Auto-completion
# Examples: PyCharm, Spyder, Jupyter Notebook

# 5. Running Python Scripts
# Create file: app.py
# Write: print("Hello Python")
# Run: python app.py

# 6. REPL
# Read → Evaluate → Print → Loop
# Start REPL: python
# Used for quick testing.

# 7. Comments
# Comments are ignored by Python.
# Single-line Comment
# This is a comment
print("Hello")

# Multi-line Comment
"""
This is
multi-line comment
"""

# 8. Indentation
# Python uses spaces instead of braces {}.
if True:
    print("Hello")

# 9. Python Syntax
# Syntax means rules for writing code.
name = "Aman"
print(name)
# Rules:
# Case-sensitive
# Proper indentation
# Parentheses required in functions

# 10. PEP 8
# PEP 8 is Python's style guide.
# Variable names
# ✅ student_name = "Aman"
# ❌ StudentName = "Aman"

# 11. input()
# Takes input from user.
name = input("Enter Name: ")
print(name)
age = input("Enter Age: ")
print(type(age)) # <class 'str'>
# input() always returns a string.

# 12. Variables
# Variables store values.
name = "Aman"
age = 25
salary = 50000
print(name, age, salary)

# 13. Constants
# Python has no true constants.
# Convention:
PI = 3.14
MAX_SIZE = 100
# Writing in CAPITAL letters means "do not change this value".

# 14. Naming Conventions
# Variable
first_name = "Aman"
# Function
def calculate_total():
    pass
# Class
class Student:
    pass
# Rules:
# Cannot start with number
# No spaces
# Case-sensitive
# ✅ Valid: name, user_name, _age
# ❌ Invalid: 2name, user name, class

# 15. Multiple Assignment
# Assign multiple values at once.
a, b, c = 10, 20, 30
print(a, b, c)

# 16. Dynamic Typing
# Python automatically determines data type.
x = 10
print(type(x)) # <class 'int'>
x = "Hello"
print(type(x)) # <class 'str'>
# No need to declare data types explicitly.

# 17. Type Checking with type()
name = "Aman"
print(type(name)) # <class 'str'>

# 18. Type Conversion / Type Casting
# Converting one data type into another.
# String → Integer
num = int("10")
print(num) # 10
# String → Float
price = float("99.9")
print(price) # 99.9
# Integer → Float
num = 10
print(float(num)) # 10.0

int()   # Whole number
float() # Decimal
str()   # Text
bool()  # True/False

# Quick Interview Questions
# 1. What does input() return?: String (str)
# 2. What is REPL?: Read-Evaluate-Print-Loop
# 3. What is PEP 8?: Python coding style guide
# 4. What is Dynamic Typing?: Variable type can change automatically.
# 5. Difference between int() and float()?: int() → whole number, float() → decimal number.
# 6. Why use int(input())?: Because input() returns a string and must be converted for calculations.