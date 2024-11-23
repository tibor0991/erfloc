from geopy.geocoders import Nominatim
from functools import cache
from fastapi import Depends

from astropy.coordinates import EarthLocation
from astropy.time import Time
from datetime import datetime
from erfloc.models import coords
from typing import Annotated

class Geolocator:
    def __init__(self,):
        self.__geolocator = Nominatim(user_agent='erfloc')

    def get_lla_coords(self, location: str):
        loc = self.__geolocator.geocode(location)
        return loc.longitude, loc.latitude, loc.altitude
    
    def get_eci_coords(self, location: str, obstime: datetime):
        lon, lat, _ = self.get_lla_coords(location)
        pos, _ = EarthLocation.from_geodetic(lon, lat).get_gcrs_posvel(obstime=Time(val=obstime))
        x,y,z = [float(f.to_value()) for f in pos.get_xyz()]
        return coords.ECI(location=location, obstime=obstime, coords=coords.XYZ(x=x,y=y,z=z))

@cache
def get_geolocator():
    return Geolocator()

GeolocatorDep = Annotated[Geolocator, Depends(get_geolocator)]







