# Use an official Python runtime as base
FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Set DISPLAY environment for Tkinter (For Linux GUI support)
ENV DISPLAY=:1

# Create output directory
RUN mkdir -p /app/output

# Run the application
CMD ["python", "performancecaterogy_app.py"]
