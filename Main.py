# -*- coding: utf-8 -*-
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

from Utils import Utils
from file_backup_gui import homepage
class Main(QMainWindow):
    selectedFiles = []
    def __init__(self):
        super().__init__()
        self.utils = Utils(widParent=self)
        self.homepage = homepage(parent=self)

    def getUi(self):
        return self.homepage.ui
    def BackupNow(self) -> bool:
        ProjectName = self.getUi().txtBackupName.text().strip()
        if not ProjectName:
            self.utils.msgHata("Please enter backup name.")
            return False
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec())