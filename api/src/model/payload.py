from pydantic import BaseModel


class Payload(BaseModel):
    part_id: int
    manufacturer: str
    mpn: str
