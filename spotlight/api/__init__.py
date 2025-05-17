from spotlight.api.routers import segments
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from spotlight.api.error_handlers import request_validation_handler


app = FastAPI()
app.include_router(segments.router)
app.exception_handler(RequestValidationError)(request_validation_handler)
