from datetime import datetime
from typing import Optional

from pydantic import BaseModel, model_validator

from schemas.doctor import Doctor


class Appointment(BaseModel):
    id: int
    doctor_id: int
    patient_name: str
    patient_phone: Optional[str] = None
    appointment_date: datetime

    @model_validator(mode="after")
    def convert_start_time_to_appointment_date(self):
        if hasattr(self, "start_time") and self.start_time is not None:
            self.appointment_date = datetime.fromtimestamp(self.start_time)
        return self


class AppointmentWithDoctor(Appointment):
    doctor: Doctor
