from fastapi import APIRouter

route = APIRouter(prefix = "/api")

from controller.text_analyzer.controller import TextAnalyzerController

route.include_router(TextAnalyzerController.router, prefix="/v1/text-analyzer")