# 8. Lists: A list is an ordered, mutable (changeable) collection that can store multiple values of different data types.
numbers = [10, 20, 30, 40]
names = ["Aman", "Rahul", "Priya"]
mixed = [1, "Hello", 3.14, True]
# 1. Creating Lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "mango"]
# 2. Indexing: Lists use zero-based indexing.
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # mango
# 3. Slicing
# Syntax: list[start:end:step]
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30]
print(numbers[2:]) # [30, 40, 50]
print(numbers[::-1]) # [50, 40, 30, 20, 10]
# 4. Updating Elements
numbers = [10, 20, 30]
numbers[1] = 99
print(numbers) # [10, 99, 30]
# 5. Adding Elements
# append(): Adds one item at the end.
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits) # ['apple', 'banana', 'mango']
# extend(): Adds multiple items.
fruits = ["apple"]
fruits.extend(["banana", "mango"])
print(fruits) # ['apple', 'banana', 'mango']
# insert(): Adds item at a specific position.
fruits = ["apple", "mango"]
fruits.insert(1, "banana")
print(fruits) # ['apple', 'banana', 'mango']

# 6. Removing Elements
# remove(): Removes first matching value.
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers) # [10, 30, 20]
# pop(): Removes element by index and returns it.
numbers = [10, 20, 30]
value = numbers.pop()
print(value) # 30
print(numbers) # [10, 20]
# clear(): Removes all elements.
numbers = [1, 2, 3]
numbers.clear()
print(numbers) # []
# 7. Nested Lists: A list inside another list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0]) # [1, 2, 3]
print(matrix[1][2]) # 6
# 8. List Methods
# index(): Returns position of element.
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana")) # 1
# count(): Counts occurrences.
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10)) # 3
# sort(): Sorts list permanently.
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers) # [1, 2, 5, 8]
# Descending order:
numbers.sort(reverse=True)
print(numbers) # [8, 5, 2, 1]
# reverse(): Reverses the list.
numbers = [1, 2, 3]
numbers.reverse()
print(numbers) # [3, 2, 1]
# copy(): Creates a shallow copy.
a = [1, 2, 3]
b = a.copy()
print(b) # [1, 2, 3]

# 9. List Unpacking: Extract values into variables.
numbers = [10, 20, 30]
a, b, c = numbers
print(a) # 10
print(b) # 20
print(c) # 30
# Using *:
numbers = [10, 20, 30, 40, 50]
a, *b, c = numbers
print(a) # 10
print(b) # [20, 30, 40]
print(c) # 50

# 10. List Concatenation: Combining lists.
list1 = [1, 2]
list2 = [3, 4]
result = list1 + list2
print(result) # [1, 2, 3, 4]
# Using extend():
list1 = [1, 2]
list1.extend([3, 4])
print(list1) # [1, 2, 3, 4]
# 11. List Comparison
a = [1, 2, 3]
b = [1, 2, 3]
c = [3, 2, 1]
print(a == b) # True
print(a == c) # False
# Equality vs Identity
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Same values : True
print(a is b)  # Same object? : False

# 12. Shallow Copy: A shallow copy copies only the outer list. Nested objects are still shared.
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 100
print(original) # [[100, 2], [3, 4]]
print(shallow) # [[100, 2], [3, 4]]
# ⚠️ Both change because inner lists are shared.

# 13. Deep Copy: A deep copy creates completely independent copies.
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 100
print(original) # [[1, 2], [3, 4]]
print(deep) # [[100, 2], [3, 4]]
# ✅ Original remains unchanged.

# Interview Questions
# Difference between append() and extend()
a = [1, 2]
a.append([3, 4])
print(a) # [1, 2, [3, 4]]
a = [1, 2]
a.extend([3, 4])
print(a) # [1, 2, 3, 4]

# Difference between remove() and pop()
a.remove(20)  # Removes by value
a.pop(1)      # Removes by index

# Difference between shallow and deep copy
# - Shallow copy: shares nested objects.
# - Deep copy: creates fully independent copies.

# Time Complexity Cheat Sheet
# Operation  -> Complexity
# Access by index -> O(1)
# Update by index -> O(1)
# Append -> O(1)
# Insert -> O(n)
# Remove -> O(n)
# Search (in) -> O(n)
# Sort -> O(n log n)

# These list concepts and methods cover about 90% of Python list questions asked in interviews and beginner-to-intermediate programming tasks. 🚀

