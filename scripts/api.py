import uvicorn
from pydantic import BaseModel, RootModel
from fastapi import FastAPI
from typing import List
import json
class Fingerprint(BaseModel):
    os: str
    window_size: int
    window_scale: int
    ttl: int
    options_length: int
    mss: int

class FingerprintDatabase(RootModel):
    root: List[Fingerprint]

f = open("data.json")
data = json.load(f)
f.close()
fingerprint_database = FingerprintDatabase(root=data)

app = FastAPI()


@app.get("/search/")
async def search(
    window_size: int | None = None,
    window_scale: int | None = None,
    ttl: int | None = None,
    options_length: int | None = None,
    mss: int | None = None):
    return find(window_size, window_scale, ttl, options_length, mss)

@app.get("/os/")
async def search(os: str):
    fingerprints = []
    for fingerprint in fingerprint_database.root:
        if os.lower() in fingerprint.os.lower():
            fingerprints.append(fingerprint)
    return fingerprints

# Eventually the goal would be to use an actual query system like SQL

def find(
    window_size: int | None = None,
    window_scale: int | None = None,
    ttl: int | None = None,
    options_length: int | None = None,
    mss: int | None = None):
    for fingerprint in fingerprint_database.root:
        if (fingerprint.window_size is not window_size) and (window_size is not None):
            continue
        if (fingerprint.window_scale is not window_scale) and (window_scale is not None):
            continue
        if (fingerprint.ttl is not ttl) and (ttl is not None):
            continue
        if (fingerprint.options_length is not options_length) and (options_length is not None):
            continue
        if (fingerprint.mss is not mss) and (mss is not None):
            continue
        return fingerprint
    return {}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
