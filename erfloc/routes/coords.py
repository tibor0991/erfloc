from fastapi import APIRouter
from erfloc.dependencies.geoloc import GeolocatorDep
from datetime import datetime

router = APIRouter()

@router.get("/lla/")
async def get_lla_coords(geoloc: GeolocatorDep, location: str):
    return geoloc.get_lla_coords(location)

@router.get("/eci/")
async def get_lla_coords(geoloc: GeolocatorDep, location: str, obstime: datetime = datetime.now()):
    return geoloc.get_eci_coords(location, obstime)


