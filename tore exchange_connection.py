[1mdiff --git a/config.py b/config.py[m
[1mindex 1b4a474..700393b 100644[m
[1m--- a/config.py[m
[1m+++ b/config.py[m
[36m@@ -1,7 +1,6 @@[m
 from dotenv import load_dotenv[m
 import os[m
 [m
[31m-# Load variables from the .env file[m
 load_dotenv()[m
 [m
 EMAIL = os.getenv("EMAIL")[m
[1mdiff --git a/email_reader.py b/email_reader.py[m
[1mindex 1841343..5919ce3 100644[m
[1m--- a/email_reader.py[m
[1m+++ b/email_reader.py[m
[36m@@ -1,48 +1,26 @@[m
[31m-import os[m
[31m-from exchangelib import FileAttachment[m
[31m-from exchange_connection import connect_to_exchange[m
[32m+[m[32mclass EmailReader:[m
 [m
[32m+[m[32m    def __init__(self, account):[m
 [m
[31m-def read_latest_emails(limit=5):[m
[31m-    account = connect_to_exchange()[m
[32m+[m[32m        self.mailbox = account.mailbox()[m
 [m
[31m-    messages = ([m
[31m-        account.inbox[m
[31m-        .all()[m
[31m-        .order_by("-datetime_received")[:limit][m
[31m-    )[m
 [m
[31m-    attachments_folder = os.path.join(os.path.dirname(__file__), "attachments")[m
[31m-    os.makedirs(attachments_folder, exist_ok=True)[m
[32m+[m[32m    def read_emails(self, limit=5):[m
 [m
[31m-    for index, message in enumerate(messages, start=1):[m
[32m+[m[32m        inbox = self.mailbox.inbox_folder()[m
 [m
[31m-        print("=" * 80)[m
[31m-        print(f"Email #{index}")[m
[31m-        print("=" * 80)[m
[32m+[m[32m        messages = inbox.get_messages([m
[32m+[m[32m            limit=limit[m
[32m+[m[32m        )[m
 [m
[31m-        print("Subject :", message.subject)[m
[32m+[m[32m        for message in messages:[m
 [m
[31m-        if message.sender:[m
[31m-            print("Sender  :", message.sender.email_address)[m
[32m+[m[32m            print(message.subject)[m
 [m
[31m-        print("Received:", message.datetime_received)[m
[32m+[m[32m            print([m
[32m+[m[32m                message.sender.address[m
[32m+[m[32m            )[m
 [m
[31m-        print("\nAttachments:")[m
[31m-[m
[31m-        if not message.attachments:[m
[31m-            print("No attachments")[m
[31m-[m
[31m-        for attachment in message.attachments:[m
[31m-[m
[31m-            if isinstance(attachment, FileAttachment):[m
[31m-[m
[31m-                filepath = os.path.join(attachments_folder, attachment.name)[m
[31m-[m
[31m-                with open(filepath, "wb") as f:[m
[31m-                    f.write(attachment.content)[m
[31m-[m
[31m-                print("Downloaded:", attachment.name)[m
[31m-                print("Saved to:", filepath)[m
[31m-[m
[31m-        print()[m
\ No newline at end of file[m
[32m+[m[32m            print([m
[32m+[m[32m                message.body[m
[32m+[m[32m            )[m
\ No newline at end of file[m
[1mdiff --git a/email_sender.py b/email_sender.py[m
[1mindex e8630d5..b11687d 100644[m
[1m--- a/email_sender.py[m
[1m+++ b/email_sender.py[m
[36m@@ -1,26 +1,23 @@[m
[31m-from exchangelib import Message, Mailbox[m
[31m-from exchange_connection import connect_to_exchange[m
[32m+[m[32mclass EmailSender:[m
 [m
[32m+[m[32m    def __init__(self, account):[m
 [m
[31m-def send_email():[m
[31m-    account = connect_to_exchange()[m
[32m+[m[32m        self.mailbox = account.mailbox()[m
 [m
[31m-    message = Message([m
[31m-        account=account,[m
[31m-        subject="Test Email from Python",[m
[31m-        body="""[m
[31m-Hello Sir,[m
 [m
[31m-This email was sent using Python and Exchange Server.[m
[32m+[m[32m    def send_email([m
[32m+[m[32m        self,[m
[32m+[m[32m        receiver,[m
[32m+[m[32m        subject,[m
[32m+[m[32m        body[m
[32m+[m[32m    ):[m
 [m
[31m-Regards,[m
[31m-IT Intern[m
[31m-""",[m
[31m-        to_recipients=[[m
[31m-            Mailbox(email_address="Taymoor.Tariq@fatima-group.com")[m
[31m-        ][m
[31m-    )[m
[32m+[m[32m        message = self.mailbox.new_message()[m
 [m
[31m-    message.send()[m
[32m+[m[32m        message.to.add(receiver)[m
 [m
[31m-    print("✅ Email sent successfully!")[m
\ No newline at end of file[m
[32m+[m[32m        message.subject = subject[m
[32m+[m
[32m+[m[32m        message.body = body[m
[32m+[m
[32m+[m[32m        message.send()[m
\ No newline at end of file[m
[1mdiff --git a/exchange_connection.py b/exchange_connection.py[m
[1mindex 6397634..64c3c1a 100644[m
[1m--- a/exchange_connection.py[m
[1m+++ b/exchange_connection.py[m
[36m@@ -1,23 +1,20 @@[m
[31m-from exchangelib import Credentials, Configuration, Account, DELEGATE[m
[31m-from config import EMAIL, PASSWORD, EWS_URL[m
[32m+[m[32m# exchange_connection.py[m
[32m+[m[32mfrom O365 import Account[m
[32m+[m[32mfrom config import CLIENT_ID, CLIENT_SECRET[m
 [m
 [m
[31m-def connect_to_exchange():[m
[31m-    credentials = Credentials([m
[31m-        username=EMAIL,[m
[31m-        password=PASSWORD[m
[31m-    )[m
[32m+[m[32mclass ExchangeConnection:[m
 [m
[31m-    config = Configuration([m
[31m-        service_endpoint=EWS_URL,[m
[31m-        credentials=credentials[m
[31m-    )[m
[32m+[m[32m    def __init__(self):[m
 [m
[31m-    account = Account([m
[31m-        primary_smtp_address=EMAIL,[m
[31m-        config=config,[m
[31m-        autodiscover=False,[m
[31m-        access_type=DELEGATE[m
[31m-    )[m
[32m+[m[32m        credentials = ([m
[32m+[m[32m            CLIENT_ID,[m
[32m+[m[32m            CLIENT_SECRET[m
[32m+[m[32m        )[m
 [m
[31m-    return account[m
\ No newline at end of file[m
[32m+[m[32m        self.account = Account(credentials)[m
[32m+[m
[32m+[m
[32m+[m[32m    def get_account(self):[m
[32m+[m
[32m+[m[32m        return self.account[m
\ No newline at end of file[m
[1mdiff --git a/main.py b/main.py[m
[1mindex dfa29b5..1800fec 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -1,11 +1,15 @@[m
[31m-from email_sender import send_email[m
[32m+[m[32m# main.py[m
[32m+[m[32mfrom exchange_connection import ExchangeConnection[m
[32m+[m[32mfrom email_reader import EmailReader[m
 [m
[31m-print("=" * 50)[m
[31m-print("Exchange Email Automation")[m
[31m-print("=" * 50)[m
 [m
[31m-try:[m
[31m-    send_email()[m
[32m+[m[32mdef main():[m
[32m+[m[32m    connection = ExchangeConnection()[m
[32m+[m[32m    account = connection.get_account()[m
 [m
[31m-except Exception as e:[m
[31m-    print(e)[m
\ No newline at end of file[m
[32m+[m[32m    reader = EmailReader(account)[m
[32m+[m[32m    reader.read_emails()[m
[32m+[m
[32m+[m
[32m+[m[32mif __name__ == "__main__":[m
[32m+[m[32m    main()[m
\ No newline at end of file[m
[1mdiff --git a/utils/file_handler.py b/utils/file_handler.py[m
[1mindex e69de29..d50227c 100644[m
[1m--- a/utils/file_handler.py[m
[1m+++ b/utils/file_handler.py[m
[36m@@ -0,0 +1,7 @@[m
[32m+[m[32mimport os[m
[32m+[m
[32m+[m
[32m+[m[32mdef create_folder(path):[m
[32m+[m
[32m+[m[32m    if not os.path.exists(path):[m
[32m+[m[32m        os.makedirs(path)[m
\ No newline at end of file[m
[1mdiff --git a/utils/logger.py b/utils/logger.py[m
[1mindex e69de29..a863615 100644[m
[1m--- a/utils/logger.py[m
[1m+++ b/utils/logger.py[m
[36m@@ -0,0 +1,21 @@[m
[32m+[m[32mfrom exchange.exchange_connection import ExchangeConnection[m
[32m+[m[32mfrom email_service.email_reader import EmailReader[m
[32m+[m[32mfrom utils.logger import get_logger[m
[32m+[m
[32m+[m[32mlogger = get_logger()[m
[32m+[m
[32m+[m
[32m+[m[32mdef main():[m
[32m+[m[32m    logger.info("Starting O365 Email Automation")[m
[32m+[m
[32m+[m[32m    connection = ExchangeConnection()[m
[32m+[m[32m    account = connection.get_account()[m
[32m+[m
[32m+[m[32m    reader = EmailReader(account)[m
[32m+[m[32m    reader.read_emails()[m
[32m+[m
[32m+[m[32m    logger.info("Program completed successfully")[m
[32m+[m
[32m+[m
[32m+[m[32mif __name__ == "__main__":[m
[32m+[m[32m    main()[m
\ No newline at end of file[m
