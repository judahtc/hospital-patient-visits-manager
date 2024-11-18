from fastapi import FastAPI, APIRouter
from fastapi import Depends, HTTPException
from models import models
from schemas import schemas
from security.jwt_handler import create_access_token
from db.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from typing import List, Union
import sqlalchemy
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(user: str, login_data: schemas.LoginSchema, db: Session = Depends(get_db)):
    if user == "admin":
        admin = db.query(models.Admin).filter(
            models.Admin.email == login_data.email).first()
        if not admin:
            raise HTTPException(status_code=404, detail="User not found")
        if admin.password != login_data.password:
            raise HTTPException(status_code=401, detail="Incorrect password")
        return create_access_token(login_data)
    else:
        patient = db.query(models.Patient).filter(
            models.Patient.email == login_data.email).first()
        return {"detail": "Login successful"}
