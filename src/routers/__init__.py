from fastapi import APIRouter

from . import appointment, doctor, healthcheck

api_router = APIRouter()

routers = [doctor.router, appointment.router, healthcheck.router]

for router in routers:
    api_router.include_router(router)
