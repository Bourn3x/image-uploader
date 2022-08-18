from pathlib import Path
test_files = Path(__file__).parent / "test-files"

# When a user calls POST /upload with no file key in body
# Then a BadRequestError 400 should be raised
def test_upload_missing_file_key(client):
  response = client.post("/upload", data = {})
  assert response.status_code == 400

# When a user calls POST /upload with file key, but no file attached
# Then a BadRequestError 400 should be raised
def test_upload_empty_file(client):
  response = client.post("/upload", data = {
    "file": None,
  })
  assert response.status_code == 400

# When a user calls POST /upload with a non-picture file extension
# Then a BadRequestError 400 should be raised
def test_upload_invalid_file_extension(client):
  response = client.post("/upload", data = {
    "file": (test_files / "notapic.txt").open("rb")
  })
  assert response.status_code == 400

  response = client.post("/upload", data = {
    "file": (test_files / "notapic.docx").open("rb")
  })
  assert response.status_code == 400

  response = client.post("/upload", data = {
    "file": (test_files / "notapic.rtf").open("rb")
  })
  assert response.status_code == 400

# When a user calls POST /upload with a string with valid file extension instead of a file
# Then a BadRequestError 400 should be raised
def test_upload_invalid_value_type(client):
  response = client.post("/upload", data = {
    "file": "hello.png"
  })
  assert response.status_code == 400
