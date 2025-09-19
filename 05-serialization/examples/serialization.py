from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True
    createdAt: datetime
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

# creating a user instance
user = User(
    id=1,
    name="Muhammad Yousaf",
    email="someone@example.com",
    address=Address(
        street="123 Main St",
        city="karachi",
        postal_code="12345"
    ),
    is_active=True,
    createdAt=datetime(2025, 3, 15, 14, 30),
    tags=["premium", "subscriber"],
)

# serializing
# using model_dump() -> dict
python_dict = user.model_dump()
print("Python Dict:", python_dict)
print("==============================================")
# using model_dump_json() -> JSON string
json_str = user.model_dump_json()
print("JSON String:", json_str)

