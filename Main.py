# -*- coding: utf-8 -*-
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui


from file_backup_gui import homepage
class Main(QMainWindow):
    selectedFiles = []
    def __init__(self):
        super().__init__()
        self.homepage = homepage(parent=self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec())