# 55. AI / Deep Learning
# AI and Deep Learning are among the most in-demand skills today, especially with the rise of ChatGPT, Copilot, Gemini, and other Generative AI tools.

# 1. Neural Networks
# A Neural Network is a machine learning model inspired by the human brain.

# Basic Structure
# Input Layer → Hidden Layer(s) → Output Layer

# Age → \
#       Hidden Layer → Salary Prediction
# Exp → /

# Components
# - Neurons (Nodes)
# - Weights
# - Bias
# - Activation Functions

# Common Activations:
# ReLU
# Sigmoid
# Tanh
# Softmax

import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1)
])

# 2. PyTorch
# PyTorch is a Deep Learning framework developed by Meta.
# Installation: pip install torch torchvision

# Tensor Example
import torch

x = torch.tensor([1, 2, 3])

print(x)

# Neural Network Example
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 1)
)

# Advantages
# Easy debugging
# Pythonic syntax
# Research friendly

# 3. TensorFlow
# - TensorFlow is Google's Deep Learning framework.
# Installation: pip install tensorflow
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse"
)

# TensorFlow vs PyTorch
# TensorFlow - PyTorch
# Production friendly - Research friendly
# Keras integration - Simpler debugging
# Strong deployment tools - More flexible

# 4. Transformers
# - Transformers power ChatGPT, Claude, Gemini, Copilot, etc.
# Traditional NLP: RNN → LSTM → GRU
# Modern NLP: Transformer

# Key Concept
# Self-Attention
# Example sentence: "The cat sat on the mat because it was tired."
# Transformer understands: it → cat

# Popular Models
# BERT
# GPT
# T5
# Llama
# Mistral

# 5. Embeddings
# - Embeddings convert text into numerical vectors.
# "dog" → [0.23, 1.45, -0.67]
# Similar meanings produce similar vectors.
# king ≈ queen
# dog ≈ puppy

# Use Cases
# Semantic Search
# Recommendation Systems
# RAG
# Clustering
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embedding = model.encode("Hello World")

# 6. LLMs (Large Language Models)
# LLMs are massive models trained on huge datasets.
# Examples:
# GPT
# Gemini
# Claude
# Llama
# Mistral

# Capabilities
# Chat
# Summarization
# Coding
# Translation
# Q&A
# Content generation

# Example Using OpenAI SDK:
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Explain Python"
)

print(response.output_text)

# 7. Hugging Face
# - GitHub of AI models.
# Website: https://huggingface.co
# Install: pip install transformers
# Load Model
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

print(
    generator("Hello AI")
)

# What You'll Find
# Datasets
# Models
# Spaces
# Inference APIs

# 8. Tokenization
# LLMs do not understand words.
# They understand Tokens.
# Example: "I love Python"
# May become: ["I", "love", "Py", "thon"]

# Example
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "gpt2"
)

tokens = tokenizer.tokenize(
    "Hello World"
)

print(tokens)
# Why Important?
# Context Window
# API Cost
# Performance

# 9. Fine-Tuning
# Fine-tuning means training a pre-trained model on your own data.
# Example:
# GPT Base Model
# ↓
# Company Documents
# ↓
# Custom AI Assistant

# Types
# Full Fine-Tuning
# Train all parameters.

# LoRA
# Train only small adapter layers.
# Popular because:
# - Faster
# - Cheaper
# - Less GPU requirement

# 10. RAG (Retrieval-Augmented Generation)
# - One of the most important AI concepts.
# Problem: LLM doesn't know company data
# Solution:
# Query
# ↓
# Vector Search
# ↓
# Relevant Documents
# ↓
# LLM
# ↓
# Answer

# Workflow
# Documents
# ↓
# Embeddings
# ↓
# Vector Database
# ↓
# Search
# ↓
# LLM

# Example Use Cases:
# - Company Chatbot
# - Knowledge Base
# - Document Search

# 11. Vector Databases
# - Store embeddings for semantic search.
# Popular Options:
# Pinecone
# Weaviate
# ChromaDB
# Qdrant
# Milvus
# FAISS
from langchain.vectorstores import FAISS
# Use Cases:
# RAG
# Similarity Search
# Recommendations

# 12. Prompt Engineering
# - Writing effective prompts to get better AI responses.
# Bad Prompt: Explain Python
# Better Prompt: Explain Python to a beginner. Include examples. Keep it under 200 words.

# Common Techniques

# Zero-Shot:
# Translate:
# Hello

# Few-Shot
# English: Hello
# French: Bonjour
#
# English: Good Morning
# French:

# Chain of Thought
# - Solve step by step.

# 13. AI APIs
# - Many companies provide AI through APIs.
# OpenAI
from openai import OpenAI
# Azure OpenAI
from openai import AzureOpenAI
# Google Gemini
import google.generativeai
# Anthropic Claude
import anthropic
# Typical Flow
# User Input
#       ↓
# API Request
#       ↓
# LLM
#       ↓
# Response

# Learning Path (Recommended Order)
# 1. Neural Networks
# 2. PyTorch
# 3. TensorFlow
# 4. Transformers
# 5. Tokenization
# 6. Embeddings
# 7. Hugging Face
# 8. LLMs
# 9. Prompt Engineering
# 10. Vector Databases
# 11. RAG
# 12. Fine-Tuning
# 13. AI APIs

# Mini Project Ideas
# Beginner
# Sentiment Analysis
# Spam Detector
# Image Classifier

# Intermediate
# Resume Analyzer
# AI Chatbot
# PDF Q&A System

# Advanced
# RAG Chatbot
# Multi-Agent AI System
# AI Code Assistant
# Custom Fine-Tuned LLM
# Enterprise Knowledge Assistant