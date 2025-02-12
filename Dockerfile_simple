# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Run script when the container starts
CMD ["python", "performancecategory.py"]

