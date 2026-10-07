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

# 2. Adding and Removing Elements
# Adding Elements
# add()
s = {1, 2, 3}
s.add(4)
print(s) # {1, 2, 3, 4}

# update()
# Add multiple elements.
s = {1, 2}
s.update([3, 4, 5])
print(s) # {1, 2, 3, 4, 5}

# Removing Elements
# remove()
s = {1, 2, 3}
s.remove(2)
print(s) # {1, 3}
# ⚠️ Throws an error if the element is not present.
# s.remove(10)

# discard()
s = {1, 2, 3}
s.discard(10)
print(s) # {1, 2, 3}: No error occurs.

# pop(): Removes a random element.
s = {1, 2, 3}
print(s.pop())

# clear()
s = {1, 2, 3}
s.clear()
print(s) # set()

# 3. Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Union (|): Combines all unique elements.
print(A | B) # {1, 2, 3, 4, 5, 6}
# OR
print(A.union(B)) # {1, 2, 3, 4, 5, 6}
# Intersection (&): Common elements.
print(A & B) # {3, 4}
# OR
print(A.intersection(B)) # {3, 4}
# Difference (-): Elements in first set but not in second.
print(A - B) # {1, 2}
# OR
print(A.difference(B)) # {1, 2}
# Symmetric Difference (^): Elements present in exactly one set.
print(A ^ B) # {1, 2, 5, 6}
# OR
print(A.symmetric_difference(B)) # {1, 2, 5, 6}

# 4. Subsets: A set is a subset if all its elements exist in another set.
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B)) # True

# 5. Supersets: A set is a superset if it contains all elements of another set.
A = {1, 2, 3, 4}
B = {1, 2}
print(A.issuperset(B)) # True

# 6. Disjoint Sets: Disjoint sets have no common elements.
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B)) # True

# 7. Set Comprehensions: Similar to list comprehensions.
# Squares
squares = {x * x for x in range(1, 6)}
print(squares) # {1, 4, 9, 16, 25}
# Even Numbers
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens) # {2, 4, 6, 8, 10}

# 8. Frozenset: A frozenset is an immutable version of a set.
# ✅ Cannot add or remove elements.
fs = frozenset([1, 2, 3, 4])
print(fs) # frozenset({1, 2, 3, 4})
# Valid Operations
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])
print(A | B) # frozenset({1, 2, 3, 4, 5})
print(A & B) # frozenset({3})
# Invalid Operations
fs = frozenset([1, 2, 3])
# fs.add(4) # AttributeError
# Because frozensets cannot be modified.

# Important Set Methods
# s.add(x)
# s.update(iterable)
# s.remove(x)
# s.discard(x)
# s.pop()
# s.clear()
#
# s.union(other)
# s.intersection(other)
# s.difference(other)
# s.symmetric_difference(other)
#
# s.issubset(other)
# s.issuperset(other)
# s.isdisjoint(other)

# Interview Questions
# Q1. Why are sets faster for searching than lists?
# Sets use hashing, so lookup is approximately O(1), while lists require O(n) search.

# Q2. Can a set contain duplicate values?
# No.
s = {1, 1, 2, 2, 3}
print(s) # {1, 2, 3}

# Q3. Can a set contain a list?
# No, because lists are mutable and unhashable.
# s = {[1, 2, 3]} # TypeError

# Q4. Can a set contain tuples?
# Yes, because tuples are immutable and hashable.
s = {(1, 2), (3, 4)}
print(s) # {(1, 2), (3, 4)}

# Memory Trick
# Union (|) → Combine everything
# Intersection (&) → Common elements
# Difference (-) → Remove common elements from first set
# Symmetric Difference (^) → Keep uncommon elements only
# Subset → Smaller inside bigger
# Superset → Bigger contains smaller
# Disjoint → No common elements
# Frozenset → Read-only set ✅