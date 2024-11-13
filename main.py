from typing import Union
from api import patients, visitors, admins
from fastapi import FastAPI

app = FastAPI(title="Hospital Patient Visit Manager", description="The Hospital Security Application is a system designed to verify and manage authorized visitors for patients. The system will be run by Admins and Security personnel. Security will verify the visitor’s identity using their National ID and check against the patient's pre-authorized visitor list.", version="1.0.0",)


@app.get("/health")
def read_root():
    return {"Hey": "I am working"}


app.include_router(admins.router)
app.include_router(patients.router)
app.include_router(visitors.router)
