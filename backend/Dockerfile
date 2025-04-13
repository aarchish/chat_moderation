# Dockerfile for a Django application
# This Dockerfile sets up a containerized environment for a Django application.

# Use the official Python image as the base image
FROM python:3.13-slim

# Set environment variables to ensure that Python outputs everything to the console (i.e., no buffering)
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies defined in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Define the default command to run when starting the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
