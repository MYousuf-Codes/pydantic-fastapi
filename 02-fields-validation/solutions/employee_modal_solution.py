from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., 
        min_length=3,
        max_length=50,
        description="Full name of the employee",
        example="Muhammad Yousaf"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ..., ge=10000
    )

