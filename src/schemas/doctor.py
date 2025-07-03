from typing import Optional

from pydantic import BaseModel


class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: Optional[str] = None
    experience_years: Optional[int] = None
