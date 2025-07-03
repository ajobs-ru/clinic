from typing import List, Union

from fastapi import APIRouter, Request

from db import crud
from schemas.appointment import Appointment, AppointmentWithDoctor

router = APIRouter()


@router.get("/appointments", response_model=List[AppointmentWithDoctor])
async def appointments_router(request: Request):
    return await crud.get_appointments()


@router.get(
    "/appointment/{appointment_id}",
    response_model=Union[AppointmentWithDoctor, None]
)
async def appointment_router(request: Request, appointment_id: int):
    return await crud.get_appointment(appointment_id)


@router.post(
    "/appointments/create",
    response_model=AppointmentWithDoctor
)
async def appointment_create_router(
    request: Request,
    appointment: Appointment
):
    return await crud.create_appointment(appointment)
