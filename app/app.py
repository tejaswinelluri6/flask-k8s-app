import logging
from flask import Flask
import os

app = Flask(__name__)  # Correct usage of Flask

# Set up logging level from environment or default to INFO
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level)

@app.route('/')
def problem():
    app.logger.info("Processing request for '/' route")
    return "WELCOME TO THE BMW GROUP!"

if __name__ == "__main__":  # Correct check for running the script
    app.run(host='0.0.0.0', port=8080)
