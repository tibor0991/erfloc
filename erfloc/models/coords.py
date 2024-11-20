from pydantic import BaseModel
from datetime import datetime

class XYZ(BaseModel):
    x: float
    y: float
    z: float

class ECI(BaseModel):
    location: str
    obstime: datetime
    coords: XYZ
