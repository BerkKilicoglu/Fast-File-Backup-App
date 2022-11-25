# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QSize, QObject, QTimer, QPoint, QEasingCurve, QParallelAnimationGroup, QAbstractAnimation, \
    QPropertyAnimation, pyqtSignal

from PyQt5.QtGui import *

class ETableWidgetItem(QTableWidgetItem):
    def __init__(self, text="", center=True):
        super().__init__()
        self.setText(text)
        if center: self.setTextAlignment(Qt.AlignCenter)
