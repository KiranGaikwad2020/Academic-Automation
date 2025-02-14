# Use an official Python runtime as base
FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Xvfb and Tkinter dependencies
RUN apt-get update && apt-get install -y xvfb x11-utils python3-tk

# Copy application files
COPY performancecategory_app.py .

# Set DISPLAY environment variable
ENV DISPLAY=:99

# Start Xvfb before running the application
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & python performancecategory_app.py"]
