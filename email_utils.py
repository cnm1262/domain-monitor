import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_alert(to_email, domain):
    try:
        msg = EmailMessage()
        msg["Subject"] = "🚨 Website Down Alert"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        msg.set_content(f"Your website {domain} is DOWN.")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

    except Exception as e:
        print("Email error:", e)