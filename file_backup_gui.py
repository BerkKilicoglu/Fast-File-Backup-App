# -*- coding: utf-8 -*-
import sys, os, time, webbrowser
from datetime import datetime, timedelta
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
    tmrAutoBackup:QTimer = None

    def __init__(self, parent:Main.Main):
        super().__init__()
        self.parent, self.utils = parent, parent.utils
        self.tmrAutoBackup = QTimer(self.parent)
        self.tmrAutoBackup.setInterval(1000)
        self.tmrAutoBackup.timeout.connect(self.CalculateAutoBackupTimer)
        self.ui = ui_homepage.Ui_MainWindow()
        self.ui.setupUi(parent)



        # Show & Hide Left Menu
        self.ui.menuBtn.clicked.connect(self.menu_hide_unhide)
        self.hidden = False
        ######

        self.ui.lblRemainingTimeToAutoBackup.setVisible(False) # default hiden
        self.ui.label_brand.setWordWrap(True)

        self.ui.pushButton_2_Dashboard.clicked.connect(lambda: self.menusection(storage=False, dashboard=True, googleDrive=False))
        self.ui.pushButton_Storage.clicked.connect(lambda: self.menusection(storage=True, dashboard=False, googleDrive=False))
        self.ui.pushButton_gDrive.clicked.connect(lambda: self.menusection(storage=False, dashboard=False, googleDrive=True))
        self.ui.frame_upload.dragEnterEvent = self.SurukleEnterEvent
        self.ui.frame_upload.dragLeaveEvent = self.SurukleLeaveEvent
        self.ui.frame_upload.dropEvent = self.SurukleDropEvent

        self.ui.frame_Drive.dragEnterEvent = self.SurukleEnterEvent
        self.ui.frame_Drive.dragLeaveEvent = self.SurukleLeaveEvent
        self.ui.frame_Drive.dropEvent = self.SurukleDropEvent

        self.ui.btnBackupNow.clicked.connect(self.parent.BackupNow)
        self.ui.btnDriveBackup.clicked.connect(self.parent.DriveBackupNow)
        self.ui.btnSelectSrcDirectory.clicked.connect(self.SelectSourceDir)
        self.ui.pushButton_srcDirDrive.clicked.connect(self.SelectSourceDir)
        self.ui.btnSelectLocation.clicked.connect(self.SelectBackupDir)
        self.ui.txtBackupName.textChanged.connect(self.BackupNameDegisti)
        self.ui.lineEdit_filetype.textChanged.connect(self.FilterTypeDegisti)
        self.ui.lineEdit_search.textChanged.connect(self.SearchDegisti)
        self.ui.txtBackupName_Drive.textChanged.connect(self.BackupNameDegisti)
        self.ui.lineEdit_filetype_Drive.textChanged.connect(self.FilterTypeDegisti)

        def releaseGitEmre(eventRelease):
            if eventRelease.button() != Qt.LeftButton:
                return
            webbrowser.open("https://www.github.com/emrecpp")
        def releaseGitBerk(eventRelease):
            if eventRelease.button() != Qt.LeftButton:
                return
            webbrowser.open("https://www.github.com/berkkilicoglu")

        self.ui.btnGitEmre.mouseReleaseEvent = releaseGitEmre
        self.ui.btnGitBerk.mouseReleaseEvent = releaseGitBerk

        def changedAutoBackup(newState:int):
            self.ui.frameAutoBackup.setEnabled(newState)
            self.parent.Settings["autoBackupEnabled"] = bool(newState)
            self.parent.SaveSettings()
            self.ui.cmbBackupPeriod.setEnabled(newState)


        self.ui.chkAutoBackup.stateChanged.connect(changedAutoBackup)
        def changedAutoBackupPeriod(newPeriod:str):
            self.parent.Settings["autoBackupPeriod"] = newPeriod
            self.parent.SaveSettings()

        self.ui.cmbBackupPeriod.currentTextChanged.connect(changedAutoBackupPeriod)

    periodInSeconds = 60
    def CalculateAutoBackupTimer(self):
        if not self.parent.Settings["autoBackupEnabled"]: return
        backupStartedDate = datetime.strptime(self.parent.Settings["dateLastBackup"], "%Y-%m-%d %H:%M:%S")


        targetDate = (backupStartedDate + timedelta(seconds=self.periodInSeconds))
        calculatedDate = (targetDate - datetime.now())
        differenceInSeconds = calculatedDate.seconds
        day = calculatedDate.days
        time = differenceInSeconds % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        if day <= 0:
            self.ui.lblRemainingTimeToAutoBackup.setText(f"{hour:02}:{minutes:02}:{seconds:02}")
        elif day == 1:
            self.ui.lblRemainingTimeToAutoBackup.setText(f"{day:02} day, {hour:02}:{minutes:02}:{seconds:02}")
        elif day > 1:
            self.ui.lblRemainingTimeToAutoBackup.setText(f"{day:02} days, {hour:02}:{minutes:02}:{seconds:02}")

        #print(targetDate, day, time, hour, seconds)

        if day == 0 and differenceInSeconds <= 0:
            print("[DEBUG] Auto backup triggered.")
            self.tmrAutoBackup.stop() # stopped timer

            self.ui.lblRemainingTimeToAutoBackup.setPixmap(QPixmap(':/logo/assets/logo/check.png').scaled(QSize(16,16), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.parent.BackupNow() # this will start timer again



    def BackupNameDegisti(self, newText:str):
        try:
            self.parent.Settings["backupName"] = newText
            self.parent.SaveSettings()
            self.parent.RefreshGui()
        except Exception as err:
            self.utils.hataKodGoster("BackupNameDegisti: %s"%str(err))
    def FilterTypeDegisti(self, newText:str):
        try:
            self.parent.Settings["excludeFileTypes"] = newText.replace(",",";").replace("-",";").replace("|",";").replace("&",";").split(";")
            self.parent.SaveSettings()
        except Exception as err:
            self.utils.hataKodGoster("FileTypeDegisti: %s"%str(err))
    def SearchDegisti(self, newText:str):
        try:
            onStoragePage = not self.onDashboard#self.ui.stackedWidget_2.currentWidget() == self.ui.pageStorage
            if onStoragePage:
                self.menusection(storage=False,dashboard=True, googleDrive=False)
                #self.ui.stackedWidget_2.slideInWgt(self.ui.pageDashboard)
            for i in range(self.ui.tableDashboard.rowCount()):
                BackupName = self.ui.tableDashboard.item(i, 0).text()
                Date = self.ui.tableDashboard.item(i, 1).text()
                if (newText.lower() in BackupName.lower()) or (newText.lower() in Date):
                    self.ui.tableDashboard.showRow(i)
                else:
                    self.ui.tableDashboard.hideRow(i)
        except Exception as err:
            self.utils.hataKodGoster("SearchDegisti: %s" % str(err))
    def SelectSourceDir(self):
        folderBackupDir = QFileDialog.getExistingDirectory(self.parent, 'Select Source Directory')
        if not folderBackupDir:
            return
        folderBackupDir = self.utils.pathConvert(folderBackupDir)
        self.parent.Settings["sourceLocation"] = folderBackupDir
        self.parent.SaveSettings()
        self.parent.RefreshGui()
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
        #self.parent.selectedDirectories = []
        for file in mime.urls():
            CorrectPath = self.utils.pathConvert(file.toLocalFile())
            if os.path.isdir(CorrectPath):
                self.parent.Settings["sourceLocation"] = CorrectPath
                self.parent.SaveSettings()
                self.parent.RefreshGui()
                break # does not supported multiple directories yet
                #self.parent.selectedDirectories.append(CorrectPath)
            else:
                print(f"{CorrectPath} klasor olmadigi icin selectedDirectories'e eklenmedi!")
        self.dragEnter=False


    onDashboard = False
    onGoogleDrive = False
    def menusection(self, storage, dashboard, googleDrive):
        dashboard_noneclicked = "background-color: #415AAF;"
        dashboard_clicked = "background-color: #FEFEFF;border-top-left-radius: 20px; color: #415AAF"
        storage_noneclicked = "background-color: #415AAF; color: black;"
        storage_clicked = "background-color: #FEFEFF; color: #415AAF;"
        drive_clicked = "background-color: #FEFEFF; border-top-left-radius:20px; color: #00AC47"
        drive_noneclicked = "background-color: #415AAF;"

        if dashboard:
            self.onDashboard=True
            self.onGoogleDrive = False
            self.ui.stackedWidget_2.slideInWgt(self.ui.pageDashboard)
            self.ui.pushButton_2_Dashboard.setStyleSheet(dashboard_clicked)
            self.ui.pushButton_Storage.setStyleSheet(storage_noneclicked)
            self.ui.pushButton_gDrive.setStyleSheet(drive_noneclicked)
            self.ui.pushButton_2_Dashboard.setIcon(QtGui.QIcon("assets/icons/nightblue/home.svg"))
            self.ui.pushButton_Storage.setIcon(QtGui.QIcon("assets/icons/white/package.svg"))
            self.ui.pushButton_gDrive.setIcon(QtGui.QIcon("assets/logo/googleDrive.png"))
            self.ui.solMenu.setStyleSheet("background-color:#415AAF")
            self.ui.label_menuname.setText("Dashboard")
        if storage:
            self.onDashboard=False
            self.onGoogleDrive = False
            self.ui.stackedWidget_2.slideInWgt(self.ui.pageStorage)
            self.ui.pushButton_Storage.setStyleSheet(storage_clicked)
            self.ui.pushButton_2_Dashboard.setStyleSheet(dashboard_noneclicked)
            self.ui.pushButton_gDrive.setStyleSheet(drive_noneclicked)
            self.ui.pushButton_Storage.setIcon(QtGui.QIcon("assets/icons/nightblue/package.svg"))
            self.ui.pushButton_2_Dashboard.setIcon(QtGui.QIcon("assets/icons/white/home.svg"))
            self.ui.pushButton_gDrive.setIcon(QtGui.QIcon("assets/logo/googleDrive.png"))
            self.ui.solMenu.setStyleSheet("background-color:#415AAF")
            self.ui.label_menuname.setText("Storage")
        if googleDrive:
            self.onDashboard=False
            self.onGoogleDrive = True
            self.ui.stackedWidget_2.slideInWgt(self.ui.pageDrive)
            self.ui.pushButton_gDrive.setStyleSheet(drive_clicked)
            self.ui.pushButton_Storage.setStyleSheet(storage_noneclicked+"background-color: #00AC47")
            self.ui.pushButton_2_Dashboard.setStyleSheet(dashboard_noneclicked+"background-color: #00AC47")
            self.ui.pushButton_gDrive.setIcon(QtGui.QIcon("assets/logo/googleDrive2.png"))
            self.ui.pushButton_Storage.setIcon(QtGui.QIcon("assets/icons/white/package.svg"))
            self.ui.pushButton_2_Dashboard.setIcon(QtGui.QIcon("assets/icons/white/home.svg"))
            self.ui.solMenu.setStyleSheet("background-color:#00AC47")
            self.ui.label_menuname.setText("Google Drive")
            self.ui.label_menuname.setStyleSheet("color: #00AC47")
            self.ui.frame_search.setStyleSheet("border-radius: 10px; border: 2px solid #00ac47")
            self.ui.lineEdit_search.setStyleSheet("border:none;color:green")
            self.ui.label_searchicon.setStyleSheet("border:none")
            self.ui.label_searchicon.setPixmap(QPixmap("assets/icons/green/search.svg"))
            self.ui.menuBtn.setIcon(QIcon("assets/icons/green/menu.svg"))
        else:
            self.ui.label_menuname.setStyleSheet("color: #415AAF")
            self.ui.frame_search.setStyleSheet("border-radius: 10px; border: 2px solid #415AAF")
            self.ui.lineEdit_search.setStyleSheet("border:none;color:#415AAF")
            self.ui.label_searchicon.setStyleSheet("border:none")
            self.ui.label_searchicon.setPixmap(QPixmap("assets/icons/nightblue/search.svg"))
            self.ui.menuBtn.setIcon(QIcon("assets/icons/nightblue/menu.svg"))







    SolMenuWidth = -1
    def menu_hide_unhide(self):
        if self.hidden:

            self.anim = QPropertyAnimation(self.ui.solMenu, b'maximumWidth')
            self.anim.setEasingCurve(QEasingCurve.InOutQuad)
            self.anim.setDuration(400)
            self.anim.setEndValue(self.SolMenuWidth)
            self.anim.start()


            self.ui.solMenu.show()
            self.hidden = False
        else:
            if self.SolMenuWidth == -1: self.SolMenuWidth =self.ui.solMenu.width() # dynamic size after loaded GUI

            self.anim = QPropertyAnimation(self.ui.solMenu, b'maximumWidth')
            self.anim.setEasingCurve(QEasingCurve.InOutQuad)
            self.anim.setDuration(400)
            self.anim.setEndValue(0)
            self.anim.start()
            def End():
                self.ui.solMenu.hide()

            self.anim.finished.connect(End)
            self.hidden = True

