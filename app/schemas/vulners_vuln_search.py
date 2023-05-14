# app/schemas/file_upload.py
from pydantic import BaseModel

class VulnersVulnSearch(BaseModel):
    service: str