# app/decryption/ntds.py
from fastapi import APIRouter, File, UploadFile
from app.schemas.vulners_vuln_search import VulnersVulnSearch
from os.path import join, dirname
from dotenv import load_dotenv
import vulners,os

router = APIRouter()

vulners_api = vulners.Vulners(api_key=os.getenv("VULNERS_API_KEY"))


@router.post("/")
# get a json {"service": "xxx"}
async def vulners_vuln_reserach(vulners_vuln_search: VulnersVulnSearch):
    
    # return the body 
    try :
        result = vulners_api.searchExploit(vulners_vuln_search.service)
    except Exception as e:
        print(e)
    # result = vulners_vuln_search.service
    return result