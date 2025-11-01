from fastapi import APIRouter, Request
from config.config import settings

from model.object.base_response_dto import BaseResponse

from common.facade.encryption import hash

import json

class DebuggerController:

    router = APIRouter()

    @router.post("/hash")
    async def get_token_hasher(request: Request):
        """DEBUG ONLY

        Generate token based-on request.
        
        -- """

        if not settings.app_debug:
            raise Exception("This endpoint is only available in debug mode.")

        def minify_json(json_str: str) -> str:
            parsed = json.loads(json_str)  # parse into Python dict
            return json.dumps(parsed, separators=(",", ":"))  # minify (no spaces/newlines)

        body = await request.body()

        json_request = minify_json(body.decode("utf-8"))

        return BaseResponse.ok(
            message = "Hash generated",
            data = {
                "token": hash(json_request),
                "original_request": json_request
            }
        )


    