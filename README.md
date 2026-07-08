# Exchange Email Automation using Python

## Overview

This project is a Python-based email automation application that connects to Microsoft Exchange Server using Exchange Web Services (EWS). The application demonstrates Object-Oriented Programming (OOP) principles by encapsulating all Exchange-related operations within a single service class.

The project supports reading and sending emails while following a clean, modular, and maintainable architecture.

---

## Features

- Connect to Microsoft Exchange Server
- Read the latest emails from the inbox
- Send emails
- Secure configuration using environment variables
- Encapsulation using the `ExchangeService` class
- Modular and maintainable code structure
- Easy to extend for future email automation tasks

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
├── exchange_service.py
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

### Clone the repository

```bash
git clone https://github.com/hudagr786-ee/o365-email-automation-python.git
```

### Navigate to the project directory

```bash
cd o365-email-automation-python
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

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
EWS_URL=https://your-server/EWS/Exchange.asmx
```

---

## Running the Application

Run the application using:

```bash
python main.py
```

---

## Project Modules

### config.py

Loads environment variables from the `.env` file and provides the application configuration.

### exchange_service.py

Contains the `ExchangeService` class, which encapsulates all Exchange-related operations.

Responsibilities include:

- Establishing a connection to Microsoft Exchange Server
- Reading emails from the inbox
- Sending emails

### utils/logger.py

Provides a reusable logging configuration for the application.

### utils/file_handler.py

Provides reusable helper functions for file and directory operations.

### main.py

Acts as the application's entry point by creating an instance of `ExchangeService` and invoking the required email operations.

---

## Software Design

This project follows modern software engineering principles, including:

- Object-Oriented Programming (OOP)
- Encapsulation
- Modular Design
- Code Reusability
- Separation of Concerns

The `ExchangeService` class encapsulates all Exchange-related functionality, exposing only the required methods while hiding the implementation details of the Exchange connection.

---

## Future Enhancements

- Read emails based on filters
- Send emails with attachments
- HTML email support
- Email search functionality
- Logging and exception handling
- Configuration through external configuration files

---

## Author

**Huda**

Electrical Engineer(Telecommunication)

IT Intern