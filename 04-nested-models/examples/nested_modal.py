from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

# always to add this forward reference
Comment.model_rebuild()  #self-referencing models

address = Address(
    street="123 Main St",
    city="Karachi",
    postal_code="12345"
)

user = User(
    id=1,
    name="Muhammad Yousaf",
    address = address
)

comment = Comment(
    id = 1,
    content = "Ki Haal ha",
    replies= [
        Comment(
            id=2,
            content="Theek thaak",
            replies=[
                Comment(
                    id=3,
                    content="Bilkul theek",
                )
            ]
        ),
        Comment(
            id=4,
            content="Hn sab theek",
            replies=[
                Comment(
                    id=5,
                    content="Good hogaya",
                )
            ]   
        )
    ]
)