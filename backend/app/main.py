# backend/app/main.py (top imports)
import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from planner import generate_itineraries
from fastapi.middleware.cors import CORSMiddleware


FRONTEND_URL = os.getenv('FRONTEND_URL', '*')


app = FastAPI()
app.add_middleware(
CORSMiddleware,
allow_origins=[FRONTEND_URL] if FRONTEND_URL != '*' else ['*'],
allow_methods=['*'],
allow_headers=['*'],
)


class TripRequest(BaseModel):
destination: str
start_date: str
end_date: str
budget: str
preferences: dict = {}


@app.post('/api/trips')
def create_trip(req: TripRequest):
itineraries = generate_itineraries(req.dict())
return {"trip": req.dict(), "itineraries": itineraries}


@app.get('/api/pois')
def list_pois():
here = os.path.dirname(__file__)
path = os.path.join(here, 'data', 'sample_pois.json')
with open(path,'r') as f:
data = json.load(f)
return data


@app.get('/healthz')
def health():
return {"status":"ok"}

