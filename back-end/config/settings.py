import os

class Config:
    # General settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use an environment variable for security
    DEBUG = True  # Enable debugging mode for development
    
    # Database settings (if applicable)
    # DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///default.db')
    
    # Logging settings (example)
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')
    
    # You can add other configurations such as CORS, JWT secrets, etc.
