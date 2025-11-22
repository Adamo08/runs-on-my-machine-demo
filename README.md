# Runs on My Machine Demo

A simple Python application that demonstrates the classic "but it works on my machine" problem and how Docker solves it.

## The Problem

Ever heard "but it works on my machine"? This happens when code runs perfectly on one developer's machine but fails on another due to different:
- Python versions
- Operating systems
- Environment configurations

## The Solution: Docker

Docker packages the application with all its dependencies into a container, ensuring it runs consistently everywhere.

## Files

- `app.py` - Simple Python script that asks for user input (requires Python 3.10+ for pattern matching)
- `Dockerfile` - (Coming soon) Instructions to containerize the application

## Running Locally

```bash
python app.py
```

## Running with Docker

(Instructions will be added after creating the Dockerfile)

## Purpose

This repository demonstrates how Docker eliminates environment inconsistencies and makes applications truly portable.
