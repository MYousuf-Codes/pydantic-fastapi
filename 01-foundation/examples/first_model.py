from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': 1, 'name': "Yousaf", 'is_active': True}

# ** is the expansion operator that unpacks the dictionary into keyword arguments
user = User(**input_data)

print(user)