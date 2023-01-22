
# Fast File Backup App

[![Build Status](https://img.shields.io/badge/lang-T%C3%BCrk%C3%A7e-red)](https://github.com/BerkKilicoglu/Fast-File-Backup-App/blob/main/README.tr.md) [![Build Status](https://img.shields.io/badge/lang-English-blue)](https://github.com/BerkKilicoglu/Fast-File-Backup-App/blob/main/README.md)

![FileBackup Gif1](https://media.giphy.com/media/D010h0DYlZJpcjHalt/giphy.gif)
![FileBackup Gif2](https://media.giphy.com/media/4XsVoileeQMtUakEhL/giphy.gif)

File Backup desktop application. The application allows you to quickly backup your files, easily track the backed up files, and recover them back.

## Features

- Backup to files can be **the local computer** and on **Google Drive**.

- You can view all your backups in detail in the **dashboard** section and recover your files quickly.

- With the automatic backup feature, you can set a time period and back up files automatically during that period.

- You can exclude specific files or file types from the backup.

- Files that have not been modified, that are already available, will not be backed up again. It does this control with hash(MD5). [to improve performance.]

- You can create new backup points for a backed up folder and keep backups of different versions of it at the same time.

## Requirements

**OS**: Windows, Linux or MacOS

**Google Drive API**
> If you are a developer and want to make the google drive feature of this application available to your users: create a developer account at cloud.google.com and create a new credentials (credentials.json) for Google API
- **pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib**  with it you can install all the libraries needed.

## Authors

 - [BerkKilicoglu](https://github.com/BerkKilicoglu)
 - [emrecpp](https://github.com/emrecpp)
