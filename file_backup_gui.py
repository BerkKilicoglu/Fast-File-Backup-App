import sys, os
from Utils import Utils
utils = Utils()
PYSIDE6_DAN_PYQT5_CEVIR = True
if PYSIDE6_DAN_PYQT5_CEVIR: # Bu Qt Designer kullanıp ui dosyasını pythona cevirince pyside6 olarak çeviriyor pyqt5 bende bulamadım kodla hallediyorum
    for Dosya in ["ui_homepage.py"]:
        DosyaKonum = f"{os.getcwd()}{os.sep}{Dosya.replace('/', os.sep)}"
        if os.path.exists(DosyaKonum):
            with open(DosyaKonum, 'r') as f: # r+ yada w+ çalışmadı
                okunan = f.read()
            with open(DosyaKonum, 'w') as f:
                f.write(okunan.replace("PySide2", "PyQt5"))
        else:
            print("PyQt5 cevirmek icin dosya bulunamadi: ", DosyaKonum)

from PyQt5.QtWidgets import QApplication, QMainWindow

import ui_homepage
from PyQt5 import QtGui


class homepage(object):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
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
        self.parent.selectedFiles = []
        for file in mime.urls():
            self.parent.selectedFiles.append(utils.pathConvert(file.toLocalFile()))
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

