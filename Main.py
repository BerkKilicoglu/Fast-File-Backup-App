# -*- coding: utf-8 -*-
import sys, os, json, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5 import QtGui, Qt
from Sync import GetFileMD5, CopyFile, GetFilesNameList, Sync
from components.ETableWidgetItem import ETableWidgetItem
from components.ButtonRecovery import ButtonRecovery
from datetime import datetime
from driveSync import *


from Utils import Utils
if __name__ == "__main__":
    from file_backup_gui import homepage
class Main(QMainWindow):
    #selectedDirectories = []
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
            ui.label_drvsource.setText("Source Location: " + ((" <font color='black'><b>" + self.Settings["sourceLocation"] + "</b></font>")
                                                              if self.Settings["sourceLocation"] else " <b>(Not Set)</b>"))
            ui.txtBackupName_Drive.setText(self.Settings["backupName"])
            ui.lineEdit_filetype_Drive.setText(";".join(self.Settings["excludeFileTypes"]))
            ui.label_drvbackup.setText("Backup Location: " + (" <font color='black'><b>drive.google.com/drive/" + self.Settings["backupName"]+"</b></font>"))


            ui.cmbBackupPeriod.setCurrentText(self.Settings["autoBackupPeriod"])

            liste = self.getUi().tableDashboard
            liste.setRowCount(0)
            liste.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            for key, value in self.Settings["saves"].items():
                backupName = key
                index = liste.rowCount()
                liste.insertRow(index)
                liste.setItem(index, 0, ETableWidgetItem(backupName))
                liste.setItem(index, 1, ETableWidgetItem(str(value["date"])))
                liste.setItem(index, 2, ETableWidgetItem(str(value["totalChangedFiles"])))
                liste.setCellWidget(index, 3, ButtonRecovery(backupName=backupName, dictSaveInfo=value, parent=self))

        except Exception as err:
            self.utils.hataKodGoster("RefreshGui: %s"%str(err))
    def getUi(self):
        return self.homepage.ui
    def BackupNow(self) -> bool:
        try:
            backupName = self.getUi().txtBackupName.text().strip()
            ExcludedFileTypes = self.getUi().lineEdit_filetype.text().split(";")
            AutoBackup = self.getUi().chkAutoBackup.isChecked()
            while "" in ExcludedFileTypes:
                ExcludedFileTypes.remove("")
            if not backupName:
                self.utils.msgHata("Please enter backup name.")
                return False
            if backupName in self.Settings["saves"] and not AutoBackup:
                answer = self.utils.msgOverWrite()
                if answer:
                    DateNow = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
                    backupName = f"{backupName}{'_'}{DateNow}"

            Src = self.Settings["sourceLocation"]
            Des = self.Settings["backupLocation"]
            if not Src or not Des or not os.path.exists(Src)\
                    or not os.path.isdir(Src)\
                    or Src == Des:# or not os.path.exists(Des):
                self.utils.msgHata(f"Please be sure you have selected Source Location & Backup location and These locations are directories.\nAlso they can't be the same.\n\n\nSrc Location: {Src}\n\nDes Location: {Des}")
                return False
            totalChangedFiles = Sync(backupName=backupName, Src=Src, Des=Des, ExcludedFileTypes=ExcludedFileTypes, ui=self.getUi())
            if totalChangedFiles != 0:
                self.getUi().lblStatus.setText(f"<b>Status:</b> {totalChangedFiles} files copied on {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}.")
                self.utils.msgUyariUnlem("Success", f"{totalChangedFiles} files copied! (Same files skipped for performance)", False)
            else:
                self.getUi().lblStatus.setText(f"<b>Status:</b> Already up to date on {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}.")


            self.Settings["dateLastBackup"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            DictSaveInfo = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "totalChangedFiles": totalChangedFiles

            }
            if backupName not in self.Settings["saves"]:
                self.Settings["saves"][backupName] = {}
            self.Settings["saves"][backupName] = DictSaveInfo
            self.SaveSettings()
            self.RefreshGui() # for add to dashboard list
            
            if AutoBackup:
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
        "dateLastBackup": "",
        "saves":{}
    }
    SETTINGS_PATH = "Settings.json"

    def DriveBackupNow(self):
        try:
            backupName = self.getUi().txtBackupName_Drive.text().strip()
            ExcludedFileTypes = self.getUi().lineEdit_filetype_Drive.text().split(";")
            while "" in ExcludedFileTypes:
                ExcludedFileTypes.remove("")
            if not backupName:
                self.utils.msgHata("Please enter backup name.")
                return False
            DriveSrc = self.Settings["sourceLocation"]
            if not DriveSrc or not os.path.exists(DriveSrc) \
                    or not os.path.isdir(DriveSrc):  # or not os.path.exists(Des):
                self.utils.msgHata(
                    f"Please be sure you have selected Source Location & Backup location and These locations are directories.\nAlso they can't be the same.\n\n\nSrc Location: {DriveSrc}\n\n")
                return False

            drive = MyDrive()
            processedFiles = GetFilesNameList(DriveSrc, excluded=ExcludedFileTypes, removeSrcDir=False)

            num_files = len(processedFiles)
            drive.uploadFiles(backupName, processedFiles, totalChangedFiles=num_files, ui=self.getUi())

            if num_files != 0:
                self.getUi().lblStatus.setText(
                    f"<b>Status:</b> {num_files} files copied on {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}.")
                self.utils.msgUyariUnlem("Success",
                                         f"{num_files} files copied! (Same files skipped for performance)",
                                         False)
            else:
                self.getUi().lblStatus.setText(
                    f"<b>Status:</b> Already up to date on {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}.")

            self.Settings["dateLastBackup"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            DictSaveInfo = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "totalChangedFiles": num_files

            }
            if backupName not in self.Settings["saves"]:
                self.Settings["saves"][backupName] = {}
            self.Settings["saves"][backupName] = DictSaveInfo
            self.SaveSettings()
            self.RefreshGui()  # for add to dashboard list



        except Exception as err:
            self.utils.hataKodGoster("[DEBUG] Drive Errors: %s" % str(err))

    Settings = {
        "backupName": "",
        "sourceLocation": "",
        "backupLocation": "",
        "excludeFileTypes": [],
        "autoBackupEnabled": 0,
        "autoBackupPeriod": "1 min",
        "dateLastBackup": "",
        "saves": {}
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