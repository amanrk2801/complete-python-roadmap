# 11. Dictionaries: A dictionary is a collection of data stored in key:value pairs.
student = {
    "name": "Aman",
    "age": 22,
    "city": "Nagpur"
}
# Keys must be unique.
# Values can be of any data type.
# Dictionaries are mutable (can be modified).

# 1. Creating Dictionaries
# Method 1
student = {
    "name": "Aman",
    "age": 22
}
print(student) # {'name': 'Aman', 'age': 22}
# Method 2
student = dict(name="Aman", age=22)
print(student) # {'name': 'Aman', 'age': 22}
# Empty Dictionary
data = {}
print(type(data)) # <class 'dict'>

# 2. Keys and Values
student = {
    "name": "Aman",
    "age": 22,
    "city": "Nagpur"
}
# Here:
# "name", "age", "city" → Keys
# "Aman", 22, "Nagpur" → Values

# 3. Accessing Values
# Using Key
student = {
    "name": "Aman",
    "age": 22
}
print(student["name"]) # Aman
# Using get()
print(student.get("age")) # 22
# Difference
# print(student["salary"]) # KeyError: 'salary'
print(student.get("salary")) # None

# 4. Adding / Updating Entries
# Add New Entry
student = {"name": "Aman"}
student["age"] = 22
print(student) # {'name': 'Aman', 'age': 22}
# Update Existing Value
student["age"] = 23
print(student) # {'name': 'Aman', 'age': 23}

# 5. Removing Entries
# del
student = {
    "name": "Aman",
    "age": 22
}
del student["age"]
print(student) # {'name': 'Aman'}
# pop()
student = {
    "name": "Aman",
    "age": 22
}
student.pop("age")
print(student) # {'name': 'Aman'}
# clear()
student.clear()
print(student) # {}

# 6. Nested Dictionaries: Dictionary inside another dictionary.
students = {
    "s1": {
        "name": "Aman",
        "age": 22
    },
    "s2": {
        "name": "Rahul",
        "age": 23
    }
}
print(students["s2"]["name"]) # Rahul

# 7. Dictionary Methods
# keys(): Returns all keys.
student = {
    "name": "Aman",
    "age": 22
}
print(student.keys()) # dict_keys(['name', 'age'])
# values(): Returns all values.
print(student.values()) # dict_values(['Aman', 22])
# items(): Returns key-value pairs.
print(student.items()) # dict_items([('name', 'Aman'), ('age', 22)])
# Loop Through Dictionary
for key, value in student.items():
    print(key, value) # name Aman, age 22
# get(): Safely access values.
print(student.get("name")) # Aman
print(student.get("salary")) # None
# update(): Adds or updates multiple entries.
student = {
    "name": "Aman"
}
student.update({
    "age": 22,
    "city": "Nagpur"
})
print(student) # {'name': 'Aman', 'age': 22, 'city': 'Nagpur'}
# pop(): Removes a specific key.
student = {
    "name": "Aman",
    "age": 22
}
age = student.pop("age")
print(age) # 22
print(student) # {'name': 'Aman'}
# popitem(): Removes the last inserted item.
student = {
    "name": "Aman",
    "age": 22
}
item = student.popitem()
print(item) # ('age', 22)
print(student) # {'name': 'Aman'}
# setdefault(): Returns value if key exists, otherwise creates key.
student = {
    "name": "Aman"
}
student.setdefault("age", 22)
print(student) # {'name': 'Aman', 'age': 22}
# If key already exists:
student.setdefault("age", 30)
print(student) # {'name': 'Aman', 'age': 22}
# clear(): Removes everything.
student = {
    "name": "Aman",
    "age": 22
}
student.clear()
print(student) # {}
# copy(): Creates a shallow copy.
student = {
    "name": "Aman",
    "age": 22
}
new_student = student.copy()
print(new_student) # {'name': 'Aman', 'age': 22}

# 8. Dictionary Unpacking
student = {
    "name": "Aman",
    "age": 22
}
# print(**student) # TypeError: print() got an unexpected keyword argument 'name'
# Correct usage:
d1 = {
    "name": "Aman",
    "age": 22
}
d2 = {
    "city": "Nagpur"
}
result = {**d1, **d2}
print(result) # {'name': 'Aman', 'age': 22, 'city': 'Nagpur'}

# 9. Dictionary Comprehensions: Just like list comprehensions.
squares = {x: x*x for x in range(1, 6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
even_squares = {
    x: x*x
    for x in range(1, 11)
    if x % 2 == 0
}
print(even_squares) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Interview Questions
# Q1. Difference between get() and []?
# d["key"] -> Raises KeyError if key not found.
# d.get("key") -> Returns None (or default value).

# Q2. Can a dictionary have duplicate keys?
d = {
    "a": 10,
    "a": 20
}
print(d) # {'a': 20} : ✅ Last value overwrites previous value.

# Q3. Are dictionaries mutable? - Yes
d = {"name": "Aman"}
d["age"] = 22 # Dictionary changes successfully.

# Practice Programs
# 1. Count Frequency of Elements
arr = [1, 2, 2, 3, 3, 3]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq) # {1: 1, 2: 2, 3: 3}
# 2. Student Marks Dictionary
marks = {
    "Aman": 85,
    "Rahul": 90,
    "Riya": 88
}
for name, mark in marks.items():
    print(name, mark) # Aman 85, Rahul 90, Riya 88
# 3. Find Highest Value
marks = {
    "Aman": 85,
    "Rahul": 90,
    "Riya": 88
}
print(max(marks.values())) # 90

# Summary
# Dictionary = {key: value}
# Important methods:
# - keys()
# - values()
# - items()
# - get()
# - update()
# - pop()
# - popitem()
# - setdefault()
# - clear()
# - copy()

# ------------------------------------------------- #
# Comprehensions in Python: Comprehensions are a short and Pythonic way to create lists, sets, and dictionaries from existing iterables.
# General syntax: [expression for item in iterable]
# Instead of writing loops with append(), we can write concise code using comprehensions.

# 1. List Comprehension: Creates a new list.
# Traditional Way
numbers = [1, 2, 3, 4, 5]
result = []
for x in numbers:
    result.append(x * 2)
print(result) # [2, 4, 6, 8, 10]
# Using List Comprehension
numbers = [1, 2, 3, 4, 5]
result = [x * 2 for x in numbers]
print(result) # [2, 4, 6, 8, 10]
# Example: Squares
squares = [x ** 2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# 2. Set Comprehension: Creates a set.
# Syntax: {expression for item in iterable}
numbers = [1, 2, 2, 3, 3, 4]
result = {x * 2 for x in numbers}
print(result) # {8, 2, 4, 6}
# Notice that duplicate values are automatically removed because a set stores unique values only.

# Example: Unique Squares
numbers = [1, 2, 2, 3]
squares = {x ** 2 for x in numbers}
print(squares) # {1, 4, 9}

# 3. Dictionary Comprehension: Creates a dictionary.
# Syntax: {key:value for item in iterable}

# Example:
numbers = [1, 2, 3, 4, 5]
result = {x: x * x for x in numbers}
print(result) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example: Number and Cube
cubes = {x: x ** 3 for x in range(1, 6)}
print(cubes) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# 4. Conditional Comprehensions: You can add conditions using if.
# Example: Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens) # [2, 4, 6]

# Example: Odd Numbers
odds = [x for x in numbers if x % 2 != 0]
print(odds) # [1, 3, 5]

# if-else Inside Comprehension
# Example:
numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(result) # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Syntax:
# [value_if_true if condition else value_if_false
#  for item in iterable]

# 5. Nested Comprehensions: A comprehension inside another comprehension.
# Traditional Nested Loop
pairs = []
for i in range(1, 4):
    for j in range(1, 4):
        pairs.append((i, j))
print(pairs) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# Nested Comprehension
pairs = [(i, j)
         for i in range(1, 4)
         for j in range(1, 4)]
print(pairs) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# Nested List Flattening
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Convert into a single list:
flat = [num for row in matrix for num in row]
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Comprehension Cheat Sheet
# List
[x for x in iterable]

# List with condition
[x for x in iterable if condition]

# List with if-else
[value1 if condition else value2 for x in iterable]

# Set
{x for x in iterable}

# Dictionary
{x: x*x for x in iterable}

# Nested
[(i, j) for i in range(3) for j in range(3)]

# Interview Questions
# Q1. Why use comprehensions?
# - Less code
# - More readable
# - Usually faster than traditional loops

# Q2. Which comprehension types exist?
# - List comprehension
# - Set comprehension
# - Dictionary comprehension
# (There is no dedicated tuple comprehension. Using parentheses creates a generator expression.)

gen = (x * 2 for x in range(5))

# Q3. When should you avoid comprehensions?
# Avoid when the logic becomes too complex:
# Hard to read
result = [x**2 if x%2==0 else x**3
          for x in range(20)
          if x > 5]
# In such cases, a normal loop is clearer.

# Practice Questions
# 1. Create a list of squares from 1 to 10.
# 2. Create a list of even numbers from 1 to 20.
# 3. Create a set of cubes from 1 to 10.
# 4. Create a dictionary {number: square} for 1 to 5.
# 5. Convert a nested list into a single list using comprehension.
# 6. Create a list containing "Pass" if marks ≥ 35 else "Fail".

# Mastering comprehensions is important because they're used heavily in real Python projects, coding interviews, pandas, Django, Flask, and automation scripts.