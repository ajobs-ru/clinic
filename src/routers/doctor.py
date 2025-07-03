from typing import List, Union

from fastapi import APIRouter, Request

from db import crud
from schemas.doctor import Doctor

router = APIRouter()


@router.get("/doctors", response_model=List[Doctor])
async def doctors_router(request: Request):
    return await crud.get_doctors()


@router.get("/doctor/{doctor_id}", response_model=Union[Doctor, None])
async def doctor_router(request: Request, doctor_id: int):
    return await crud.get_doctor(doctor_id)


@router.post("/doctors/create", response_model=Doctor)
async def doctor_create_router(request: Request, doctor: Doctor):
    return await crud.create_doctor(doctor)
