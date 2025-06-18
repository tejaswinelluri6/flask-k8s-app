# Use the official Python image from Docker Hub
FROM python:alpine3.21
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN adduser -D -u 1000 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app && \
    pip install --no-cache-dir flask

# Copy the local app files into the container's working directory
COPY . /app

# Switch to the non-root user
USER appuser

# Expose the port that the app will run on (5000 in this case)
EXPOSE 8080

# Set the command to run your Flask app
CMD ["python3", "app.py"]
