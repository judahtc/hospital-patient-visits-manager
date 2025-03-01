from fastapi import FastAPI, APIRouter
from fastapi import Depends, HTTPException
from models import models
from schemas import schemas
from db.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from typing import List, Union
import sqlalchemy
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
router = APIRouter(prefix="/audit", tags=["audit"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get('/')
def audit_trail():
    return "audit trail"