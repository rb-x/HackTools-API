# app/decryption/utils.py
from pypykatz.registry.offline_parser import OffineRegistry
from pypykatz.pypykatz import pypykatz
from base64 import b64decode
import json

def decrypt_sam(sam_data: bytes, system_data: bytes):
    result = OffineRegistry.from_bytes(system_data, sam_data).to_json()
    # JSON compaction
    result = json.loads(result)
    return result

def decrypt_ntds(ntds_data, system_data, security_data):
    #TODO: Implement the NTDS decryption logic 
    pass


def dump_lsass(lsass_dump: bytes):
    # lsass will be sent as a base64 encoded string
    # lsass:bytes = b64decode(lsass_dump)
    result = pypykatz.parse_minidump_bytes(lsass_dump).to_json()
    # JSON compaction
    result = json.loads(result)
    return result


# dump lsass memory




