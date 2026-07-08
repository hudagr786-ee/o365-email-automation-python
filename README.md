# Exchange Email Automation System

## Project Overview

The Exchange Email Automation System is a Python application developed to automate email operations using Microsoft Exchange Web Services (EWS). It enables users to connect to an Exchange mailbox, send emails, read inbox messages, and download email attachments without using Microsoft Outlook.

This project was developed as part of an internship at **Fatima Group** to understand Exchange Server integration and email automation using Python.

---

## Features

- Connect to Microsoft Exchange Server
- Authenticate Exchange mailbox
- Read latest emails from Inbox
- Display email details (Subject, Sender, Date & Time)
- Download email attachments
- Send emails directly through Python
- Secure credential management using `.env`
- Exception handling for reliable execution

---

## Technologies Used

- Python 3.12
- ExchangeLib
- Microsoft Exchange Web Services (EWS)
- Python Dotenv

---

## Project Structure

```
PythonProject/
│
├── attachments/
├── .env
├── .env.example
├── config.py
├── exchange_connection.py
├── email_reader.py
├── email_sender.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Step 1: Clone or Download the Project

Download the project files or clone the repository.

---

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project directory.

Example:

```env
EMAIL=your_email@company.com
PASSWORD=your_password
EWS_URL=https://your-server/EWS/Exchange.asmx
```

---

## Project Modules

### `config.py`

Loads environment variables securely from the `.env` file.

Responsibilities:

- Load email credentials
- Load Exchange Server URL
- Keep sensitive information outside the source code

---

### `exchange_connection.py`

Creates a connection with Microsoft Exchange Server.

Responsibilities:

- Create Exchange credentials
- Configure Exchange Server
- Authenticate mailbox
- Return an authenticated Exchange account

---

### `email_reader.py`

Reads emails from the Inbox.

Responsibilities:

- Open Inbox
- Read latest emails
- Display email details
- Download attachments
- Save attachments inside the `attachments` folder

---

### `email_sender.py`

Sends emails using Exchange Server.

Responsibilities:

- Create email message
- Set recipient
- Set subject
- Set email body
- Send email

---

### `main.py`

Acts as the entry point of the application.

Responsibilities:

- Start the application
- Call required functions
- Display application status
- Handle exceptions

---

## Application Workflow

```
Start Application
        │
        ▼
Run main.py
        │
        ▼
Connect to Exchange Server
        │
        ▼
Authenticate Mailbox
        │
        ├──────────────┐
        ▼              ▼
Read Emails      Send Email
        │              │
        ▼              ▼
Download       Deliver Email
Attachments
        │
        ▼
Display Status
        │
        ▼
Application Ends
```

---

## Running the Application

Run the project using:

```bash
python main.py
```

---

## Sample Output

### Reading Emails

```
==================================================
Exchange Email Automation
==================================================

Email #1

Subject : EMAIL AUTOMATION LIBS
Sender  : it.intern3@fatima-group.com
Received: 2026-07-08

Downloading:
Post-Mid-Term Assignment 2 TRW.pdf

Saved Successfully
```

---

### Sending Emails

```
==================================================
Exchange Email Automation
==================================================

Connecting to Exchange Server...

Creating Email...

Sending Email...

Email sent successfully.
```

---

## Security

For security reasons, sensitive information such as:

- Email Address
- Password
- Exchange Server URL

is stored in a `.env` file instead of the application source code.

---

## Future Enhancements

Possible future improvements include:

- Send emails with attachments
- Reply to emails automatically
- Forward emails
- Filter emails by sender or subject
- Read emails from custom folders
- Schedule automated email tasks
- Email logging
- HTML email support

---

## Requirements

Required Python packages:

- exchangelib
- python-dotenv
- requests
- requests_ntlm
- lxml

Install them using:

```bash
pip install -r requirements.txt
```

---

## Author

## Author

**Huda**  
*IT Intern | Fatima Group*  

Developed during my internship as a practical implementation of Python programming concepts, automation, and software development practices.

---

## License

This project was developed for educational and internship purposes.