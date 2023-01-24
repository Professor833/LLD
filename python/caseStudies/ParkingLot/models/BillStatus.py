from .BaseModel import BaseModel
from enum import Enum
from typing import Optional

class BillStatus(BaseModel, Enum):
    PAID = 1
    UNPAID = 2
