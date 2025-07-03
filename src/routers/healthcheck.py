from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/health")
async def healthcheck(request: Request):
    return {"status": "ok"}
