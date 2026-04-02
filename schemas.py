from pydantic import BaseModel, Field
from typing import Optional


class TravelRequest(BaseModel):
    message: str = Field(..., min_length=3)
    budget: Optional[int] = Field(default=None, gt=0)
    travelers: Optional[int] = Field(default=None, gt=0)