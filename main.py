from email_sender import send_email

print("=" * 50)
print("Exchange Email Automation")
print("=" * 50)

try:
    send_email()

except Exception as e:
    print(e)