# Use the official Python image
FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python script into the container
COPY comment_instagram.py /app/comment_instagram.py

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Entry point for the container
ENTRYPOINT ["python3", "comment_instagram.py"]
