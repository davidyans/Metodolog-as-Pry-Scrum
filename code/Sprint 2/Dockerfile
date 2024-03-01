# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the Python dependencies file to the container
COPY requirements.txt /app/

# Install Flask and any other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Use Python to execute the Flask application
CMD ["python", "-m", "flask", "run"]
