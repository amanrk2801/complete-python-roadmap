# 31. JSON in Python
# JSON (JavaScript Object Notation) is a lightweight format used to store and exchange data. APIs, configuration files, and web applications commonly use JSON.

# 1. JSON Structure
# JSON consists of:
# - Objects → {} (similar to Python dictionaries)
# - Arrays → [] (similar to Python lists)
# - Key-value pairs

# JSON Example
# {
#     "name": "Aman",
#     "age": 22,
#     "skills": ["Python", "SQL"],
#     "is_employee": true
# }

# Equivalent Python Dictionary
data = {
    "name": "Aman",
    "age": 22,
    "skills": ["Python", "SQL"],
    "is_employee": True
}

# 2. json.loads()
# - Converts a JSON string → Python object.
# Syntax: json.loads(json_string)

import json

json_data = '{"name":"Aman","age":22}'

python_data = json.loads(json_data)

print(python_data) # {'name': 'Aman', 'age': 22}
print(type(python_data)) # <class 'dict'>

# 3. json.dumps()
# Converts a Python object → JSON string.
# Syntax: json.dumps(python_object)
import json

data = {
    "name": "Aman",
    "age": 22
}

json_data = json.dumps(data)

print(json_data) # {"name": "Aman", "age": 22}
print(type(json_data)) # <class 'str'>

# Pretty JSON
import json

data = {
    "name": "Aman",
    "age": 22
}

print(json.dumps(data, indent=4))
# Output
# {
#     "name": "Aman",
#     "age": 22
# }

# 4. json.load()
# - Reads JSON data from a file and converts it to a Python object.
# sample.json
# {
#     "name": "Aman",
#     "age": 22
# }
import json

with open("sample.json", "r") as file:
    data = json.load(file)

print(data) # {'name': 'Aman', 'age': 22}

# 5. json.dump()
# - Writes a Python object into a JSON file.
import json

data = {
    "name": "Aman",
    "age": 22
}

with open("sample.json", "w") as file:
    json.dump(data, file)

# Pretty Writing
import json

with open("sample.json", "w") as file:
    json.dump(data, file, indent=4)
# Generated file:
# {
#     "name": "Aman",
#     "age": 22
# }

# 6. Python ↔ JSON Conversion
# Python - JSON
# dict -> object
# list -> array
# tuple -> array
# str -> string
# int -> number
# float -> number
# True -> true
# False -> false
# None -> null

import json

data = {
    "name": "Aman",
    "active": True,
    "salary": None
}

json_data = json.dumps(data)
print(json_data) # {"name": "Aman", "active": true, "salary": null}

# 7. Nested JSON
# - JSON can contain objects inside objects and arrays inside objects.
{
    "name": "Aman",
    "address": {
        "city": "Nagpur",
        "state": "Maharashtra"
    },
    "skills": [
        "Python",
        "SQL",
        "Django"
    ]
}
# Accessing Nested Data
import json

data = '''
{
    "name":"Aman",
    "address":{
        "city":"Nagpur",
        "state":"Maharashtra"
    }
}
'''

obj = json.loads(data)

print(obj["address"]["city"]) # Nagpur

# Nested List Example
data = {
    "students": [
        {"name": "Aman", "marks": 90},
        {"name": "Rahul", "marks": 85}
    ]
}

print(data["students"][1]["name"]) # Rahul

# 8. API Responses
# - Most APIs return data in JSON format.
# Example API Response
{
    "id": 101,
    "name": "Laptop",
    "price": 50000
}
# Reading API Response
import requests

response = requests.get(
    "https://api.example.com/product"
)

data = response.json()

print(data["name"]) # Laptop
print(data["price"]) # 50000

# Function - Input - Output
# json.loads() - JSON String - Python Object
# json.load() - JSON File - Python Object

# Remember
s = '{"name":"Aman"}'
json.loads(s)      # string
with open("data.json") as f:
    json.load(f)   # file

# dumps vs dump
# Function - Purpose
# json.dumps() - Python object → JSON string
# json.dump() - Python object → JSON file

# Remember
json.dumps(data)
# Returns:
'{"name":"Aman"}'
json.dump(data, file)
# Writes directly to a file.

# Interview Questions
# Q1. Difference between loads() and load()?
# loads() reads JSON from a string.
# load() reads JSON from a file.

# Q2. Difference between dumps() and dump()?
# dumps() converts Python object to JSON string.
# dump() writes Python object into a JSON file

# Q3. What is JSON?
# A lightweight data exchange format consisting of key-value pairs and arrays.

# Q4. JSON equivalent of Python None?
# None → null

# Q5. JSON equivalent of Python True and False?
# True  → true
# False → false

# Practice Program
import json

student = {
    "name": "Aman",
    "age": 22,
    "skills": ["Python", "SQL"]
}

# Python -> JSON string
json_data = json.dumps(student, indent=4)
print(json_data)

# JSON string -> Python
python_data = json.loads(json_data)
print(python_data["skills"][0])

# Output:
# {
#     "name": "Aman",
#     "age": 22,
#     "skills": [
#         "Python",
#         "SQL"
#     ]
# }
# Python

# This covers JSON completely for Python interviews and real-world API usage.

# --------------------------------------- #
# 32. CSV (Comma-Separated Values)
# CSV files are used to store tabular data (rows and columns). Python provides the built-in csv module to work with CSV files easily.
# import csv

# 1. Reading CSV
# Suppose students.csv contains:
# Name,Age,City
# John,20,New York
# Alice,22,London
# Bob,21,Paris

# Read the file:
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
# Output
# ['Name', 'Age', 'City']
# ['John', '20', 'New York']
# ['Alice', '22', 'London']
# ['Bob', '21', 'Paris']

# 2. Writing CSV
import csv

data = [
    ["Name", "Age", "City"],
    ["John", 20, "New York"],
    ["Alice", 22, "London"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)
# Generated file:
# Name,Age,City
# John,20,New York
# Alice,22,London

# 3. csv.reader
# - csv.reader() reads a CSV file row by row.
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
# Access specific columns:
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip header

    for row in reader:
        print("Name:", row[0])
        print("Age:", row[1])
# Output:
# Name: John
# Age: 20
#
# Name: Alice
# Age: 22

# 4. csv.writer
# csv.writer() writes data into a CSV file.
# Write One Row
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 20])
# Write Multiple Rows
import csv

rows = [
    ["Name", "Age"],
    ["John", 20],
    ["Alice", 22],
    ["Bob", 21]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(rows)
# 5. DictReader
# - DictReader reads each row as a dictionary.
# CSV File:
# Name,Age,City
# John,20,New York
# Alice,22,London
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
# Output:
# {'Name': 'John', 'Age': '20', 'City': 'New York'}
# {'Name': 'Alice', 'Age': '22', 'City': 'London'}

# Access values by column name:
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], row["Age"])
# Output
# John 20
# Alice 22

# Advantage: No need to remember column indexes.
# ❌ row[1]
# ✅ row["Age"]

# 6. DictWriter
# - DictWriter writes dictionaries to a CSV file.
import csv

data = [
    {"Name": "John", "Age": 20, "City": "New York"},
    {"Name": "Alice", "Age": 22, "City": "London"}
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
# Generated CSV:
# Name,Age,City
# John,20,New York
# Alice,22,London

# Writing One Dictionary
import csv

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "Name": "John",
        "Age": 20
    })

# Interview Questions
# Q1. Why use newline="" while opening a CSV file for writing?
# with open("data.csv", "w", newline="") as file:
# It prevents extra blank lines from being added between rows.

# Q2. Difference between reader and DictReader?
# reader
['John', '20', 'NY']
# Access using index:
row[0]
# DictReader
{'Name': 'John', 'Age': '20', 'City': 'NY'}
# Access using key:
row["Name"]

# Q3. Difference between writerow() and writerows()?
# writerow()
writer.writerow(["John", 20])
# Writes one row.
# writerows()
writer.writerows(rows)
# Writes multiple rows.

# Practice Programs
# 1. Read and Print CSV
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# 2. Print Only Names
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"])

# 3. Create Employee CSV
import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Salary"])
    writer.writerow([1, "John", 50000])
    writer.writerow([2, "Alice", 60000])

# 4. Calculate Total Salary
import csv

total = 0

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["Salary"])

print("Total Salary:", total) # Total Salary: 110000

# Quick Revision
import csv

# Read
csv.reader(file)

# Write
csv.writer(file)

# Read as dictionary
csv.DictReader(file)

# Write dictionary
csv.DictWriter(file, fieldnames=fields)

# Write header
writer.writeheader()

# One row
writer.writerow(row)

# Multiple rows
writer.writerows(rows)

# Remember:
#
# reader → List of values
# writer → Write lists
# DictReader → Read dictionaries
# DictWriter → Write dictionaries
# newline="" → Avoid extra blank lines in CSV files.