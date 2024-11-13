from fastapi import FastAPI, APIRouter


router = APIRouter(prefix="/patients", tags=["patients"])


@router.get("/")
def get_patients():
    return {"name": "Judah Chisare", "national_id": "67-161886z67"}
