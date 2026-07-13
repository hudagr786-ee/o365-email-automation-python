"""
file_handler.py

Provides reusable file handling utilities.
"""

import os


def create_folder(path):
    """
    Creates a folder if it does not exist.

    Args:
        path (str)
    """

    if not os.path.exists(path):

        os.makedirs(path)