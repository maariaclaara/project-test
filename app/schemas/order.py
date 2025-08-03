
from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class Item(BaseModel):
    name: str
    quantity: int
    unit_price: float

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    order_date: datetime
    items: List[Item]
