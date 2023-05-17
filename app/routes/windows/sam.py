# app/decryption/sam.py
from fastapi import APIRouter, File, UploadFile
from .utils import decrypt_sam


router = APIRouter()


@router.post("/")
async def decrypt_sam_file(sam: UploadFile = File(...) , system: UploadFile = File(...)):
    # WARNING:multipart.multipart:Did not find boundary character 104 at index 2
    
    sam_data = await sam.read()
    system_data = await system.read()

    result = decrypt_sam(sam_data, system_data)
    return result
