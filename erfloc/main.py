from fastapi import FastAPI
from erfloc.routes import coords, forms

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(coords.router, prefix='/api/coords')
app.include_router(forms.router)

app.mount("/static", StaticFiles(directory="erfloc/statics", packages=["erfloc"], html=True), name="static")