import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from PyQt5.QtWidgets import QApplication

#yetkilendirme ve kimlik doğrulama
class MyDrive():
    def __init__(self):
        # If modify SCOPES, delete the token.json
        SCOPES = ["https://www.googleapis.com/auth/drive"]

        creds = None
        # The file token.json stores the user's access and created automatically
        # when the authorization flow completes for the first time
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        # If no credentials are available, allow the user to log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save credentials for next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build("drive", "v3", credentials=creds)


    def uploadFiles(self, BackupName, SrcPath, totalChangedFiles, ui=None):
        try:
            files = SrcPath
            response = self.service.files().list(
                q="name='" + BackupName + "' and mimeType='application/vnd.google-apps.folder'",
                spaces='drive'
            ).execute()

            if not response['files']:
                file_metadata = {
                    "name": "{}".format(BackupName),
                    "mimeType":"application/vnd.google-apps.folder"
                }

                file = self.service.files().create(body=file_metadata, fields="id").execute()

                folder_id = file.get('id')
            else:
                folder_id = response['files'][0]['id']

            counter = 1

            for file in files:  #os.listdir(SrcPath)

                QApplication.processEvents()
                file_name = os.path.basename(file)
                file_metadata = {
                    "name": file_name,
                    "parents": [folder_id]
                }

                media = MediaFileUpload(f"{file}") #media = MediaFileUpload(f"{SrcPath}/{file}")

                upload_file = self.service.files().create(body=file_metadata,
                                                          media_body=media,
                                                          fields="id").execute()
                if ui:
                    ui.lblStatus.setText(
                        f"<b>Status: </b> File copying ({file_name}) {totalChangedFiles}/{counter} {((counter / totalChangedFiles ) * 100):.2f}%")
                    QApplication.processEvents()

                counter += 1
                print("[DEBUG] Backed up file: " + file)


        except HttpError as erros:
            print("[DEBUG] Error: " + str(erros))
