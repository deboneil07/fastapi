#from typing import Union
import secrets
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import validators

import schemas, models
from database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

@app.get('/')
def read_root():
    return "Welcome to url shortener API :D"

@app.post('/url', response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="provided url is not valid")

    return f"TODO: create db entry for: {url.target_url}"