# Dockerfile for a FastAPI application
# This Dockerfile sets up a containerized environment for a FastAPI application.
# It uses the official Python image, installs dependencies, and runs the FastAPI server.

# Use the official Python image as the base image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
