from typing import Union
from api import patients, visitors, admins, hospital, security

from fastapi import FastAPI
from models import models
from db.database import engine

app = FastAPI(title="Hospital Patient Visit Manager", description="The Hospital Security Application is a system designed to verify and manage authorized visitors for patients. The system will be run by Admins and Security personnel. Security will verify the visitor’s identity using their National ID and check against the patient's pre-authorized visitor list.", version="1.0.0",)

models.Base.metadata.create_all(bind=engine)


@app.get("/health")
def read_root():
    return {"Hey": "I am working"}


app.include_router(security.router)
app.include_router(hospital.router)
app.include_router(admins.router)
app.include_router(patients.router)
app.include_router(visitors.router)
