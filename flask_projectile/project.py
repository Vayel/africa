import os

from projectile.downloader import DriveDocumentDownloader
from projectile.reader import LibreOfficeDocumentReader
from projectile.uploader import DriveDocumentUploader
from projectile.project import TrelloProject
from projectile.tools import Drive, Trello

import javelot.config


class Project(TrelloProject):
    def __init__(self, url):
        trello = Trello(
            api_key=os.environ['TRELLO_API_KEY'],
            api_secret_path=os.environ['TRELLO_API_SECRET_PATH'],
            app_name=os.environ['API_APP_NAME'],
        )

        super().__init__(
            url=url,
            trello=trello,
            design_list_id=os.environ['TRELLO_DESIGN_LIST_ID'],
            quality_member_card_url=os.environ['TRELLO_QUALITY_MEMBER_CARD_URL'],
            quality_chief_card_url=os.environ['TRELLO_QUALITY_CHIEF_CARD_URL'],
            path=os.environ['PROJECT_FOLDER'],
            output_dirname=javelot.config.PDF_DIRNAME,
            document_dirname='documents'
        )
        
        self.reader = LibreOfficeDocumentReader(
            db_name=self.slug,
            path=self.get_document_path(),
        )

        app_drive = Drive(
            api_key_path=os.environ['GOOGLE_API_KEY_PATH'],
            credentials_path=os.environ['GOOGLE_APP_CREDENTIAL_PATH'],
            scopes='https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.readonly',
            app_name=os.environ['API_APP_NAME'],
        )
        self.downloader = DriveDocumentDownloader(
            drive=app_drive,
            folder_id=os.environ['GOOGLE_TEMPLATE_DRIVE_ID'],
            path=self.get_document_path(),
        )
        
        user_drive = Drive(
            api_key_path=os.environ['GOOGLE_API_KEY_PATH'],
            credentials_path=os.environ['GOOGLE_USER_CREDENTIAL_PATH'],
            scopes='https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.readonly',
            app_name=os.environ['API_APP_NAME'],
        )
        self.uploader = DriveDocumentUploader(
            root_dirname=self.name,
            validated_dirname='Validés',
            drive=user_drive,
            path=self.get_output_path(),
        )
