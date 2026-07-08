"""
config.py

This module loads the application configuration from the .env file.
It provides the Exchange email credentials and server settings
required to establish a connection.
"""

from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
EWS_URL = os.getenv("EWS_URL")