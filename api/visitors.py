from fastapi import FastAPI, APIRouter


router = APIRouter(prefix="/visitors", tags=["visitors"])


@router.get("/")
def get_visitors():
    return {"name": "Judah Chisare", "national_id": "67-161886z67"}
