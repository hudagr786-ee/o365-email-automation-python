from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
EWS_URL = os.getenv("EWS_URL")