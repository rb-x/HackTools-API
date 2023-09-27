from fastapi.testclient import TestClient
from io import BytesIO
from app.main import app

client = TestClient(app)

def test_sam_decryption():
    # Replace 'your file content' with the appropriate file content for testing.
    file_data = b"your file content"
    file_like_object = BytesIO(file_data)

    response = client.post(
        "/decrypt/sam",
        files={
            "sam": ("sam_filename", file_like_object, "application/octet-stream"),
            "system": ("system_filename", file_like_object, "application/octet-stream"),
            "security": ("security_filename", file_like_object, "application/octet-stream"),
        },
    )

    assert response.status_code == 200

def test_ntds_decryption():
    pass