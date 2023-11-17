# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# and ensure pytest is installed for running tests

RUN pip install --no-cache-dir -r requirements.txt pytest

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt and pytest
RUN pip install --no-cache-dir -r requirements.txt pytest

# Command to run when the container launches
CMD ["python", "./test.py"]
