import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"

def send_alert(to_email, domain):
    msg = EmailMessage()
    msg["Subject"] = "🚨 Website Down Alert"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    msg.set_content(f"""
Alert!

Your website is down:
{domain}

Please check it as soon as possible.
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)