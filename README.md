# Exchange Email Automation using Python

## Overview

This project is a Python-based email automation application that connects to Microsoft Exchange Server, reads emails, and provides a modular structure for extending email automation features.

The project follows clean coding practices by separating configuration, connection handling, email operations, and utility functions into individual modules.

---

## Features

- Connect to Microsoft Exchange Server
- Read latest emails from inbox
- Send emails
- Environment variable support using `.env`
- Modular project structure
- Reusable utility functions
- Easy to maintain and extend

---

## Project Structure

```
PythonProject/
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── file_handler.py
│
├── config.py
├── exchange_connection.py
├── email_reader.py
├── email_sender.py
├── main.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python 3.x
- exchangelib
- python-dotenv

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd PythonProject
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

Example:

```env
EMAIL=your_email@example.com
PASSWORD=your_password
EWS_URL=https://your_server/EWS/Exchange.asmx
```

---

## Running the Project

Run the application:

```bash
python main.py
```

---

## Module Description

### config.py

Loads environment variables from the `.env` file.

### exchange_connection.py

Creates and returns a connection to Microsoft Exchange Server.

### email_reader.py

Reads emails from the mailbox.

### email_sender.py

Creates and sends emails.

### utils/logger.py

Provides a reusable logging configuration for the application.

### utils/file_handler.py

Contains reusable helper functions for file and folder operations.

### main.py

Application entry point.

---

## Software Design

This project follows the **Single Responsibility Principle (SRP)**.

Each module is responsible for a single task:

- Configuration Management
- Exchange Connection
- Email Reading
- Email Sending
- Utility Functions
- Application Execution

This modular design improves readability, maintainability, and scalability.

---

## Author

**Huda**

Electrical Engineering (Telecommunication)

Python Intern