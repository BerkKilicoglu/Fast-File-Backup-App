# -*- coding: utf-8 -*-
import sys, os, json, time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

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
            ui.label_blocation.setText("Backup Location" + ((": <b>" + self.Settings["backupLocation"] + "</b>") if self.Settings["backupLocation"] else " <b>(Not Set)</b>"))
            ui.lineEdit_filetype.setText(";".join(self.Settings["excludeFileTypes"]))
        except Exception as err:
            self.utils.hataKodGoster("RefreshGui: %s"%str(err))
    def getUi(self):
        return self.homepage.ui
    def BackupNow(self) -> bool:
        try:
            ProjectName = self.getUi().txtBackupName.text().strip()
            if not ProjectName:
                self.utils.msgHata("Please enter backup name.")
                return False
        except Exception as err:
            self.utils.hataKodGoster("BackupNow: %s" % str(err))
    Settings = {
        "backupLocation": "",
        "excludeFileTypes":[]
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