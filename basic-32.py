# 56. DevOps with Python
# DevOps focuses on automating software development, deployment, infrastructure, and monitoring. Python is one of the most popular languages for DevOps because it is simple and has powerful automation libraries.

# 1. Docker
# Docker packages applications and their dependencies into containers.
# Why Docker?
# - Consistent environments
# - Easy deployment
# - Application isolation
# - Scalability

# Dockerfile Example
# FROM python:3.12
#
# WORKDIR /app
#
# COPY requirements.txt .
#
# RUN pip install -r requirements.txt
#
# COPY . .
#
# CMD ["python", "app.py"]

# Build and Run
# docker build -t myapp .
#
# docker run myapp

# Python Example
# print("Running inside Docker")

# 2. CI/CD
# CI (Continuous Integration)
# Automatically:
# - Build code
# - Run tests
# - Check quality
# CD (Continuous Delivery/Deployment)
# Automatically:
# - Deploy application
# - Release updates

# Flow:
# Developer
#     ↓
# Git Push
#     ↓
# CI Pipeline
#     ↓
# Tests
#     ↓
# Build
#     ↓
# Deploy

# 3. GitHub Actions
# GitHub's CI/CD platform.
# Project Structure:
# .github/
# └── workflows/
#     └── python.yml

# Example Workflow
# name: Python CI
#
# on: [push]
#
# jobs:
#   build:
#     runs-on: ubuntu-latest
#
#     steps:
#       - uses: actions/checkout@v4
#
#       - name: Setup Python
#         uses: actions/setup-python@v5
#
#       - name: Install Dependencies
#         run: |
#           pip install -r requirements.txt
#
#       - name: Run Tests
#         run: |
#           pytest

# Benefits:
# Automated testing
# Automated deployment
# Code quality checks

# 4. AWS SDK (Boto3)
# - Boto3 is the Python SDK for AWS.
# Install: pip install boto3
# Connect to S3
import boto3

s3 = boto3.client("s3")

response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])

# Upload File
import boto3

s3 = boto3.client("s3")

s3.upload_file(
    "report.pdf",
    "mybucket",
    "report.pdf"
)

# Launch EC2
import boto3

ec2 = boto3.resource("ec2")

instance = ec2.create_instances(
    ImageId="ami-123456",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro"
)

# 5. Cloud Automation
# - Automate cloud operations.
# Tasks:
# - Create servers
# - Create storage
# - Backup systems
# - Scale resources
import boto3

ec2 = boto3.client("ec2")

ec2.start_instances(
    InstanceIds=["i-123456"]
)
# Automated nightly task:
import schedule
import time

def backup():
    print("Taking backup")

schedule.every().day.at("01:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)

# 6. Infrastructure Automation
# Infrastructure as Code (IaC)
# Tools:
# - Terraform
# - Ansible
# - AWS CloudFormation
# - Pulumi
# Python + Ansible
import subprocess

subprocess.run(
    ["ansible-playbook", "deploy.yml"]
)

# Using Terraform
import subprocess

subprocess.run(["terraform", "init"])
subprocess.run(["terraform", "apply", "-auto-approve"])

# Benefits:
# Repeatability
# Version control
# Less manual work

# 7. Monitoring
# Monitoring tracks:
# - CPU
# - Memory
# - Network
# - Application health
# Using psutil: pip install psutil
import psutil

print("CPU:", psutil.cpu_percent())

print("Memory:", psutil.virtual_memory().percent)

# Health Check Script
import requests

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    print("Healthy")
else:
    print("Down")

# Popular Tools:
# Prometheus
# Grafana
# Datadog
# New Relic

# 8. Logging
# Logging helps track application behavior.
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log"
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Something failed")

# Log Levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# Structured Logging:
import logging

logger = logging.getLogger(__name__)

logger.info(
    "User logged in",
    extra={"user_id": 123}
)

# 9. Environment Management
# Avoid hardcoding secrets.
# Environment Variables
import os

db_host = os.getenv("DB_HOST")

print(db_host)

# Set Variables
# Linux: export DB_HOST=localhost
# Windows: set DB_HOST=localhost

# Using .env
# Install: pip install python-dotenv
# Create:
# DB_HOST=localhost
# DB_USER=admin
# DB_PASSWORD=secret

# Read:
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")

print(host)

# Real DevOps Project Example
# A Python web app:
# Flask App
#     ↓
# Docker Container
#     ↓
# GitHub Actions
#     ↓
# Run Tests
#     ↓
# Build Image
#     ↓
# Push to Docker Hub
#     ↓
# Deploy on AWS EC2
#     ↓
# Monitor with Grafana
#     ↓
# Logs stored centrally

# Interview Questions
# 1. What is Docker?
# A containerization platform used to package applications with dependencies.

# 2. Difference between CI and CD?
# CI = Continuous Integration
# CD = Continuous Delivery/Deployment

# 3. What is Boto3?
# Python SDK to interact with AWS services.

# 4. Why environment variables?
# To securely store configuration and secrets.

# 5. What is Infrastructure as Code?
# Managing infrastructure through code instead of manual setup.

# 6. What is monitoring?
# Tracking system and application health.

# 7. Why logging is important?
# For debugging, auditing, and troubleshooting production issues.

# ------------------------------------------------ #