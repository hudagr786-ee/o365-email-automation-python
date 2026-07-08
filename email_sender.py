from exchangelib import Message, Mailbox
from exchange_connection import connect_to_exchange


def send_email():
    account = connect_to_exchange()

    message = Message(
        account=account,
        subject="Test Email from Python",
        body="""
Hello Sir,

This email was sent using Python and Exchange Server.

Regards,
IT Intern
""",
        to_recipients=[
            Mailbox(email_address="Taymoor.Tariq@fatima-group.com")
        ]
    )

    message.send()

    print("✅ Email sent successfully!")