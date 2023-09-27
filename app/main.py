from fastapi import FastAPI, HTTPException, Depends, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import secrets
from app.routes.windows import sam, ntds, lsass
from app.services import vulners
import logging,os
from typing import Optional

logger = logging.getLogger("api_key_logger")
dev = os.environ.get("DEV")
API_KEY = secrets.token_urlsafe(32) if not dev else "test"

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def on_startup():
    logger.warning(f" | API key: {API_KEY}")

def api_key_check(request: Request):
    api_key = request.headers.get('x-api-key', None)
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key.")
    return api_key

class AuthenticatedRouter(APIRouter):
    def add_api_route(self, *args, **kwargs):
        if "dependencies" not in kwargs:
            kwargs["dependencies"] = []
        kwargs["dependencies"].append(Depends(api_key_check))
        super().add_api_route(*args, **kwargs)

router = AuthenticatedRouter()

@app.get("/ping")
async def ping():
    return {"status": "success"}

@app.get("/auth_check")
async def auth_check(api_key: str = Depends(api_key_check)):
    return {"status": "success"}

app.include_router(vulners.router, prefix="/vulners", tags=["Vulners API"])
app.include_router(sam.router, prefix="/decrypt/sam", tags=["SAM Decryption"])
app.include_router(ntds.router, prefix="/decrypt/ntds", tags=["NTDS Decryption"])
app.include_router(lsass.router, prefix="/decrypt/lsass", tags=["LSASS dump"])