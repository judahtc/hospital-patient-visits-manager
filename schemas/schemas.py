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


class AdminBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    role: str
    hospital_id: int
    is_active: bool = True


class AdminCreate(AdminBase):
    password: str


class AdminUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    role: str | None = None
    is_active: bool | None = None


class AdminResponse(AdminBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
