from exchangelib import FileAttachment


def read_latest_emails(account, limit=5):

    messages = (
        account.inbox
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