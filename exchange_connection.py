from exchangelib import Credentials, Configuration, Account, DELEGATE
from config import EMAIL, PASSWORD, EWS_URL


def connect_to_exchange():
    credentials = Credentials(
        username=EMAIL,
        password=PASSWORD
    )

    config = Configuration(
        service_endpoint=EWS_URL,
        credentials=credentials
    )

    account = Account(
        primary_smtp_address=EMAIL,
        config=config,
        autodiscover=False,
        access_type=DELEGATE
    )

    return account