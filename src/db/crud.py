from typing import List, Union

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import joinedload, sessionmaker

from config import DB_URL
from schemas.appointment import Appointment as AppointmentSchema
from schemas.doctor import Doctor as DoctorSchema

from .models import Appointment, Doctor

engine = create_async_engine(
    DB_URL, pool_pre_ping=True, pool_recycle=3600, pool_size=10, max_overflow=50
)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# Doctor methods


async def get_doctor(doctor_id: int) -> Union[Doctor, None]:
    async with async_session() as session:
        query = select(Doctor).where(Doctor.id == doctor_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def create_doctor(doctor: DoctorSchema) -> Doctor:
    async with async_session() as session:
        result = await session.execute(
            insert(Doctor).values(**doctor.model_dump()).returning(Doctor)
        )
        await session.commit()
        return result.scalar_one()


async def get_doctors() -> List[Doctor]:
    async with async_session() as session:
        result = await session.execute(select(Doctor))
        return result.scalars().all()


# Appointment methods


async def get_appointment(appointment_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(Appointment)
            .options(joinedload(Appointment.doctor))
            .where(Appointment.id == appointment_id)
        )
        return result.scalar_one_or_none()


async def create_appointment(appointment: AppointmentSchema) -> Appointment:
    async with async_session() as session:
        result = await session.execute(
            insert(Appointment)
            .values(**appointment.model_dump())
            .returning(Appointment)
        )
        await session.commit()
        return result.scalar_one()


async def get_appointments() -> List[Appointment]:
    async with async_session() as session:
        result = await session.execute(
            select(Appointment).options(joinedload(Appointment.doctor))
        )
        return result.scalars().all()
