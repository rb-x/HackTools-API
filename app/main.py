from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import secrets
from app.decryption import sam, ntds, lsass
from app.services import vulners
import logging,os


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

@app.middleware("http")
async def check_api_key(request, call_next):
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        return JSONResponse(status_code=401, content={"detail": "Invalid API key."})
    try:
        response = await call_next(request)
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": "An internal error occurred."})
    
    return response

app.include_router(vulners.router, prefix="/vulners", tags=["Vulners API"])
app.include_router(sam.router, prefix="/decrypt/sam", tags=["SAM Decryption"])
app.include_router(ntds.router, prefix="/decrypt/ntds", tags=["NTDS Decryption"])
app.include_router(lsass.router, prefix="/decrypt/lsass", tags=["LSASS dump"])
 