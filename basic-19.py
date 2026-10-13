# 34. APIs (Application Programming Interfaces)
# - APIs are one of the most important topics in Python because they allow your application to communicate with other applications and services.

# 1. What is an API?
# - API (Application Programming Interface) is a set of rules that allows two applications to communicate.
# Example: Your Python application wants weather data.
# Python App ---> API ---> Weather Server ---> JSON
# Instead of accessing the database directly, your application requests data through an API.
# Real examples:
# Google Maps API
# GitHub API
# OpenWeather API
# Stripe API
# PayPal API

# 2. HTTP
# - HTTP (HyperText Transfer Protocol) is the protocol used for communication between clients and servers.
# Request Flow
# Client (Browser/Python) -> HTTP -> Server
# Example: GET https://api.example.com/users

# 3. GET
# - Used to retrieve data.
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.json())
# Output:
# [
#     {
#         "id": 1,
#         "name": "Leanne Graham"
#     }
# ]

# 4. POST
# - Used to create new data.
import requests

data = {
    "name": "Aman",
    "age": 25
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.json())

# 5. PUT
# - Used to replace/update entire resource.
import requests

data = {
    "name": "Aman",
    "age": 26
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=data
)

print(response.json())

# 6. PATCH
# - Used to partially update data.
response = requests.patch(
    "https://jsonplaceholder.typicode.com/users/1",
    json={"age": 26}
)

print(response.json())
# Difference:
# PUT   -> Update entire object
# PATCH -> Update specific fields

# 7. DELETE
# Used to remove data.
response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)

# 8. HTTP Status Codes
# 1xx - Informational : 100 Continue
# 2xx - Success : 200 OK, 201 Created, 204 No Content
# 3xx - Redirection : 301 Moved Permanently, 302 Found
# 4xx - Client Errors : 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
# 5xx - Server Errors : 500 Internal Server Error, 503 Service Unavailable

# Example:
if response.status_code == 200:
    print("Success")

# 9. Headers
# - Headers provide additional information with requests.
headers = {
    "User-Agent": "Python-App",
    "Accept": "application/json"
}

response = requests.get(
    "https://api.example.com/users",
    headers=headers
)
# Common Headers:
# Authorization
# Content-Type
# Accept
# User-Agent

# 10. Query Parameters
# - Used to send filters in URL.
# /users?page=2&limit=10
params = {
    "page": 2,
    "limit": 10
}

response = requests.get(
    "https://api.example.com/users",
    params=params
)

# Generated URL:
# - https://api.example.com/users?page=2&limit=10

# 11. Request Body
# Data sent with POST, PUT, PATCH requests.
data = {
    "name": "Aman",
    "email": "aman@gmail.com"
}

response = requests.post(
    url,
    json=data
)

# Body:
# {
#     "name": "Aman",
#     "email": "aman@gmail.com"
# }

# 12. JSON
# - Most APIs communicate using JSON.
# JSON
{
    "name": "Aman",
    "age": 25,
    "skills": ["Python", "Django"]
}
# Python Dict
data = {
    "name": "Aman",
    "age": 25,
    "skills": ["Python", "Django"]
}
# Convert:
import json

json_string = json.dumps(data)
python_dict = json.loads(json_string)

# 13. Authentication
# - Authentication verifies who you are.
# Common methods:
# Username/Password
# API Keys
# JWT Tokens
# OAuth
headers = {
    "Authorization": "Bearer TOKEN"
}

# 14. API Keys
# - Many APIs provide an API Key.
# API_KEY = "abc123"
# Header Method
headers = {
    "x-api-key": API_KEY
}
# Query Parameter Method
params = {
    "api_key": API_KEY
}

# 15. OAuth Basics
# - OAuth lets users grant access without sharing passwords.
# Flow
# User -> Login -> OAuth Provider(Google/GitHub) -> Access Token -> Application
# Authorization: Bearer ACCESS_TOKEN
# Common OAuth Providers:
# Google
# GitHub
# Facebook
# Microsoft

# Python: requests
# Most popular HTTP library.
# Installation: pip install requests
# GET Request
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response.status_code)
print(response.json())
# POST Request
import requests

data = {
    "title": "Python",
    "body": "Learning APIs"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.json())
# Error Handling
import requests

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.json())

except requests.exceptions.RequestException as e:
    print("Error:", e)

# Python: httpx
# - Modern alternative to requests.
# Installation: pip install httpx
# GET Request
import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response.json())
# Async Request
import asyncio
import httpx

async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )
        print(response.json())

asyncio.run(get_data())

# requests vs httpx
# Feature - requests - httpx
# Easy to use - ✅ - ✅
# Synchronous - ✅ - ✅
# Asynchronous - ❌ - ✅
# HTTP/2 - ❌ - ✅
# Modern - ❌ - ✅

# Interview Questions
# Q1. What is an API?
# - A mechanism that allows applications to communicate with each other.

# Q2. Difference between GET and POST?
# GET -> Fetch data
# POST -> Create data

# Q3. Difference between PUT and PATCH?
# PUT -> Replace entire resource
# PATCH -> Partial update

# Q4. What is JSON?
# - A lightweight data-interchange format used by APIs.

# Q5. What is an API Key?
# - A unique key used to identify and authorize API requests.

# Q6. What does Status Code 404 mean?
# - Resource Not Found

# Q7. What does Status Code 401 mean?
# Unauthorized
# Authentication required

# Q8. Why use httpx over requests?
# - Async support
# - HTTP/2 support
# - Better modern architecture

# Mini Project: Public API Client
import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Name:", data["name"])
    print("Followers:", data["followers"])
    print("Public Repos:", data["public_repos"])

else:
    print("Error:", response.status_code)