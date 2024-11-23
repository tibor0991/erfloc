from fastapi import Form, APIRouter, Request
from datetime import datetime
from typing import Annotated
from erfloc.dependencies.geoloc import GeolocatorDep
from erfloc.dependencies.templates import TemplateDep

router = APIRouter()

@router.post("/site/get-coords")
async def get_coords(request: Request, location: Annotated[str, Form()], observation_time: Annotated[datetime, Form()], geolocator: GeolocatorDep, template: TemplateDep):
    coords = geolocator.get_eci_coords(location, observation_time)
    return template.TemplateResponse(
        request=request,
        name="eci_coords.html.j2",
        context={**coords.model_dump()}
    )




