from pydantic import BaseModel
from typing import List


class POI(BaseModel):
id: str
name: str
city: str
lat: float
lon: float
tags: List[str]
price: str
rating: float
