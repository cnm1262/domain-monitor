from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from database import Base, engine, SessionLocal
from models import Domain
from monitor import check_all_domains

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
    owner_email: str

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/domains")
def get_domains():
    db = SessionLocal()
    domains = db.query(Domain).all()
    db.close()
    return domains

@app.post("/domains")
def add_domain(domain: DomainCreate):
    db = SessionLocal()

    existing = db.query(Domain).filter(Domain.url == domain.url).first()
    if existing:
        db.close()
        return {"message": "Domain already exists"}

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
    return {"message": "All domains checked"}