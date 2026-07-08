from exchange_connection import connect_to_exchange
from email_reader import read_latest_emails


def main():

    account = connect_to_exchange()

    read_latest_emails(account)


if __name__ == "__main__":
    main()