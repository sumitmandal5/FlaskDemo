# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app
# Copy the all the files into the container directory app
COPY . /app
# Install the dependencies
RUN pip install -r requirements.txt
# Expose the port in container that the app runs on
EXPOSE 3000
#this will run in the mentioned working directory which is app
CMD python ./main.py

