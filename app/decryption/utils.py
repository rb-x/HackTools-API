# app/decryption/utils.py
from pypykatz.registry.offline_parser import OffineRegistry
import json

def decrypt_sam(sam_data: bytes, system_data: bytes):
    result = OffineRegistry.from_bytes(system_data, sam_data).to_json()
    # JSON compaction
    result = json.loads(result)
    return result

def decrypt_ntds(ntds_data, system_data, security_data):
    #TODO: Implement the NTDS decryption logic 
    pass
