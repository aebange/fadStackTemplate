# Use an official Python runtime as a parent image
FROM python:3.12.1

# Create and set the working directory
WORKDIR /app

# Copy only the necessary files
COPY backend /app

# Install dependencies
RUN pip install -r app/requirements.txt

# Expose the port your app runs on
EXPOSE 5000

ENV PYTHONPATH=/app:$PYTHONPATH

# Command to run your application
CMD ["python", "backend/app/app.py"]
