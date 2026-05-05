from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Domain
from monitor import check_all_domains
from database import Base, engine
from models import Domain
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/domains")
def get_domains():
    db = SessionLocal()
    domains = db.query(Domain).all()
    db.close()
    return domains

from models import DomainCreate

@app.post("/domains")
def add_domain(domain: DomainCreate):
    db = SessionLocal()
    new_domain = Domain(
        url=domain.url,
        owner_email=domain.owner_email
    )
    db.add(new_domain)
    db.commit()
    db.refresh(new_domain)
    db.close()
    return new_domain

@app.get("/check-now")
def check_now():
    check_all_domains()
    return {"message": "checked"}