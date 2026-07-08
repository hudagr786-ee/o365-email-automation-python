# Exchange Email Automation using Python

## Overview

This project is a Python-based email automation application that connects to Microsoft Exchange Server using Exchange Web Services (EWS). The application demonstrates Object-Oriented Programming (OOP) principles by encapsulating all Exchange-related operations within a single service class.

The project supports reading and sending emails while maintaining a clean, modular, and maintainable architecture.

---

## Features

- Connect to Microsoft Exchange Server
- Read latest emails
- Send emails
- Secure configuration using environment variables
- Encapsulation using a single service class
- Utility modules for logging and file handling
- Clean and maintainable project structure

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

Clone the repository

```bash
git clone https://github.com/your-username/o365-email-automation-python.git
```

Move to project directory

```bash
cd o365-email-automation-python
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file.

Example

```env
EMAIL=your_email@example.com
PASSWORD=your_password
EWS_URL=https://your-server/EWS/Exchange.asmx
```

---

## Run the Project

```bash
python main.py
```

---

## Project Modules

### config.py

Loads environment variables.

### exchange_service.py

Responsible for:

- Connecting to Microsoft Exchange Server
- Reading emails
- Sending emails

This class encapsulates all Exchange-related functionality.

### utils/logger.py

Provides reusable logging configuration.

### utils/file_handler.py

Provides reusable helper functions for file and folder operations.

### main.py

Application entry point that creates an instance of `ExchangeService` and invokes its methods.

---

## Object-Oriented Design

This project demonstrates:

- Encapsulation
- Modular Design
- Code Reusability
- Separation of Concerns

The Exchange connection and email operations are encapsulated inside the `ExchangeService` class, exposing only public methods to the application while hiding implementation details.

---

## Author

**Huda**

Electrical Engineer (Telecommunication)

IT Intern