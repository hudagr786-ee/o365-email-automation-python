class EmailSender:
    def __init__(self, account):
        self.mailbox = account.mailbox()

    def send_email(self, receiver, subject, body):
        message = self.mailbox.new_message()

        message.to.add(receiver)
        message.subject = subject
        message.body = body

        message.send()