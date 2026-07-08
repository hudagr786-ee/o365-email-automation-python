"""
logger.py

This module provides a reusable logging configuration
for the application.

It helps maintain consistent logging across different modules.
"""
import logging


def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()