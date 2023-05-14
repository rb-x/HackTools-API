# app/decryption/ntds.py
from fastapi import APIRouter, File, UploadFile
from app.schemas.file_upload import LSASS_B64DUMP
from app.decryption.utils import dump_lsass


router = APIRouter()

@router.post("/")
async def lsass_dump(lsass: UploadFile):
    lsass = await lsass.read()
    result = dump_lsass(lsass)
    return result
