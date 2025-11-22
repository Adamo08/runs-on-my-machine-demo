# Use an official Python runtime as base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy application file(s) to container
COPY app.py .

# Command to run when container starts
CMD ["python", "app.py"]
