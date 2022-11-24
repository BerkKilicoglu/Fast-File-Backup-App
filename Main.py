# -*- coding: utf-8 -*-
import sys, os, json, time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from Sync import GetFileMD5, CopyFile, GetFilesNameList
from datetime import datetime

from Utils import Utils
if __name__ == "__main__":
    from file_backup_gui import homepage
class Main(QMainWindow):
    selectedDirectories = []
    def __init__(self):
        super().__init__()

        self.utils = Utils(widParent=self)
        self.homepage = homepage(parent=self)
        self.LoadSettings()
        self.RefreshGui()

    def RefreshGui(self):
        try:
            ui = self.getUi()
            ui.label_source.setText("Source Location: " + ((" <font color='black'><b>" + self.Settings["sourceLocation"] + "</b></font>") if self.Settings["sourceLocation"] else " <b>(Not Set)</b>"))
            ui.label_backup.setText("Backup Location: " + ((" <font color='black'><b>" + self.Settings["backupLocation"] + "</b></font>") if self.Settings["backupLocation"] else " <b>(Not Set)</b>"))
            ui.txtBackupName.setText(self.Settings["backupName"])
            ui.lineEdit_filetype.setText(";".join(self.Settings["excludeFileTypes"]))
            ui.chkAutoBackup.setChecked(self.Settings["autoBackupEnabled"])


            ui.cmbBackupPeriod.setCurrentText(self.Settings["autoBackupPeriod"])
        except Exception as err:
            self.utils.hataKodGoster("RefreshGui: %s"%str(err))
    def getUi(self):
        return self.homepage.ui
    def BackupNow(self) -> bool:
        try:
            backupName = self.getUi().txtBackupName.text().strip()
            ExcludedFileTypes = self.getUi().lineEdit_filetype.text().split(";")
            if not backupName:
                self.utils.msgHata("Please enter backup name.")
                return False
            Src = self.Settings["sourceLocation"]
            Des = self.Settings["backupLocation"]
            if not Src or not Des or not os.path.exists(Src)\
                    or not os.path.isdir(Src)\
                    or Src == Des:# or not os.path.exists(Des):
                self.utils.msgHata(f"Please be sure you have selected Source Location & Backup location and These locations are directories.\nAlso they can't be the same.\n\n\nSrc Location: {Src}\n\nDes Location: {Des}")
                return False
            ProcessedFilesInSrc = GetFilesNameList(Src, excluded=ExcludedFileTypes, removeSrcDir=False)#, FilesInDes = GetFilesNameList(Src, [".txt"]), GetFilesNameList(Des)
            if True:
                DestinationPath = f"{Des}{os.sep}{backupName}"
            else: # new version, optional backup.
                DateNow = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
                DestinationPath = f"{Des}{os.sep}{backupName}{os.sep}{DateNow}"
            os.makedirs(DestinationPath, exist_ok=True)
            totalChangedFiles = 0
            for FileSrc in ProcessedFilesInSrc:
                ResultDes = FileSrc.replace(Src, DestinationPath)
                ParsedFileName = FileSrc.replace(Src, "")
                if len(ParsedFileName) > 0: # For safety.
                    ParsedFileName = ParsedFileName[1:] # Remove os.sep in first character
                if os.path.exists(ResultDes): # For more performance, hash compare, if hashes are the same; it will not copy.
                    hashSrc = GetFileMD5(FileSrc)
                    hashDes = GetFileMD5(ResultDes)
                    if hashSrc == hashDes:
                        print("Not copied file: %s [Files are the same]" % str(FileSrc))
                        continue

                if CopyFile(FileSrc, ResultDes):
                    totalChangedFiles += 1
                else:
                    print("[ERR] File: %s not copied (CopyFile is false)" % str(FileSrc))

                self.getUi().lblStatus.setText(f"<b>Status: </b> File copying ({ParsedFileName}) {totalChangedFiles}/{len(ProcessedFilesInSrc)} {((totalChangedFiles)/len(ProcessedFilesInSrc)*100)}%")

            if totalChangedFiles != 0:
                self.getUi().lblStatus.setText(f"<b>Status:</b> {totalChangedFiles} files copied on {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}.")
                self.utils.msgUyariUnlem("Success", f"{totalChangedFiles} files copied! (Same files skipped for performance)", False)
            else:
                self.getUi().lblStatus.setText(f"<b>Status:</b> Already up to date on {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}.")


            self.Settings["dateLastBackup"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.SaveSettings()
            
            
            if self.getUi().chkAutoBackup.isChecked():
                self.getUi().lblRemainingTimeToAutoBackup.setVisible(True)
                selectedPeriod = self.getUi().cmbBackupPeriod.currentText()
                self.homepage.periodInSeconds = 60
                if selectedPeriod in ["5 sec", "5 secs", "5 seconds"]:
                    self.homepage.periodInSeconds = 5
                elif selectedPeriod == "1 min":
                    self.homepage.periodInSeconds = 60
                elif selectedPeriod == "5 min":
                    self.homepage.periodInSeconds = 60 * 5
                elif selectedPeriod == "1 hour":
                    self.homepage.periodInSeconds = 60 * 60
                elif selectedPeriod == "12 hours":
                    self.homepage.periodInSeconds = 60 * 60 * 12
                elif selectedPeriod == "1 day":
                    self.homepage.periodInSeconds = 60 * 60 * 24
                elif selectedPeriod == "1 week":
                    self.homepage.periodInSeconds = 60 * 60 * 24 * 7
                elif selectedPeriod == "1 month":
                    self.homepage.periodInSeconds = 60 * 60 * 24 * 30
                self.homepage.periodInSeconds += 2 # QTimer starts 1 second later delay

                self.homepage.tmrAutoBackup.start(1000)
            else:
                self.getUi().lblRemainingTimeToAutoBackup.setVisible(False)
                self.homepage.tmrAutoBackup.stop()

        except Exception as err:
            self.utils.hataKodGoster("BackupNow: %s" % str(err))
    Settings = {
        "backupName":"",
        "sourceLocation": "",
        "backupLocation": "",
        "excludeFileTypes":[],
        "autoBackupEnabled": 0,
        "autoBackupPeriod":"1 min",
        "dateLastBackup": ""
    }
    SETTINGS_PATH = "Settings.json"
    def LoadSettings(self):
        try:
            if not os.path.exists(self.SETTINGS_PATH):
                return
            with open(self.SETTINGS_PATH, 'r', encoding='utf-8') as f:
                self.Settings = json.loads(f.read())
        except Exception as err:
            self.utils.hataKodGoster("LoadSettings: %s"%str(err))
    def SaveSettings(self):
        try:
            with open(self.SETTINGS_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.Settings, f, ensure_ascii=False, indent=4)
        except Exception as err:
            self.utils.hataKodGoster("SaveSettings: %s"%str(err))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec())