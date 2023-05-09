# app/decryption/ntds.py
from fastapi import APIRouter, File, UploadFile
from .utils import decrypt_ntds

router = APIRouter()

@router.post("/")
async def decrypt_ntds_file(ntds: UploadFile = File(...), system: UploadFile = File(...), security: UploadFile = File(...)):
    #  TODO: Implement the NTDS decryption logic using pypykatz or another library
    ntds_data = await ntds.read()
    system_data = await system.read()
    security_data = await security.read()

    result = decrypt_ntds(ntds_data, system_data, security_data)
    return result
