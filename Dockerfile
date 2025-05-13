# Use Python 3.13 as base image
FROM python:3.13-slim

# Working dir in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ ./app/
COPY tests/ ./tests/

# Set ENV variables
ENV PYTHONPATH=/app

# Run the app 
CMD ["python", "app/main.py"]
