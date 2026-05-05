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
Bonjour,

Votre site web est indisponible :

{domain}

Merci de le vérifier rapidement.
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)