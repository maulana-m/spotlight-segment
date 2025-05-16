from spotlight.api.routers import segments
from fastapi import FastAPI


app = FastAPI()
app.include_router(segments.router)
