### 6. Loops in Python: Loops are used to execute a block of code repeatedly.
# 1. for Loop: A for loop is used to iterate over a sequence (list, tuple, string, dictionary, range, etc.).
for i in [1, 2, 3, 4, 5]:
    print(i)
# range(): range() generates a sequence of numbers.
# range(start, stop, step)
for i in range(5):
    print(i) # 0 1 2 3 4
for i in range(1, 6):
    print(i) # 1 2 3 4 5
for i in range(0, 10, 2):
    print(i) # 0 2 4 6 8
# Iterating Lists
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit) # Apple Banana Mango
# Using Index
fruits = ["Apple", "Banana", "Mango"]
for i in range(len(fruits)):
    print(i, fruits[i]) # 0 Apple, 1 Banana, 2 Mango
# Iterating Strings
name = "AMAN"
for ch in name:
    print(ch) # A M A N

# Iterating Dictionaries
student = {
    "name": "Aman",
    "age": 25
}
# Keys
for key in student:
    print(key) # name, age
# Values
for value in student.values():
    print(value) # Aman, 25
# Key-Value Pairs
for key, value in student.items():
    print(key, value) # name Aman, age 25
# Nested Loops: A loop inside another loop.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# Pattern Example
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
# 2. while Loop: A while loop runs as long as a condition is True.
# Basic while
i = 1
while i <= 5:
    print(i)
    i += 1
# Conditions
number = 10
while number > 0:
    print(number)
    number -= 1
print("Done")
# Infinite Loops: A loop whose condition never becomes False.
while True:
    print("Hello")
# ⚠️ This will run forever until manually stopped (Ctrl + C).
# Example with break:
while True:
    name = input("Enter name: ")
    if name == "exit":
        break
    print(name)
# 3. Loop Control Statements
# break: Stops the loop immediately.
for i in range(1, 11):
    if i == 5:
        break
    print(i) # 1 2 3 4
# continue: Skips the current iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i) # 1 2 4 5
# pass: Placeholder statement. It does nothing.
for i in range(5):
    pass
print("Loop completed")
# Note: Useful when writing code structure first:
if True:
    pass
# Loop else: The else block executes when a loop finishes normally.
# With for
for i in range(5):
    print(i)
else:
    print("Loop completed")
# With break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
# NOTE: else is not executed because the loop ended using break.

# Interview Questions
# Q1. Difference between for and while?
# for
# - Used when iterations are known
# - Iterates over sequence
# - Less chance of infinite loop
# while
# - Used when iterations are unknown
# - Runs based on condition
# - More chance of infinite loop

# Q2. Why use range(n + 1)?: Because the stopping value is excluded.
for i in range(1, 6):
    print(i) # 1 2 3 4 5
# Note: To include 5, we use 6.

# Q3. What is the difference between break and continue?
# break      -> Ends the loop
# continue   -> Skips current iteration

# Practice Programs
# 1. Print 1 to 10
for i in range(1, 11):
    print(i)
# 2. Print Even Numbers
for i in range(2, 21, 2):
    print(i)
# 3. Sum of 1 to N
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)
# 4. Multiplication Table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
# 5. Count Divisible by 3
n = int(input("Enter N: "))
count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1
print(count)
# 6. Reverse Countdown
n = 10
while n > 0:
    print(n)
    n -= 1

# Note: Master these loop concepts before moving to Functions, because loops and functions are the foundation of almost every Python program. 🚀
# --------------------------------------------- #
# loops: for and while
# 1. for loop
## Suppose you want to print numbers 1 to 5
for i in range(1,6): # The ending value is excluded.
    print(i) # 1 2 3 4 5

for i in range(5): # When only one number is provided, Python starts from 0.
    print(i) # 0 1 2 3 4

## You can also specify a step
for i in range(2, 11, 2): # start: 2, stop: 11, step: 2
    print(i) # 2 4 6 8 10

print("Exercises")
# 1. Print numbers 1 to 10
for i in range(1,11):
    print(i) # 1 to 10

# 2. Print even numbers from 1 to 20
for i in range(2,21,2):
    print(i)

# 3. Print the multiplication table
for i in range(1, 11):
    print(f"5 * {i} = {5 * i}") # f-string

# dynamic table:
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 4. Calculate the sum from 1 to N
num = int(input("Enter a number: "))
total = 0 # Accumulator
for i in range(1, num+1):
    total += i
print("Sum:", total)

# 5. Count how many numbers are divisible by 3
num = int(input("Enter a number: "))
count = 0 # Counter
for i in range(1, num+1):
    if i % 3 == 0:
        count += 1
print("Count=",count)

# 2. while loop: A while loop repeats as long as a condition is true.
i = 1 # initialization
while i <= 5: # condition
    print(i)
    i += 1 # update

# Note: The update is important.
# If you write:
# i = 1
# while i <= 5:
#     print(i)
# the loop never ends because i always remains 1.
# That's called an infinite loop.

# for vs while
# Use for when you generally know what you're iterating over:
for i in range(1, 11):
    print(i)

# Use while when repetition depends primarily on a condition:
password = ""
while password != "Aman123":
    password = input("Enter password: ")
print("Login successful")

