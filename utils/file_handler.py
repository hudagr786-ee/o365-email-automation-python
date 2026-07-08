"""
file_handler.py

This module contains helper functions for file and folder
operations used throughout the application.
"""

import os


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)