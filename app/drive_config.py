import json

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

import io


SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

SERVICE_ACCOUNT_FILE = 'credentials.json'

FILE_ID = '1j9MAzPRY9R_LjfzhW3taPmRot96rdMvO'


def get_repositories():

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    service = build(
        'drive',
        'v3',
        credentials=credentials
    )

    request = service.files().get_media(
        fileId=FILE_ID
    )

    file_stream = io.BytesIO()

    downloader = MediaIoBaseDownload(
        file_stream,
        request
    )

    done = False

    while not done:
        status, done = downloader.next_chunk()

    file_stream.seek(0)

    content = file_stream.read().decode('utf-8')

    config = json.loads(content)

    return config["repositories"]