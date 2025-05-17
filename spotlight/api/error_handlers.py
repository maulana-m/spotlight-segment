from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, List
import re
import http
import logging


logger = logging.getLogger(__name__)


def _camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).upper()


def error_response(error: Exception, error_code: int = 500, descriptions: Optional[List] = None):
    if descriptions is None:
        descriptions = []

    status = http.HTTPStatus(error_code).name

    if isinstance(error, HTTPException):
        name = error.detail.replace(" ", "")
        error_code = error.status_code
    else:
        name = error.__class__.__name__

        error_message = [
            {"field": desc[0], "message": desc[1]} for desc in descriptions
        ]

    return JSONResponse(
        dict(
            status=status,
            error=_camel_to_snake(name),
            code=error_code,
            descriptions=error_message,
        ),
        status_code=error_code,
    )


async def bad_request_exception_handler(_, error: Exception):
    return error_response(error, 400)


async def request_validation_handler(_: Request, error: RequestValidationError):
    validation_errors = [(".".join(str(x) for x in e["loc"]), e["type"])
                         for e in error.errors()]
    return error_response(error, 400, validation_errors)
