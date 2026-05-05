import requests
from datetime import datetime
from database import SessionLocal
from models import Domain
from email_utils import send_alert

def check_all_domains():
    db = SessionLocal()
    domains = db.query(Domain).all()

    for domain in domains:
        try:
            response = requests.get(domain.url, timeout=5)
            domain.response_time = response.elapsed.total_seconds()

            if 200 <= response.status_code < 400:
                domain.status = "UP"
            else:
                domain.status = "DOWN"
                send_alert(domain.owner_email, domain.url)

        except Exception:
            domain.status = "DOWN"
            domain.response_time = 0
            send_alert(domain.owner_email, domain.url)

        domain.last_checked = datetime.utcnow().isoformat()

    db.commit()
    db.close()