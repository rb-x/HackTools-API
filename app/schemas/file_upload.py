# app/schemas/file_upload.py
from pydantic import BaseModel
from fastapi import UploadFile

class FileUpload(BaseModel):
    sam: UploadFile
    system: UploadFile
    security: UploadFile
    ntds: UploadFile


# LSASS upload ase B64 json
class LSASS_B64DUMP(BaseModel):
    lsass: str