from exchangelib import (
    Credentials,
    Configuration,
    Account,
    DELEGATE
)

from config import EMAIL, PASSWORD, EWS_URL


class ExchangeService:

    def __init__(self):

        self.account = self._connect()


    def _connect(self):

        credentials = Credentials(
            username=EMAIL,
            password=PASSWORD
        )

        config = Configuration(
            service_endpoint=EWS_URL,
            credentials=credentials
        )

        return Account(
            primary_smtp_address=EMAIL,
            config=config,
            autodiscover=False,
            access_type=DELEGATE
        )


    def read_emails(self, limit=5):

        messages = (
            self.account.inbox
            .all()
            .order_by("-datetime_received")[:limit]
        )

        for index, message in enumerate(messages, start=1):

            print("=" * 60)
            print(f"Email #{index}")
            print("=" * 60)

            print("Subject :", message.subject)
            print("Sender  :", message.sender)
            print("Received:", message.datetime_received)
            print("Body:")
            print(message.text_body)


    def send_email(
        self,
        receiver,
        subject,
        body
    ):

        # Implement your send email logic here
        pass