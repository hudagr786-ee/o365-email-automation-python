"""
main.py

Application entry point.

Creates an ExchangeService object and
invokes the required email operations.
"""

from exchange_service import ExchangeService


def main():
    """
    Executes the application workflow.

    Returns:
        bool
    """

    service = ExchangeService()

    success = service.read_emails()

    return success


if __name__ == "__main__":

    main()