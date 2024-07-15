# Use Python 3.6.5 as a parent image
FROM python:3.6.5-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Copy the start-server script into the container
COPY start-server.sh /app/

# Make the start-server script executable
RUN chmod +x /app/start-server.sh

# Expose port 7188 for the application
EXPOSE 7188

# Run the application
CMD ["/app/start-server.sh"]



