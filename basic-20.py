# 35. Web Development
#
# Web Development in Python is mainly done using Flask, Django, and FastAPI. All three are popular but used for different purposes.
#
# Flask → Lightweight and flexible
# Django → Full-featured framework
# FastAPI → Modern, high-performance APIs

# 1. Flask
# Flask is a micro web framework. It is simple, easy to learn, and perfect for small-to-medium projects.
# Installation: pip install flask
# Basic Flask App
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

app.run(debug=True)

# Routes: Routes define URLs.
@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

# Request Methods
from flask import request

@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        return "POST Request"
    return "GET Request"

# Request Data
# Query Parameters
@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Searching for {name}"

# URL: /search?name=Aman

# Form Data
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return username

# Responses
from flask import jsonify

@app.route("/api")
def api():
    return jsonify({
        "name": "Aman",
        "age": 22
    })

# Output:
# {
#   "name": "Aman",
#   "age": 22
# }

# Templates: Flask uses Jinja2 templates.
# templates/index.html
# <h1>Hello {{ name }}</h1>

# app.py
from flask import render_template

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Aman"
    )

# Forms
# <form method="POST">
#     <input type="text" name="username">
#     <button>Submit</button>
# </form>

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        return request.form["username"]
    return render_template("form.html")

# REST API Example
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop"}
]

@app.route("/products")
def get_products():
    return jsonify(products)

# 2. Django
# - Django is a full-stack framework with built-in authentication, ORM, admin panel, and security features.
# Installation: pip install django
# Create Project: django-admin startproject myproject
# Run Server: python manage.py runserver

# Project Structure
# myproject/
# │
# ├── manage.py
# ├── myproject/
# │     ├── settings.py
# │     ├── urls.py
# │     ├── wsgi.py
# │     └── asgi.py

# Apps
# - Create an app: python manage.py startapp blog
# Structure:
# blog/
# ├── models.py
# ├── views.py
# ├── admin.py
# ├── urls.py
# └── tests.py

# Models: Models define database tables.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
# Migration:
# python manage.py makemigrations
# python manage.py migrate

# Views
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")

# URLs
# urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path("", home),
]

# Templates
# home.html
# <h1>Welcome {{ name }}</h1>
# views.py
from django.shortcuts import render

def home(request):
    return render(
        request,
        "home.html",
        {"name": "Aman"}
    )

# ORM
# Create
Product.objects.create(
    name="Laptop",
    price=50000
)
# Read
Product.objects.all()
# Filter
Product.objects.filter(price__gt=1000)
# Update
product = Product.objects.get(id=1)
product.price = 60000
product.save()
# Delete
product.delete()

# Admin Panel
# Create admin user: python manage.py createsuperuser
# Register model:
from django.contrib import admin
from .models import Product

admin.site.register(Product)
# Admin URL: http://127.0.0.1:8000/admin/

# Authentication
# Login
from django.contrib.auth import authenticate

user = authenticate(
    username="admin",
    password="123"
)
# Logout
from django.contrib.auth import logout

logout(request)
# Current User
request.user

# 3. FastAPI
# - FastAPI is designed for building fast, modern APIs with automatic validation and documentation.
# Installation: pip install fastapi uvicorn
# Run Application: uvicorn main:app --reload

# Basic FastAPI App
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

# Routes
@app.get("/users")
def get_users():
    return ["Aman", "Rahul"]
@app.post("/users")
def create_user():
    return {"status": "created"}

# Pydantic Models
# Used for request validation.
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Validation
@app.post("/user")
def create_user(user: User):
    return user
# Request:
{
  "name": "Aman",
  "age": 22
}
# Invalid age type automatically raises an error.

# Dependency Injection
from fastapi import Depends

def get_db():
    return "Database"

@app.get("/")
def home(db=Depends(get_db)):
    return {"db": db}

# Async APIs
@app.get("/data")
async def get_data():
    return {"message": "Async API"}

# Why Async?
# Handles many requests simultaneously
# Better performance
# Ideal for APIs

# OpenAPI / Swagger
# - Automatic API documentation.
# After running: http://127.0.0.1:8000/docs
# Swagger UI opens automatically.
# Alternative: http://127.0.0.1:8000/redoc

# REST Service Example
from fastapi import FastAPI

app = FastAPI()

products = []

@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return product

@app.get("/products")
def get_products():
    return products

# Flask vs Django vs FastAPI
# Feature - Flask - Django - FastAPI
# Learning Curve - Easy - Medium - Easy
# Performance - Good - Good - Excellent
# API Development - Good - Good - Excellent
# Built-in Features - Few - Many - Moderate
# ORM Included - No - Yes - No
# Admin Panel - No - Yes - No
# Best for - Small Apps - Large Projects - APIs & Microservices

# Interview Question
# Which framework should I choose?
#
# Flask → Small projects, learning web development.
# Django → Full-fledged web applications with authentication, admin, ORM.
# FastAPI → High-performance REST APIs, microservices, and modern backend development.