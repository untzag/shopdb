from pydantic import BaseModel


class Vendor(BaseModel):
    vendor_id: int
    name: str
    website: str
    note: str
