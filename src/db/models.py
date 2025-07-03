from sqlalchemy import (BigInteger, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    phone = Column(String)
    experience_years = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    appointments = relationship("Appointment", back_populates="doctor")


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    doctor_id = Column(BigInteger, ForeignKey("doctors.id"), nullable=False)
    patient_name = Column(String, nullable=False)
    patient_phone = Column(String)
    appointment_date = Column(DateTime(timezone=True), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    doctor = relationship("Doctor", back_populates="appointments")
