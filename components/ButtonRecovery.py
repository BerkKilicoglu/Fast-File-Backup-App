# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QSize, QObject, QTimer, QPoint, QEasingCurve, QParallelAnimationGroup, QAbstractAnimation, \
    QPropertyAnimation, pyqtSignal

from PyQt5.QtGui import *
from Sync import Sync
class ButtonRecovery(QPushButton):
    def __init__(self, backupName:str, dictSaveInfo:dict, parent=None):
        super().__init__(parent)
        self.backupName, self.dictSaveInfo, self.widParent = backupName, dictSaveInfo, parent
        self.setText("Recover")
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("background-color:rgb(0,0,100);color:white")
        self.clicked.connect(self.Tiklandi)
    def Tiklandi(self):
        try:

            SrcPath, DesPath = self.widParent.Settings["sourceLocation"], self.widParent.Settings["backupLocation"]
            SrcPath, DesPath = DesPath, SrcPath
            totalChangedFiles = Sync(backupName=self.backupName, Src=SrcPath, Des=DesPath, ExcludedFileTypes=[],
                                     ui=self.widParent.getUi())
            self.widParent.getUi().lblStatus.setText(f"<b>Status: </b> Restored {totalChangedFiles} files.")
        except Exception as err:
            self.utils.hataKodGoster("ButtonRecovery click: %s"%str(err))
