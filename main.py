from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Domain
from monitor import check_all_domains
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DomainCreate(BaseModel):
    url: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/domains")
def add_domain(domain: DomainCreate, db: Session = Depends(get_db)):
    new_domain = Domain(url=domain.url)
    db.add(new_domain)
    db.commit()
    db.refresh(new_domain)

    return {
        "message": "Domain added successfully",
        "domain": new_domain.url
    }

@app.get("/domains")
def get_domains(db: Session = Depends(get_db)):
    return db.query(Domain).all()

@app.get("/")
def home():
    return {"message": "Domain Monitor API is running"}

@app.get("/check-now")
def check_now():
    check_all_domains()
    return {"message": "All domains checked"}