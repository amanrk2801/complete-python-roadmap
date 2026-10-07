'''
# 1. What is Python?
Ans: Python is a High Level, Interpreted programming language
known for simple syntax and a large ecosystem.
'''
# 2. First Python Program
print("Hello, Shri Krishna")

# 3. Variables: name, age, salary
name = "Aman"
age = 29
salary = 70000
print(name, age, salary)

# 4. Data Types:
# Basic
# 1. int (Integer): Stores whole numbers (positive, negative, or zero).
age = 25 # <class 'int'>
# 2. float (Floating Point Number): Stores numbers with decimal points.
pi = 3.14159 # <class 'float'>
# 3. complex (Complex Number): Used for mathematical calculations involving imaginary numbers.
num = 3 + 4j # 3 = real part, 4j = imaginary part
print(num) # (3+4j)
print(type(num)) # <class 'complex'>
# 4. bool (Boolean): Stores only two values
is_logged_in = True # <class 'bool'>
# 5. str (String): Stores text.
name = "Aman" # <class 'str'>
# Note: Strings can contain: Letters, Numbers, Symbols
# 6. None (NoneType): Represents "no value" or "nothing".
user = None # <class 'NoneType'>
if user is None:
    print("No user found")
# Remember: int, float, complex, bool, str, and NoneType are Python's basic built-in data types.

# Collection Types: Collection types are used to store multiple values in a single variable.
# 1.List (list)
# - Ordered collection
# - Mutable (can be changed)
# - Allows duplicate values
# - Uses []
fruits = ["apple", "banana", "apple"]
print(fruits) # ['apple', 'banana', 'apple']
# ✅ Add, remove, update items possible.

# 2.Tuple (tuple)
# Ordered collection
# Immutable (cannot be changed after creation)
# Allows duplicates
# Uses ()
numbers = (10, 20, 30, 10)
print(numbers) # (10, 20, 30, 10)
# ✅ Faster than lists for fixed data.

# 3.Set (set)
# Unordered collection
# Mutable
# Does not allow duplicates
# Uses {}
nums = {1, 2, 3, 2, 1}
print(nums) # {1, 2, 3}
# ✅ Useful for removing duplicates.

# 4.Frozen Set (frozenset)
# Unordered collection
# Immutable version of a set
# No duplicates allowed
fs = frozenset([1, 2, 3])
print(fs) # frozenset({1, 2, 3})
# ❌ Cannot add or remove elements.

# 5.Dictionary (dict)
# Stores data as key-value pairs
# Mutable
# Keys must be unique
# Uses {key: value}
student = {
    "name": "Aman",
    "age": 25
}
print(student["name"]) # Aman
# ✅ Most commonly used data structure in Python.
# Dictionaries maintain insertion order in modern Python versions.

# 6.Range (range)
# Generates a sequence of numbers
# Often used with loops
r = range(1, 6)
for i in r:
    print(i) # 1,2,3,4,5
# ✅ Memory efficient because it generates numbers on demand.

# Easy Memory Trick
# List → Changeable collection
# Tuple → Fixed collection
# Set → Unique values only
# Frozenset → Fixed set
# Dict → Key → Value mapping
# Range → Number sequence generator

# Binary Types in Python
# Binary types are used to store binary data (data in the form of bytes instead of normal text).
# 1. bytes
# - Immutable (cannot be changed after creation).
# - Each value must be between 0 and 255.
data = bytes([65, 66, 67])
print(data) # b'ABC'
print(data[0]) # 65
# ✅ Used for reading files, network communication, images, etc.

# 2. bytearray
# - Mutable version of bytes.
# - You can modify its contents.
data = bytearray([65, 66, 67])
data[0] = 90
print(data) # bytearray(b'ZBC')
# ✅ Useful when binary data needs to be changed.

# 3. memoryview
# Provides a view of binary data without copying it.
# Faster and more memory-efficient for large data.
data = bytes([10, 20, 30, 40])
view = memoryview(data)
print(view[0]) # 10
print(view[1]) # 20
# ✅ Used in high-performance applications that process large binary data.

# Comparison
# bytes      -> Immutable binary data
# bytearray  -> Mutable binary data
# memoryview -> View/access binary data without copying

# Easy Analogy
# bytes = Printed book (read only)
# bytearray = Notebook (can edit)
# memoryview = Looking at a book through a window (view without making another copy)

# bytes = immutable, bytearray = mutable, memoryview = no-copy view of binary data.

# 5. Taking User Input
DOB = input("Enter your DOB: ")
print(DOB)
print(type(DOB)) # <class 'str'> Note: input() always returns a string.

# 6. Type Conversion
age = int(input("Enter age: ")) # Explicit Type Conversion: int()
print("Your age is: ",age)
print(type(age)) # <class 'int'>

int("10")      # String -> Integer
float("10.5")  # String -> Float
str(100)       # Integer -> String
bool(1)        # Integer -> Boolean

# Note: Python treats certain value as False
# 0, 0.0, ""(empty string), [](empty list), {}(empty dictionary), None.
# Everything else is generally True.

# 7. Basic Operators
## Arithmetic
a = 10
b = 5
print(a+b) # addition
print(a-b) # substraction
print(a*b) # multiplication
print(a/b) # division
print(a//b) # floor division
print(a%b) # remainder
print(a**b) # power

# let's combine everything
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello,",name)
print("You are", age, "years old")

# 1. Problem: Create variables
name = "Aman"
age = 29
city = "Pune"
print("My name is",name)
print("I am", age, "years old")
print("I live in",city)

# 2. Problem: Take two numbers from the user and print
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 3. Problem: Take a person's age and point their age after 10 years
age = int(input("Enter your age: "))
print("After 10 years",age+10)

# 4. Problem: Take length and width and calculate the area of a rectangle
length = 10
width = 10
area = length*width
print(area)

# 5. Problem: Take a number and determine whether it is even or odd
num = int(input("Enter a number: "))
print(["Even", "Odd"][num%2])
# num % 2 = 0 → ["Even", "Odd"][0] → Even
# num % 2 = 1 → ["Even", "Odd"][1] → Odd

# Very important Python concepts
# 1. Mutable vs Immutable
# Mutable: Objects whose value can be changed after creation.
# Examples: list, dict, set, bytearray
nums = [1, 2, 3]
nums.append(4)
print(nums) # [1, 2, 3, 4]
# The same object is modified.

# Immutable: Objects whose value cannot be changed after creation.
# Examples: int, float, bool, str, tuple, frozenset, bytes
name = "Aman"
name = name + " Kumar"
print(name)
# A new string object is created instead of modifying the old one.

# Quick Memory Trick
# ✅ Mutable = Can Modify
# ❌ Immutable = Cannot Modify

# 2. Hashable vs Unhashable
# A hashable object has a fixed hash value and can be used as:
# - Dictionary keys
# - Set elements

# Hashable
hash("Aman")
hash(10)
hash((1, 2, 3))
# Examples: int, float, str, tuple (if all elements are hashable), frozenset, bool
student = {
    "name": "Aman"
}
# Here "name" is hashable.

# Unhashable
hash([1, 2, 3]) # TypeError: unhashable type: 'list'
# Examples: list, dict, set
# Why?
# Because their contents can change, so their hash value would change.

# 3. Identity vs Equality
# Equality (==)
# Checks whether values are equal.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
# Because values are same.

# Identity (is)
# Checks whether two variables refer to the same object in memory.
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False
# Different objects.

# 4. id()
# Returns the memory identity of an object.
# Syntax: id(object)
x = 100
print(id(x)) # 1402143245
# (The number varies on every system.)

# 5. is Operator
# Checks identity.
a = [1, 2, 3]
b = a
print(a is b) # True
# Both point to same object.

a = [1, 2]
b = [1, 2]
print(a is b) # False
# Different objects.

# 6. == Operator
# Checks equality of values.
a = [1, 2]
b = [1, 2]
print(a == b) # True
# Values are equal.

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
print(a is b) # False
# ==  → Compare values
# is  → Compare memory locations (identity)

# Interview Question
x = None
print(x == None) # True
print(x is None) # True

# But Pythonic way is:
if x is None:
    print("Value is None")
# ✅ Use is None
# ❌ Avoid == None

# Mutable     -> Can change after creation
# Immutable   -> Cannot change after creation
#
# Hashable    -> Can be hashed, used as dict key
# Unhashable  -> Cannot be hashed
#
# ==          -> Compares values
# is          -> Compares identity
#
# id(obj)     -> Returns object's identity
#
# a == b      -> Same content?
# a is b      -> Same object?

# One-line Rule
#
# Use '==' when comparing values, use 'is' when checking whether two variables refer to the same object (especially None). ✅