# -*- coding: utf-8 -*-
import sys, os

import Main

PYSIDE6_DAN_PYQT5_CEVIR = True
if PYSIDE6_DAN_PYQT5_CEVIR: # Bu Qt Designer kullanıp ui dosyasını pythona cevirince pyside6 olarak çeviriyor pyqt5 bende bulamadım kodla hallediyorum
    for Dosya in ["ui_homepage.py"]:
        DosyaKonum = f"{os.getcwd()}{os.sep}{Dosya.replace('/', os.sep)}"
        if os.path.exists(DosyaKonum):
            with open(DosyaKonum, 'r') as f: # r+ yada w+ çalışmadı
                okunan = f.read()
            with open(DosyaKonum, 'w') as f:
                f.write(okunan.replace("PySide2", "PyQt5").replace("PySide6", "PyQt5"))
        else:
            print("PyQt5 cevirmek icin dosya bulunamadi: ", DosyaKonum)

from PyQt5.QtWidgets import QApplication, QMainWindow

import ui_homepage
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class homepage(object):
    def __init__(self, parent:Main.Main):
        super().__init__()
        self.parent, self.utils = parent, parent.utils
        self.ui = ui_homepage.Ui_MainWindow()
        self.ui.setupUi(parent)



        # Show & Hide Left Menu
        self.ui.menuBtn.clicked.connect(self.menu_hide_unhide)
        self.hidden = False
        ######
        self.ui.label_brand.setWordWrap(True)

        self.ui.pushButton_2_Dashboard.clicked.connect(lambda: self.menusection(storage=False, dashboard=True))
        self.ui.pushButton_Storage.clicked.connect(lambda: self.menusection(storage=True, dashboard=False))
        self.ui.frame_upload.dragEnterEvent = self.SurukleEnterEvent
        self.ui.frame_upload.dragLeaveEvent = self.SurukleLeaveEvent
        self.ui.frame_upload.dropEvent = self.SurukleDropEvent

        self.ui.btnBackupNow.clicked.connect(self.parent.BackupNow)
        self.ui.btnSelectLocation.clicked.connect(self.SelectBackupDir)
        self.ui.lineEdit_filetype.textChanged.connect(self.FileTypeDegisti)

    def FileTypeDegisti(self, newText:str):
        try:
            self.parent.Settings["excludeFileTypes"] = newText.replace(",",";").replace("-",";").replace("|",";").replace("&",";").split(";")
            self.parent.SaveSettings()
        except Exception as err:
            self.utils.hataKodGoster("FileTypeDegisti: %s"%str(err))
    def SelectBackupDir(self):
        folderBackupDir = QFileDialog.getExistingDirectory(self.parent, 'Select Backup Directory')
        if not folderBackupDir:
            return
        folderBackupDir = self.utils.pathConvert(folderBackupDir)
        self.parent.Settings["backupLocation"] = folderBackupDir
        self.parent.SaveSettings()
        self.parent.RefreshGui()

    dragEnter = False
    def SurukleEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.dragEnter=True
            event.accept()
        else:
            event.ignore()
    def SurukleLeaveEvent(self,event):
        self.dragEnter=False
    def SurukleDropEvent(self,event):
        mime = event.mimeData()
        self.parent.selectedDirectories = []
        for file in mime.urls():
            CorrectPath = self.utils.pathConvert(file.toLocalFile())
            if os.path.isdir(CorrectPath):
                self.parent.selectedDirectories.append(CorrectPath)
            else:
                print(f"{CorrectPath} klasor olmadigi icin selectedDirectories'e eklenmedi!")
        self.dragEnter=False



    def menusection(self, storage, dashboard):
        if dashboard:
            self.ui.stackedWidget_2.slideInWgt(self.ui.pageDashboard)
            self.ui.pushButton_2_Dashboard.setStyleSheet("background-color: #FEFEFF;border-top-left-radius: 20px; color: #415AAF")
            self.ui.pushButton_Storage.setStyleSheet("background-color: #415AAF; color: black;")
            self.ui.pushButton_2_Dashboard.setIcon(QtGui.QIcon("assets/icons/nightblue/home.svg"))
            self.ui.pushButton_Storage.setIcon(QtGui.QIcon("assets/icons/white/package.svg"))
        if storage:
            self.ui.stackedWidget_2.slideInWgt(self.ui.pageStorage)
            self.ui.pushButton_Storage.setStyleSheet("background-color: #FEFEFF; color: #415AAF")
            self.ui.pushButton_2_Dashboard.setStyleSheet("background-color: #415AAF;")
            self.ui.pushButton_Storage.setIcon(QtGui.QIcon("assets/icons/nightblue/package.svg"))
            self.ui.pushButton_2_Dashboard.setIcon(QtGui.QIcon("assets/icons/white/home.svg"))



    def menu_hide_unhide(self):
        if self.hidden:
            self.ui.solMenu.show()
            self.hidden = False
        else:
            self.ui.solMenu.hide()
            self.hidden = True

