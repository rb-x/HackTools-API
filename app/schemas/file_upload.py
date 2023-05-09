# app/schemas/file_upload.py
from pydantic import BaseModel
from fastapi import UploadFile

class FileUpload(BaseModel):
    sam: UploadFile
    system: UploadFile
    security: UploadFile
    ntds: UploadFile
