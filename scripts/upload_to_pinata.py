from pathlib import Path
import os
import requests

PINATA_BASE_URL = "https://api.pinata.cloud"
PIN_FILE_ENDPOINT = "/pinning/pinFileToIPFS"
HEADERS = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def upload_to_pinata():
    filepath = "./img/dragon.png"
    filename = filepath.split("/")[-1]

    with Path(filepath).open("rb") as fp:
        imageBinary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + PIN_FILE_ENDPOINT,
            files={"file": (filename, imageBinary)},
            headers=HEADERS,
        )
        print(response.json())


def main():
    upload_to_pinata()