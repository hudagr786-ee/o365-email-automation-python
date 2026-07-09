# Exchange Email Automation System

## Overview

Exchange Email Automation System is a Python-based application that integrates with Microsoft Exchange Server to automate email operations.

The project provides a backend service for connecting with Exchange Server, reading emails, sending emails, and detecting new incoming emails. A FastAPI-based API layer and HTML dashboard have been added to demonstrate client-server communication and real-time email monitoring using polling.

---

## Features

* Connects with Microsoft Exchange Server using Exchange Web Services (EWS)
* Reads latest emails from inbox
* Sends emails automatically
* Detects newly received emails
* REST API implementation using FastAPI
* Web-based email monitoring dashboard
* Client-server communication
* Automatic email checking using polling
* Clean separation between API layer and service layer
* Secure configuration using environment variables

---

## System Architecture

```
                 Browser Client
                       |
                       |
              HTML Dashboard
                       |
              Polling Every 5 Seconds
                       |
                       |
              FastAPI Backend
                       |
                       |
              ExchangeService
                       |
                       |
          Microsoft Exchange Server
```

---

## Project Structure

```
PythonProject/

│
├── app.py
│       FastAPI application and API endpoints
│
├── exchange_service.py
│       Exchange Server operations
│
├── config.py
│       Configuration and environment variables
│
├── static/
│       └── index.html
│              Email monitoring dashboard
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
        Sensitive credentials
```

---

## Technologies Used

* Python
* FastAPI
* Exchange Web Services (EWS)
* exchangelib
* HTML/CSS/JavaScript
* Uvicorn
* dotenv

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project directory:

```
EMAIL=your_email
PASSWORD=your_password
EWS_URL=exchange_server_url
```

The application loads credentials securely using environment variables.

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The server will run at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

### Home Endpoint

```
GET /
```

Returns API status information.

---

### Email Monitoring Endpoint

```
GET /check-new-email
```

Checks Exchange inbox for newly received emails.

Example response:

```json
{
    "new_email": true,
    "subject": "Meeting Update"
}
```

---

### Dashboard

```
GET /dashboard
```

Opens the email monitoring dashboard.

The dashboard automatically checks for new emails every 5 seconds.

---

## How Polling Works

The frontend dashboard acts as a client.

Flow:

```
Browser
   |
   |
Every 5 seconds
   |
   |
GET /check-new-email
   |
   |
FastAPI Server
   |
   |
ExchangeService
   |
   |
Exchange Server
```

If a new email is detected, the dashboard updates automatically.

---

## ExchangeService Design

The `ExchangeService` class handles all Exchange-related operations:

* Establishing Exchange connection
* Reading emails
* Sending emails
* Detecting new emails

Keeping Exchange operations separate improves:

* Code maintainability
* Reusability
* Scalability

---

## API Documentation

FastAPI automatically provides interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Future Improvements

Possible enhancements:

* Replace polling with WebSocket-based real-time notifications
* Add database storage for email history
* Add authentication using OAuth2
* Migrate from Exchange Web Services (EWS) to Microsoft Graph API
* Add background email monitoring service
* Improve logging and monitoring
* Add automated testing

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* Backend API development
* Client-server architecture
* REST API communication
* Microsoft Exchange integration
* Python service layer design
* Frontend-backend interaction
* Email automation workflow

---

## Author

**Huda**

Electrical Engineering Student
Telecommunication Domain
