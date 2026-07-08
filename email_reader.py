import os
from exchangelib import FileAttachment
from exchange_connection import connect_to_exchange


def read_latest_emails(limit=5):
    account = connect_to_exchange()

    messages = (
        account.inbox
        .all()
        .order_by("-datetime_received")[:limit]
    )

    attachments_folder = os.path.join(os.path.dirname(__file__), "attachments")
    os.makedirs(attachments_folder, exist_ok=True)

    for index, message in enumerate(messages, start=1):

        print("=" * 80)
        print(f"Email #{index}")
        print("=" * 80)

        print("Subject :", message.subject)

        if message.sender:
            print("Sender  :", message.sender.email_address)

        print("Received:", message.datetime_received)

        print("\nAttachments:")

        if not message.attachments:
            print("No attachments")

        for attachment in message.attachments:

            if isinstance(attachment, FileAttachment):

                filepath = os.path.join(attachments_folder, attachment.name)

                with open(filepath, "wb") as f:
                    f.write(attachment.content)

                print("Downloaded:", attachment.name)
                print("Saved to:", filepath)

        print()