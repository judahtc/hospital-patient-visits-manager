from fastapi import FastAPI, APIRouter


router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/")
def get_admins():
    return {"name": "Judah Chisare", "national_id": "67-161886z67"}
