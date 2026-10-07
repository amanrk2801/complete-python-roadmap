# 9. Tuples in Python
# A tuple is an ordered collection of elements. It is similar to a list, but tuples are immutable, meaning their values cannot be changed after creation.
# 1. Creating Tuples
# - Tuples are created using parentheses ().
t = (1, 2, 3)
print(t) # (1, 2, 3)
# Single-element tuple
t = (5,)
print(type(t)) # <class 'tuple'>
# ⚠️ Without the comma, Python treats it as an integer:
t = (5)
print(type(t)) # <class 'int'>

# 2. Indexing
# Like lists, tuples use zero-based indexing.
colors = ("red", "green", "blue")
print(colors[0]) # red
print(colors[1]) # green
print(colors[-1]) # blue

# 3. Slicing: We can extract a portion of a tuple.
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4]) # (20, 30, 40)
print(numbers[:3]) # (10, 20, 30)
print(numbers[2:]) # (30, 40, 50)

# 4. Tuple Unpacking: Assign tuple values directly to variables.
person = ("Aman", 25, "India")
name, age, country = person
print(name) # Aman
print(age) # 25
print(country) # India
# Using *
numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers
print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5

# 5. Nested Tuples: A tuple can contain other tuples.
data = (
    ("Aman", 25),
    ("Rahul", 24),
    ("Priya", 23)
)
print(data[0]) # ('Aman', 25)
print(data[0][1]) # 25

# 6. Tuple Methods: Tuples have only two built-in methods because they are immutable.
# count(): Counts occurrences of a value.
nums = (1, 2, 3, 2, 2)
print(nums.count(2)) # 3
# index(): Returns the first index of a value.
nums = (10, 20, 30, 20)
print(nums.index(20)) # 1

# 7. Named Tuples: Named tuples provide field names instead of indexes.
from collections import namedtuple
Student = namedtuple("Student", ["name", "age"])
s1 = Student("Aman", 25)
print(s1.name) # Aman
print(s1.age) # 25
# Benefits: More readable, Faster than dictionaries, Immutable

# 8. Tuple vs List
# Feature -> Tuple -> List
# Syntax -> (1,2,3) -> [1,2,3]
# Mutable -> ❌ No -> ✅ Yes
# Ordered -> ✅ Yes -> ✅ Yes
# Faster -> ✅ Usually -> ❌ Slightly slower
# Methods -> Few -> Many
# Hashable -> ✅ (if elements are hashable) -> ❌

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list[0] = 100      # Works
# my_tuple[0] = 100   # Error

# 9. Immutability: Once a tuple is created, its elements cannot be modified.
t = (10, 20, 30)
# t[0] = 100 # TypeError: 'tuple' object does not support item assignment

# Why Use Immutable Objects?
# - Safer data storage
# - Faster execution
# - Can be used as dictionary keys
# - Useful for fixed data

coordinates = (10, 20)
location = {
    coordinates: "Office"
}
print(location) # {(10, 20): 'Office'}

# Interview Questions
# Q1. Difference between tuple and list?
# - List is mutable.
# - Tuple is immutable.
# - Tuple is generally faster and uses less memory.

# Q2. Why use a tuple instead of a list?
# Use a tuple when data should not change, such as:
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# Q3. How do you convert a tuple to a list?
t = (1, 2, 3)
lst = list(t)
print(lst) # [1, 2, 3]

# Q4. How do you convert a list to a tuple?
lst = [1, 2, 3]
t = tuple(lst)
print(t) # (1, 2, 3)

# Q5. Can a tuple contain mutable objects?
# - Yes.
t = ([1, 2], [3, 4])
t[0].append(5)
print(t) # ([1, 2, 5], [3, 4])
# Even though the tuple itself is immutable, the list inside it can still be modified.

# Quick Summary
# Tuple = Ordered + Immutable
# Created using ()
# Supports indexing and slicing
# Can be nested
# Only two methods: count(), index()
# Useful for fixed data
# NamedTuple provides named fields

#-----------------------------------------------------------------#

# 10. Sets in Python
# A Set is an unordered collection of unique elements. Sets do not allow duplicate values.
s = {1, 2, 3, 4}
print(s) # {1, 2, 3, 4}
# 1. Creating Sets
# Using Curly Braces
numbers = {1, 2, 3, 4}
print(numbers)
# Using set()
numbers = set([1, 2, 3, 4])
print(numbers)
# Empty Set
s = set()      # Correct
print(type(s))
# ⚠️ {} creates an empty dictionary, not a set.
d = {}
print(type(d)) # <class 'dict'>
