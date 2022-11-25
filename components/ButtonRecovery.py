# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QSize, QObject, QTimer, QPoint, QEasingCurve, QParallelAnimationGroup, QAbstractAnimation, \
    QPropertyAnimation, pyqtSignal

from PyQt5.QtGui import *

class ButtonRecovery(QPushButton):
    def __init__(self, dictSaveInfo:dict):
        super().__init__()
        self.dictSaveInfo = dictSaveInfo
        self.setText("Recover")