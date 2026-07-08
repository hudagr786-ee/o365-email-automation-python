from exchange_service import ExchangeService


def main():

    service = ExchangeService()

    service.read_emails()

    # service.send_email(
    #     receiver="abc@example.com",
    #     subject="Hello",
    #     body="Testing..."
    # )


if __name__ == "__main__":
    main()