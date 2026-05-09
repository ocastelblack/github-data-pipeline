from google.oauth2 import service_account

from googleapiclient.discovery import build

from googleapiclient.http import MediaFileUpload

from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/drive']

SERVICE_ACCOUNT_FILE = 'credentials.json'

FOLDER_ID = '1_U75_PTY7Qs3RJqxKFTeyGpswQhLbGEW'


def upload_file(file_path):

    try:

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )

        service = build(
            'drive',
            'v3',
            credentials=credentials
        )

        file_metadata = {
            'name': file_path,
            'parents': [FOLDER_ID]
        }

        media = MediaFileUpload(
            file_path,
            mimetype='text/csv'
        )

        uploaded_file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True
        ).execute()

        print(
            f"Archivo subido a Drive. ID: {uploaded_file.get('id')}"
        )

    except HttpError as e:

        print("No fue posible subir el archivo a Google Drive")

        print(f"Detalle: {e}")

        print(
            "El reporte fue generado correctamente de forma local."
        )