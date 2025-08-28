from fastapi import APIRouter

route = APIRouter(prefix = "/api")

from controller.text_analyzer.controller import TextAnalyzerController
from controller.debugger.controller import DebuggerController

route.include_router(TextAnalyzerController.router, prefix="/v1/text-analyzer")
route.include_router(DebuggerController.router, prefix="/debug")