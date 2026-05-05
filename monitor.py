import requests
from datetime import datetime
from database import SessionLocal
from models import Domain
from email_utils import send_alert

OWNER_EMAIL = "owner_email@gmail.com"

def check_all_domains():
    db = SessionLocal()
    domains = db.query(Domain).all()

    for domain in domains:
        try:
            response = requests.get(domain.url, timeout=5)
            domain.response_time = str(response.elapsed.total_seconds())

            if response.status_code == 200:
                domain.status = "UP"
            else:
                domain.status = "DOWN"
                send_alert(OWNER_EMAIL, domain.url)

        except Exception:
            domain.status = "DOWN"
            domain.response_time = "0"
            send_alert(OWNER_EMAIL, domain.url)

        domain.last_checked = datetime.utcnow()

    db.commit()
    db.close()

if __name__ == "__main__":
    check_all_domains()