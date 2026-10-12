# 15. Lambda Functions in Python
# A lambda function is a small anonymous (nameless) function that can have any number of arguments but only one expression.

# 1. Lambda Syntax
# Normal Function
def square(x):
    return x * x
print(square(5)) # 25

# Lambda Function
square = lambda x: x * x
print(square(5)) # 25

# Syntax: lambda arguments: expression
add = lambda a, b: a + b
print(add(10, 20)) # 30

# 2. Lambda with map()
# map() applies a function to every element of an iterable.

# Without Lambda
def square(x):
    return x * x
numbers = [1, 2, 3, 4]
result = list(map(square, numbers))
print(result) # [1, 4, 9, 16]

# With Lambda
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * x, numbers))
print(result) # [1, 4, 9, 16]

# Double Every Number
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result) # [2, 4, 6, 8]

# 3. Lambda with filter()
# filter() keeps only elements for which the condition is True.
# Find Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result) # [2, 4, 6]
# Find Odd Numbers
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result) # [1, 3, 5]
# Numbers Greater Than 10
numbers = [5, 12, 8, 15, 20]
result = list(filter(lambda x: x > 10, numbers))
print(result) # [12, 15, 20]

# 4. Lambda with sorted()
# sorted() can sort data using a custom key.
# Sort a List of Tuples by Age
students = [
    ("Aman", 22),
    ("Rahul", 20),
    ("Priya", 25)
]
result = sorted(students, key=lambda x: x[1])
print(result) # [('Rahul', 20), ('Aman', 22), ('Priya', 25)]

# Sort by Name
students = [
    ("Aman", 22),
    ("Rahul", 20),
    ("Priya", 25)
]
result = sorted(students, key=lambda x: x[0])
print(result) # [('Aman', 22), ('Priya', 25), ('Rahul', 20)]

# Sort in Descending Order
numbers = [5, 1, 8, 2, 9]
result = sorted(numbers, key=lambda x: x, reverse=True)
print(result) # [9, 8, 5, 2, 1]

# 5. Lambda vs Normal Function
# Normal Function
def multiply(a, b):
    return a * b
print(multiply(3, 4))

# Lambda Function
multiply = lambda a, b: a * b
print(multiply(3, 4))

# Difference
# Normal Function
# - Created using def
# - Has a function name
# - Can contain multiple statements
# - More readable for complex logic
# - Can use return

# Lambda Function
# - Created using lambda
# - Usually anonymous
# - Only one expression
# - Best for short operations
# - No return keyword needed

# When to Use Lambda?
#
# ✅ Short one-line functions
#
# ✅ With map(), filter(), sorted()
#
# ✅ Temporary functions
#
# ❌ Large or complex logic
#
# ❌ Multiple statements

# Interview Questions
# Q1. Can a lambda function have multiple arguments?
add = lambda a, b, c: a + b + c
print(add(1, 2, 3)) # 6

# Q2. Can lambda contain loops?
# ❌ No. Lambda can contain only a single expression.

# Q3. Does lambda need return?
# ❌ No. -> square = lambda x: x * x
# The expression result is returned automatically.

# Q4. Which is better: lambda or normal function?
# - Use lambda for short operations.
# - Use normal functions (def) for real-world applications because they are more readable and maintainable.

# Quick Revision
# Lambda
# square = lambda x: x*x
#
# # map
# list(map(lambda x: x*2, [1,2,3]))
#
# # filter
# list(filter(lambda x: x%2==0, [1,2,3,4]))
#
# # sorted
# sorted([(1,3),(2,1),(3,2)], key=lambda x:x[1])

# Rule: If the function is only 1 line and used once, lambda is a good choice. Otherwise, prefer def.

# ------------------------------------------------- #

# Functional Programming in Python
# Functional Programming (FP) is a programming style where functions are treated as first-class objects and computations are performed using functions rather than changing program state.

# 1. First-class Functions
# - In Python, functions are treated like any other object.

# ✅ Can be:
#
# Assigned to variables
# Passed as arguments
# Returned from other functions
# Stored in collections

def greet():
    return "Hello"
say_hello = greet
print(say_hello())

# 2. Higher-order Functions
# A function that:
# - Takes another function as an argument
# - Returns a function
def apply(func, value):
    return func(value)
def square(x):
    return x * x
print(apply(square, 5))

# 3. map() - Applies a function to every item in an iterable.
# Syntax - map(function, iterable)
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

# 4. filter() - Filters elements based on a condition.
# Syntax - filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# 5. reduce() - Reduces an iterable to a single value.
# Import - from functools import reduce
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)
# Working
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10

# 6. zip() - Combines multiple iterables element-wise.
names = ["Aman", "Rahul", "Vijay"]
marks = [90, 85, 92]
result = list(zip(names, marks))
print(result)

# 7. enumerate() - Provides index along with values.
fruits = ["Apple", "Banana", "Mango"]
for index, value in enumerate(fruits):
    print(index, value)

# Start from 1
for index, value in enumerate(fruits, start=1):
    print(index, value)

# 8. any() - Returns True if at least one element is true.
numbers = [0, 0, 5, 0]
print(any(numbers)) # Because 5 is truthy.
print(any([False, False, False])) # False

# 9. all() - Returns True if all elements are true.
numbers = [1, 2, 3]
print(all(numbers)) # True
print(all([1, 2, 0])) # False: Because 0 is falsy.

# 10. min() - Returns the smallest element.
numbers = [10, 5, 20, 2]
print(min(numbers)) # 2
# With strings
names = ["Aman", "Rahul", "Vijay"]
print(min(names)) # Aman - (Alphabetically smallest)

# 11. max() - Returns the largest element.
numbers = [10, 5, 20, 2]
print(max(numbers)) # 20

# 12. sum() - Returns the total sum.
numbers = [1, 2, 3, 4]
print(sum(numbers)) # 10
# With start value
print(sum([1, 2, 3], 100)) # 106

# 13. sorted() - Returns a new sorted list.
numbers = [5, 1, 8, 3]
print(sorted(numbers)) # [1, 3, 5, 8]
# Descending Order
print(sorted(numbers, reverse=True)) # [8, 5, 3, 1]
# Sort by Length
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=len)) # ['kiwi', 'apple', 'banana']

# Interview Questions
# Q1. Difference between map() and filter()?
# map()
# - Transforms every element.
# - Output size remains same.
map(lambda x: x * 2, [1,2,3])
# filter()
# - Selects elements based on condition.
# - Output size may decrease.
filter(lambda x: x % 2 == 0, [1,2,3])

# Q2. Difference between any() and all()?
any([0, 0, 1])    # True
all([0, 0, 1])    # False
# any() → At least one True
# all() → All must be True

# Q3. Why use lambda with map() and filter()?
# Because lambda allows creating small anonymous functions inline.
list(map(lambda x: x * x, [1,2,3])) # [1, 4, 9]

# Quick Revision
# map()        # Transform data
# filter()     # Filter data
# reduce()     # Reduce to single value
# zip()        # Combine iterables
# enumerate()  # Index + value
# any()        # At least one True
# all()        # All True
# min()        # Smallest element
# max()        # Largest element
# sum()        # Total
# sorted()     # Sort iterable

# Real-world flow:
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, evens)
result = reduce(lambda x, y: x + y, squares)
print(result) # 56
# (2² + 4² + 6² = 4 + 16 + 36 = 56)
