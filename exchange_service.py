import logging
import os
import re

from exchangelib import (
    Credentials,
    Configuration,
    Account,
    DELEGATE,
    FileAttachment
)

from config import (
    EMAIL,
    PASSWORD,
    EWS_URL
)


class ExchangeService:

    def __init__(self):

        self.logger = logging.getLogger("exchange")

        self.account = self._connect()

    def _connect(self):

        credentials = Credentials(
            username=EMAIL,
            password=PASSWORD
        )

        config = Configuration(
            service_endpoint=EWS_URL,
            credentials=credentials
        )

        account = Account(
            primary_smtp_address=EMAIL,
            config=config,
            autodiscover=False,
            access_type=DELEGATE
        )

        self.logger.info(
            "Exchange connection successful"
        )

        return account
    def clean_email_body(self, body):

        """
        Returns only the newest message.
        Removes Outlook quoted history.
        """

        if body is None:
            return ""

        body = str(body)

        markers = [

            "\nFrom:",
            "\r\nFrom:",

            "\nSent:",
            "\r\nSent:",

            "-----Original Message-----",

            "\nSubject:",
            "\r\nSubject:"
        ]

        cleaned = body

        for marker in markers:

            if marker in cleaned:

                cleaned = cleaned.split(marker)[0]

        cleaned = re.sub(
            r"\n{3,}",
            "\n\n",
            cleaned
        )

        return cleaned.strip()


    def is_reply(self, subject):

        if not subject:
            return False

        subject = subject.upper()

        return (
            subject.startswith("RE:")
            or subject.startswith("FW:")
            or subject.startswith("FWD:")
        )
    def read_emails(self, limit=10):

        emails = []

        self.logger.info(
            f"Reading latest {limit} emails"
        )

        messages = (
            self.account
            .inbox
            .all()
            .order_by("-datetime_received")[:limit]
        )

        for message in messages:

            attachments = []

            # -----------------------------
            # Handle Attachments
            # -----------------------------
            if message.has_attachments:

                self.logger.info(
                    f"Attachments detected in email: {message.subject}"
                )

                for attachment in message.attachments:

                    self.logger.info(
                        f"Attachment type: {type(attachment)}"
                    )

                    self.logger.info(
                        f"Attachment name: {attachment.name}"
                    )

                    if isinstance(attachment, FileAttachment):

                        os.makedirs(
                            "attachments",
                            exist_ok=True
                        )

                        file_path = os.path.join(
                            "attachments",
                            attachment.name
                        )

                        with open(file_path, "wb") as file:

                            file.write(
                                attachment.content
                            )

                        self.logger.info(
                            f"Saved attachment: {attachment.name}"
                        )

                        attachments.append(
                            {
                                "name": attachment.name,
                                "size": attachment.size,
                                "url": f"/attachments/{attachment.name}"
                            }
                        )

            # -----------------------------
            # Conversation ID
            # -----------------------------
            try:

                conversation_id = str(
                    message.conversation_id.id
                )

            except Exception:

                conversation_id = ""

            # -----------------------------
            # Sender
            # -----------------------------
            sender = ""

            try:

                if message.sender:

                    sender = message.sender.email_address

            except Exception:

                sender = ""

            # -----------------------------
            # Email Body
            # -----------------------------

            # Plain text (for automation and parsing)
            body_text = self.clean_email_body(
                message.text_body
            )

            # HTML (for displaying like Outlook)
            body_html = ""

            try:
                if message.body:
                    body_html = str(message.body)
                    body_html = re.sub(
                        r'margin\s*:\s*[^;"\']+',
                        'margin:5px',
                        body_html,
                        flags=re.IGNORECASE
                    )

                    body_html = re.sub(
                        r'padding\s*:\s*[^;"\']+',
                        'padding:2px',
                        body_html,
                        flags=re.IGNORECASE
                    )

                    body_html = body_html.replace("&nbsp;", " ")
            except Exception:
                body_html = ""

            # -----------------------------
            # Date & Time
            # -----------------------------
            received = message.datetime_received.strftime(
                "%d %b %Y %I:%M %p"
            )

            # -----------------------------
            # Reply Detection
            # -----------------------------
            reply = self.is_reply(
                message.subject
            )

            # -----------------------------
            # Build JSON
            # -----------------------------
            emails.append({

                "conversation_id": conversation_id,

                "subject": message.subject,

                "sender": sender,

                "received": received,

                "is_reply": reply,

                "body_text": body_text,

                "body_html": body_html,

                "has_attachments": message.has_attachments,

                "attachments": attachments

            })
        return emails