from fastapi import FastAPI
from erfloc.routes import coords

app = FastAPI()

app.include_router(coords.router, prefix='/api/coords')