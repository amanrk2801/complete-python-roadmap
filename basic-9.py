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
