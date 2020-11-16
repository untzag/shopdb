from pydantic import BaseModel
from typing import List
from model.vendor import Vendor


class Part(BaseModel):
    part_id: int
    manufacturer: str
    mpn: str
    description: str
    note: str
    vendors: List[Vendor]
