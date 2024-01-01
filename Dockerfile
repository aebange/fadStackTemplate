# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /app

# Copy the virtual environment (venv) into the container
COPY backend/venv /app/venv

# Copy the rest of the application code
COPY backend /app

# Expose any necessary ports
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application using the virtual environment
CMD ["venv/bin/python", "app.py"]
