# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtCore import Qt, QSize, QObject, QTimer, QPoint, QEasingCurve, QParallelAnimationGroup, QAbstractAnimation, \
    QPropertyAnimation, pyqtSignal

from PyQt5.QtGui import *
from queue import Queue

class EStackedWidgetSliding(QStackedWidget):
    def __init__(self, parent=None):
        super(EStackedWidgetSliding, self).__init__(parent)
        self.init(parent)
    QueueToShowWidget = Queue() # her seferinde yeni olusturmayi unutma yoksa kayma oluyor next widget -1 donuyor

    def init(self, parent=None):
        self.QueueToShowWidget = Queue() #bu olmazsa index karisiyor next index -1 geliyor büyük bug oluyor (tetiklenmeyi şöyle bulabilirsin: self.ui.stackedTopBar.slideInWgt(self.ui.topBar_Ayarlar) bunu iki kez alt alta yaz (not stackedTopBar olmalı)). ALT ALTA 2 kez yazilinca 2. cagirisinta kuyruga ekliyor, kuyruktada diğer ana ui.forms'a kayiyor (kuyruk ramde yeni olusturulmadigi icin) bu seferde bulamiyor -1 donuyor
        self.parent = parent
        self.m_direction = Qt.Vertical
        self.m_speed = 800#400
        # OutBack, yukarı gidip tekrar geliyor
        # OutCubic güzel, biraz lag lı ama
        # OutQuart güzel
        # OutExpo da olabilir idare eder
        self.m_animationtype = QEasingCurve.OutCubic  # OutCubic
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnow = QPoint(0, 0)
        self.m_active = False
        #self.tmrShowWidgets = QTimer(self)
        #self.tmrShowWidgets.timeout.connect(self.TmrShowWidgetsFunc)
        #self.tmrShowWidgets.setInterval(500)
        #self.tmrShowWidgets.start()

    def setDirection(self, direction):
        self.m_direction = direction

    def setSpeed(self, speed):
        self.m_speed = speed

    def setAnimation(self, animationtype):
        self.m_animationtype = animationtype

    def setWrap(self, wrap):
        self.m_wrap = wrap

    @QtCore.pyqtSlot()
    def slideInPrev(self):
        now = self.currentIndex()
        if self.m_wrap or now > 0:
            self.slideInIdx(now - 1)

    @QtCore.pyqtSlot()
    def slideInNext(self):
        now = self.currentIndex()
        if self.m_wrap or now < (self.count() - 1):
            self.slideInIdx(now + 1)

    def slideInIdx(self, idx):
        if idx > (self.count() - 1):
            idx = idx % self.count()
        elif idx < 0:
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx))

    def slideInWgt(self, newwidget) -> bool:
        if self.m_active:
            self.QueueToShowWidget.put(newwidget) # eğer ard arda beklenmeden tıklandıysa kuyruğa ekliyor
            return False

        self.m_active = True

        _now = self.currentIndex()
        _next = self.indexOf(newwidget) # Not: -1 gelirse print(self.count())'a ve animationDoneSlot slotuna dikkat et, widget gizleme falan yapıyor heralde
        if _next == -1:
            print("StackedWidgetSliding next: -1")
        if _now == _next:
            self.m_active = False
            return False
        if not hasattr(self.parent, "frameRect"): # yeni tasarıma geçiriken böyle bir hata çıktı, bu versiyon öncekinde çalışıyor halbuki, uğraşılırsa çözülür yani
            self.parent.frameRect = self.rect
        offsetx, offsety = self.parent.frameRect().width(), self.parent.frameRect().height()
        if self.widget(_next) == None:
            print("EStackedwidget next none")
            print("[self.widget(x) for x in range(self.count())]:\n")
            listWidgets = [str(self.widget(x)) for x in range(self.count())]
            print("\n".join(listWidgets))
            print(f"\n_now:{_now} - next: {_next} - newWidget:\n{str(newwidget)}")
            breakpoint()
        self.widget(_next).setGeometry(self.parent.frameRect())

        if not self.m_direction == Qt.Horizontal:
            if _now < _next:
                offsetx, offsety = 0, -offsety
            else:
                offsetx = 0
        else:
            if _now < _next:
                offsetx, offsety = -offsetx, 0
            else:
                offsety = 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()
        self.m_pnow = pnow

        offset = QPoint(offsetx, offsety)
        self.widget(_next).move(pnext - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        anim_group = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        for index, start, end in zip(
                (_now, _next), (pnow, pnext - offset), (pnow + offset, pnext)
        ):
            animation = QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.m_speed,
                easingCurve=self.m_animationtype,
                startValue=start,
                endValue=end,
            )
            anim_group.addAnimation(animation)

        self.m_next = _next
        self.m_now = _now
        self.m_active = True
        anim_group.start(QAbstractAnimation.DeleteWhenStopped)
        return True

    @QtCore.pyqtSlot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnow)
        self.m_active = False
        if self.QueueToShowWidget.empty(): return
        Wid = self.QueueToShowWidget.get()
        if not self.slideInWgt(Wid): # beklemeden ard arda tıklanırsa tüm sayfalar yüklendikten sonra diğerine geçmesi lazım yoksa görüntü iç içe geçiyor, bu işlemde onu yapıyor
            self.QueueToShowWidget.put(Wid)