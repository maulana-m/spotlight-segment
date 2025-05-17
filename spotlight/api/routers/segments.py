from fastapi.routing import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
from spotlight.core.config import GENERAL_CONFIG
from spotlight.core.downloader import Downloader
from spotlight.core.service import SpotlightService
from spotlight.core.llm import GeminiApi
from spotlight.core.dto import SpotlightRequest


router = APIRouter()

spotlight_service = SpotlightService(
    _downloader=Downloader(),
    llm=GeminiApi()
)


@router.post("/segments/")
async def segments(request: Request, spotlight_request: SpotlightRequest):
    response = await spotlight_service.run(spotlight_request)

    return JSONResponse(
        dict(data=response, status="success")
    )

