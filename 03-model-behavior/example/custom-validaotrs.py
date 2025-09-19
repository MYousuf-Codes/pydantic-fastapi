from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username') #username field validator
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters long')
        return v

class SignupData(BaseModel):
    password: str
    password_confirm: str

    @model_validator(mode='after') #model validator
    def password_match(cls, values):
        if values.password != values.password_confirm:
            raise ValueError('Password do not match')
        return values

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self)-> float: #computed field
        return self.price * self.quantity