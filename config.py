import os

from dotenv import load_dotenv


load_dotenv()


EMAIL = os.getenv(
    "EMAIL"
)

PASSWORD = os.getenv(
    "PASSWORD"
)

EWS_URL = os.getenv(
    "EWS_URL"
)