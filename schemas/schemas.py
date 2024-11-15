from pydantic import BaseModel, EmailStr
from typing import Optional, Union
from uuid import UUID
from datetime import datetime


class HospitalBase(BaseModel):
    name: str
    address: str
    contact_number: str
    email: EmailStr
    website: Optional[str] = None


class HospitalCreate(HospitalBase):
    pass


class HospitalUpdate(HospitalBase):
    name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[EmailStr] = None
    website: Optional[str] = None


class HospitalRead(HospitalBase):
    id: int
    created_at: datetime
    updated_at: datetime
