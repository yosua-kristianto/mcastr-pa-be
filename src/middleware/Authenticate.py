from http.client import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from common.facade.encryption import hash, verify_hash
import json

class Authenticate(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        unguarded_check = [
            "/api/debug/hash",
        ]

        print(f"Request path: {request.url.path}")

        # ✅ Skip auth if path is in whitelist
        if request.url.path in unguarded_check:
            return await call_next(request)
        
        if(request.headers.get("X-AUTH-TOKEN") is None):
            raise HTTPException(status_code=401, detail="Unauthorized")

        token = request.headers.get("X-AUTH-TOKEN") 

        body = await request.body()

        def minify_json(json_str: str) -> str:
            parsed = json.loads(json_str)  # parse into Python dict
            return json.dumps(parsed, separators=(",", ":"))  # minify (no spaces/newlines)

        json_request = minify_json(body.decode("utf-8"))

        print(body)
        print(json_request)

        if(not verify_hash(token, hash(json_request))):
           raise HTTPException(status_code=403, detail="Invalid token")
        
        return await call_next(request)