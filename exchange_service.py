"""
exchange_service.py

This module provides the ExchangeService class, which encapsulates
all Exchange-related operations, including establishing the
connection, reading emails, and sending emails.

It serves as the central service for email automation.
"""

from exchangelib import (
    Credentials,
    Configuration,
    Account,
    DELEGATE,
    Message,
    Mailbox
)

from config import EMAIL, PASSWORD, EWS_URL


class ExchangeService:
    """
    Manages Exchange server operations through a single service class.

    This class establishes the Exchange connection and provides
    methods for reading and sending emails.
    """

    def __init__(self):
        """
        Initializes the Exchange service by establishing
        a connection to the Exchange server.
        """
        self.account = self._connect()

    def _connect(self):
        """
        Creates and returns an authenticated Exchange account.

        Returns:
            Account: Authenticated Exchange account.
        """

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

    def read_emails(self, limit=5):
        """
        Retrieves and displays the latest emails from the inbox.

        Args:
            limit (int): Number of emails to retrieve.
        """

        messages = (
            self.account.inbox
            .all()
            .order_by("-datetime_received")[:limit]
        )

        for index, message in enumerate(messages, start=1):

            print("=" * 80)
            print(f"Email #{index}")
            print("=" * 80)

            print("Subject :", message.subject)
            print("Sender  :", message.sender)
            print("Received:", message.datetime_received)
            print("Body:")
            print(message.text_body)
            print()

    def send_email(self, receiver, subject, body):
        """
        Creates and sends an email.

        Args:
            receiver (str): Recipient email address.
            subject (str): Email subject.
            body (str): Email message body.
        """

        message = Message(
            account=self.account,
            subject=subject,
            body=body,
            to_recipients=[
                Mailbox(email_address=receiver)
            ]
        )

        message.send()

        print("Email sent successfully.")