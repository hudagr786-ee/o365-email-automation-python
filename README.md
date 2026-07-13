# Exchange Email Automation System

## Overview

The **Exchange Email Automation System** is a Python-based application that integrates with Microsoft Exchange Server using **Exchange Web Services (EWS)**.

The project provides a complete email automation solution capable of reading emails, sending emails, monitoring new incoming emails, detecting attachments, and displaying Outlook emails through a modern FastAPI web dashboard.

The application follows a clean modular architecture using Object-Oriented Programming (OOP), making it maintainable, scalable, and easy to extend.

---

# Features

- Connects securely to Microsoft Exchange Server (EWS)
- Reads the latest emails from the inbox
- Sends emails directly through Python
- Detects newly received emails
- Displays the latest 5 emails
- Preserves HTML email formatting
- Detects email replies and forwards
- Automatically downloads email attachments
- Allows attachment download from the dashboard
- Displays sender, subject, received date, and email body
- Live dashboard with automatic refresh every 5 seconds
- Search emails by subject or sender
- Email statistics dashboard
- REST API built using FastAPI
- Secure credential management using `.env`
- Modular Object-Oriented architecture

---

# System Architecture

```
                    Browser Client
                           │
                           │
                HTML / CSS / JavaScript
                           │
                 Auto Refresh (5 Seconds)
                           │
                           ▼
                    FastAPI Backend
                           │
                           ▼
                  ExchangeService Class
                           │
                           ▼
             Microsoft Exchange Server (EWS)
```

---

# Project Structure

```
PythonProject/

│
├── app.py
│       FastAPI application
│
├── exchange_service.py
│       Handles Exchange Server operations
│
├── config.py
│       Loads environment variables
│
├── static/
│       └── index.html
│              Email monitoring dashboard
│
├── attachments/
│       Downloaded email attachments
│
├── utils/
│       ├── logger.py
│       └── file_handler.py
│
├── requirements.txt
│
├── README.md
│
└── .env
        Exchange credentials
```

---

# Technologies Used

- Python
- FastAPI
- Exchange Web Services (EWS)
- exchangelib
- HTML
- CSS
- JavaScript
- Uvicorn
- python-dotenv

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the project folder.

```env
EMAIL=your_email@example.com
PASSWORD=your_password
EWS_URL=https://your-exchange-server/EWS/Exchange.asmx
```

The application securely loads these credentials using **python-dotenv**.

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

# Dashboard

Open:

```
http://127.0.0.1:8000/dashboard
```

The dashboard provides:

- Latest 5 emails
- Email subject
- Sender information
- Received date & time
- HTML email preview
- Attachment detection
- Attachment download
- Email search
- Live updates every 5 seconds

---

# API Endpoints

## Home

```
GET /
```

Returns application status.

---

## Latest Emails

```
GET /emails
```

Returns the latest emails from Exchange Server.

Example:

```json
{
  "count": 5,
  "emails": [
    {
      "subject": "Project Update",
      "sender": "user@example.com",
      "received": "10 Jul 2026 11:30 AM",
      "has_attachments": true
    }
  ]
}
```

---

## Check New Email

```
GET /check-new-email
```

Detects whether a new email has arrived.

Example:

```json
{
    "new_email": true,
    "subject": "Meeting Schedule"
}
```

---

## Download Attachment

```
GET /attachments/{filename}
```

Downloads a saved email attachment.

---

## Dashboard

```
GET /dashboard
```

Opens the live Exchange Email Monitor dashboard.

---

# Email Monitoring Workflow

```
Browser Dashboard
        │
        │
Auto Refresh (5 sec)
        │
        ▼
FastAPI API
        │
        ▼
ExchangeService
        │
        ▼
Exchange Server
        │
        ▼
Latest Emails Returned
        │
        ▼
Dashboard Updated
```

---

# ExchangeService Responsibilities

The `ExchangeService` class is responsible for:

- Establishing Exchange Server connection
- Reading inbox emails
- Sending emails
- Cleaning email body
- Detecting replies and forwards
- Processing HTML emails
- Detecting attachments
- Saving attachments
- Returning email data to FastAPI

This separation improves:

- Maintainability
- Scalability
- Code Reusability
- Encapsulation

---

# FastAPI Documentation

Interactive Swagger documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

# Security

Sensitive credentials are never hardcoded.

The application uses:

- `.env`
- python-dotenv

to securely load Exchange credentials.

---

# Future Improvements

Possible future enhancements include:

- Microsoft Graph API integration
- OAuth2 Authentication
- WebSocket real-time notifications
- Background email monitoring service
- Email database storage
- Pagination
- Email filtering
- Unit testing
- Docker deployment

---

# Learning Outcomes

This project demonstrates:

- Python Object-Oriented Programming
- Microsoft Exchange Server Integration
- Exchange Web Services (EWS)
- FastAPI Development
- REST API Design
- Client-Server Architecture
- HTML Email Rendering
- Attachment Handling
- Backend-Frontend Communication
- Polling Mechanism
- Environment Variable Management
- Modular Software Design

---

# Author

**Huda**

Electrical Engineering Student (Telecommunication)

Python Developer | FastAPI | Exchange Email Automation