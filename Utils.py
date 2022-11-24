# -*- coding: utf-8 -*-
import sys, os, traceback
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os, json


class Utils():
    def __init__(self, widParent):
        super().__init__()
        self.widParent = widParent
    def isWindows(self) -> bool:
        return os.name == 'nt'
    def pathConvert(self, path:str)->str:
        if self.isWindows():
            return path.replace("/", "\\").replace("\\\\","\\")
        else:
            return path.replace("\\\\", "/").replace("\\", "/")

    def hataKodGoster(self, err=""):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        if exc_type == None and exc_obj == None and exc_tb == None:
            return
        # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        fname = exc_tb.tb_frame.f_code.co_filename
        hataStr = "%s %s %s %s\nTraceback: %s" % (str(err), exc_type, fname, exc_tb.tb_lineno, traceback.format_exc())
        print(hataStr)

    def msgHata(self, hata):
        try:
            msgBox = QMessageBox(self.widParent)


            font = QFont('Arial', 12)
            msgBox.setFont(font)
            # font = QFont(self.fontAdi_Exo2, 14)
            msgBox.setWindowTitle("Error")
            msgBox.setText(hata)
            #msgBox.setWindowIcon(QIcon(":/logo/assets/logo/error.png"))

            msgBox.setIconPixmap(QPixmap(":/logo/assets/logo/error.png").scaled(QSize(48,48),Qt.KeepAspectRatio, Qt.SmoothTransformation))
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.button(QMessageBox.Yes).setText('OK')
            msgBox.button(QMessageBox.Yes).setFont(font)
            msgBox.exec_()
        except Exception as err:
            self.hataKodGoster("Utils msgHata: %s" % str(err))

    def msgUyariUnlem(self, baslik, mesaj, topmost=False):
        try:
            msgBox = QMessageBox(self.widParent)

            #msgBox.setWindowIcon(QIcon(":/logo/assets/logo/check.png"))
            msgBox.setFont(QFont('Calibri', 11, weight=QFont.Bold))
            msgBox.setWindowTitle(baslik)
            msgBox.setText(mesaj)
            msgBox.setIconPixmap(QPixmap(':/logo/assets/logo/check.png'))
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.button(QMessageBox.Yes).setText('Tamam')
            msgBox.exec_()
        except Exception as err:
            self.hataKodGoster("Utils msgUyariUnlem: %s" % str(err))