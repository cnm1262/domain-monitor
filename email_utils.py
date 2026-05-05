import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_alert(to_email, domain):
    try:
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            print("Email not configured.")
            return

        msg = EmailMessage()
        msg["Subject"] = "Website Down Alert"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        msg.set_content(f"""
Bonjour,

Votre site web est indisponible :

{domain}

Merci de le vérifier rapidement.
""")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Alert email sent.")

    except Exception as e:
        print("Email error:", e)