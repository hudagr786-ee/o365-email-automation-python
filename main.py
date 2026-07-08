"""
main.py

This is the entry point of the application.
It creates an instance of ExchangeService and
invokes the required email operations.
"""

from exchange_service import ExchangeService


def main():

    service = ExchangeService()

    service.read_emails()

    # Uncomment to send an email
    # service.send_email(
    #     receiver="example@example.com",
    #     subject="Test Email",
    #     body="Hello from Python!"
    # )


if __name__ == "__main__":
    main()