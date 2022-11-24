# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepagesfCaEC.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from components.EStackedWidgetSliding import EStackedWidgetSliding

import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 851)
        icon = QIcon()
        icon.addFile(u":/logo/assets/logo/BerkEmreLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"QLineEdit#lineEdit_search{\n"
"border:none\n"
"}\n"
"#centralwidget{\n"
"	background-color: #EFF9FE;\n"
"}\n"
"\n"
"#header, #uploadfiles, #uploadsettings{\n"
"	background-color: #FEFEFF;\n"
"}\n"
"\n"
"#solMenu{\n"
"	background-color: #415AAF;\n"
"}\n"
"\n"
"#lineEdit_filetype {\n"
"	background-color: #E5E5E5;\n"
"color:#415AAF;\n"
"}\n"
"\n"
"#txtBackupName{\n"
"	color: #415AAF;\n"
"	background-color: #E5E5E5;\n"
"}\n"
"#lineEdit_search{\n"
"	\n"
"	color: #415AAF\n"
"}\n"
"\n"
"#frame_search{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #415AAF;\n"
"}\n"
"\n"
"#label_menuname{\n"
"	color: #415AAF;\n"
"}\n"
"\n"
"#frame_upload{\n"
"	border-radius: 10px;\n"
"	border: 1.8px dotted #619EF1;\n"
"	background-color: #F5F8FC;\n"
"}\n"
"\n"
"#pushButton_selectfile, #btnSelectLocation{\n"
"	background-color: #415AAF;\n"
"	border-radius: 25px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"#btnSelectLocation::hover, #btnSelectLocation::hover{\n"
""
                        "	background-color: #1F2A5B;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#pushButton_selectfile::pressed, #btnSelectLocation::pressed{\n"
"	background-color: #8BA0D6;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#lineEdit_filetype, #txtBackupName{\n"
"	border-radius: 10px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#btnBackupNow{\n"
"	font: 75 10pt \"Microsoft YaHei UI\";\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"	border: 3px solid  rgb(61, 217, 245);\n"
"	border-radius:60px;\n"
"}\n"
"#btnBackupNow::hover{\n"
"	font: 75 10pt \"Microsoft YaHei UI\";\n"
"	font-weight: bold;\n"
"	color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1F2A5B, stop:1 #8BA0D6);\n"
"	border: 3px solid #8BA0D6;\n"
"	border-radius:60px;\n"
"}\n"
"#btnBackupNow::pressed{\n"
"	font: 75 10pt \"Microsoft YaHei UI\";\n"
"	"
                        "font-weight: bold;\n"
"	color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #415AAF, stop:1 #D4F1FF);\n"
"	border: 3px solid #D4F1FF;\n"
"	border-radius:60px;\n"
"}\n"
"\n"
"#pushButton_Storage{\n"
"	color: #415AAF;\n"
"	background-color: #FEFEFF;\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"	border-top-left-radius: 20px;\n"
"}\n"
"\n"
"#pushButton_2_Dashboard{\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"#btnGitBerk, #btnGitEmre{\n"
"	background-color: #415AAF;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: none;\n"
"	background-color: rgb(65,90,175, .7);\n"
"	color: 	white;\n"
"	font-weight: bold;\n"
"	padding: 3px;	\n"
"}\n"
"\n"
"QComboBox:on{\n"
"    background-color: rgb(65,90,175, .5);\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.solMenu = QWidget(self.centralwidget)
        self.solMenu.setObjectName(u"solMenu")
        self.solMenu.setMaximumSize(QSize(275, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.solMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 0, 0, 0)
        self.frame_menumain = QFrame(self.solMenu)
        self.frame_menumain.setObjectName(u"frame_menumain")
        self.frame_menumain.setFrameShape(QFrame.StyledPanel)
        self.frame_menumain.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_menumain)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_brand = QFrame(self.frame_menumain)
        self.frame_brand.setObjectName(u"frame_brand")
        self.frame_brand.setFrameShape(QFrame.StyledPanel)
        self.frame_brand.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_brand)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.frame_brand)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.label_brand = QLabel(self.frame_brand)
        self.label_brand.setObjectName(u"label_brand")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_brand.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_brand)


        self.verticalLayout_10.addWidget(self.frame_brand, 0, Qt.AlignTop)

        self.frame_menusection = QFrame(self.frame_menumain)
        self.frame_menusection.setObjectName(u"frame_menusection")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menusection.sizePolicy().hasHeightForWidth())
        self.frame_menusection.setSizePolicy(sizePolicy)
        self.frame_menusection.setFrameShape(QFrame.StyledPanel)
        self.frame_menusection.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_menusection)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_2 = QSpacerItem(87, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.frame_section = QFrame(self.frame_menusection)
        self.frame_section.setObjectName(u"frame_section")
        self.frame_section.setFrameShape(QFrame.StyledPanel)
        self.frame_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_section)
        self.verticalLayout_12.setSpacing(50)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Storage = QPushButton(self.frame_section)
        self.pushButton_Storage.setObjectName(u"pushButton_Storage")
        self.pushButton_Storage.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_Storage.setFont(font2)
        self.pushButton_Storage.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/nightblueIcons/assets/icons/nightblue/package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Storage.setIcon(icon1)
        self.pushButton_Storage.setIconSize(QSize(32, 32))
        self.pushButton_Storage.setCheckable(True)
        self.pushButton_Storage.setChecked(False)

        self.verticalLayout_12.addWidget(self.pushButton_Storage)

        self.pushButton_2_Dashboard = QPushButton(self.frame_section)
        self.pushButton_2_Dashboard.setObjectName(u"pushButton_2_Dashboard")
        self.pushButton_2_Dashboard.setMinimumSize(QSize(0, 50))
        self.pushButton_2_Dashboard.setFont(font2)
        self.pushButton_2_Dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/whiteIcons/assets/icons/white/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2_Dashboard.setIcon(icon2)
        self.pushButton_2_Dashboard.setIconSize(QSize(32, 32))
        self.pushButton_2_Dashboard.setCheckable(True)
        self.pushButton_2_Dashboard.setChecked(False)

        self.verticalLayout_12.addWidget(self.pushButton_2_Dashboard)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.gridLayout_5.addWidget(self.frame_section, 1, 0, 1, 4)

        self.label = QLabel(self.frame_menusection)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(128, 128))
        self.label.setPixmap(QPixmap(u":/logo/assets/logo/GitHub-Mark-Light-64px.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(88, 45, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.frame_git = QFrame(self.frame_menusection)
        self.frame_git.setObjectName(u"frame_git")
        self.frame_git.setFrameShape(QFrame.StyledPanel)
        self.frame_git.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_git)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnGitBerk = QPushButton(self.frame_git)
        self.btnGitBerk.setObjectName(u"btnGitBerk")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.btnGitBerk.setFont(font3)
        self.btnGitBerk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGitBerk.setIconSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.btnGitBerk)

        self.btnGitEmre = QPushButton(self.frame_git)
        self.btnGitEmre.setObjectName(u"btnGitEmre")
        self.btnGitEmre.setFont(font3)
        self.btnGitEmre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGitEmre.setIconSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.btnGitEmre)


        self.gridLayout_5.addWidget(self.frame_git, 3, 0, 1, 4)


        self.verticalLayout_10.addWidget(self.frame_menusection)


        self.verticalLayout_9.addWidget(self.frame_menumain)


        self.gridLayout_6.addWidget(self.solMenu, 0, 0, 1, 1)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.h_section = QWidget(self.header)
        self.h_section.setObjectName(u"h_section")
        self.horizontalLayout_3 = QHBoxLayout(self.h_section)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.h_section)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/nightblueIcons/assets/icons/nightblue/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon3)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)

        self.label_menuname = QLabel(self.h_section)
        self.label_menuname.setObjectName(u"label_menuname")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_menuname.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_menuname)


        self.horizontalLayout_2.addWidget(self.h_section)

        self.h_search = QWidget(self.header)
        self.h_search.setObjectName(u"h_search")
        self.horizontalLayout_4 = QHBoxLayout(self.h_search)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.frame_search = QFrame(self.h_search)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(250, 0))
        self.frame_search.setMaximumSize(QSize(250, 16777215))
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 9, -1)
        self.label_searchicon = QLabel(self.frame_search)
        self.label_searchicon.setObjectName(u"label_searchicon")
        self.label_searchicon.setMinimumSize(QSize(30, 30))
        self.label_searchicon.setMaximumSize(QSize(30, 30))
        self.label_searchicon.setPixmap(QPixmap(u":/nightblueIcons/assets/icons/nightblue/search.svg"))
        self.label_searchicon.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_searchicon)

        self.lineEdit_search = QLineEdit(self.frame_search)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setFont(font)

        self.horizontalLayout_5.addWidget(self.lineEdit_search)


        self.horizontalLayout_4.addWidget(self.frame_search, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.h_search)

        self.h_profile = QWidget(self.header)
        self.h_profile.setObjectName(u"h_profile")
        self.verticalLayout_8 = QVBoxLayout(self.h_profile)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnProfile = QPushButton(self.h_profile)
        self.btnProfile.setObjectName(u"btnProfile")
        self.btnProfile.setIcon(icon)
        self.btnProfile.setIconSize(QSize(40, 40))

        self.verticalLayout_8.addWidget(self.btnProfile)


        self.horizontalLayout_2.addWidget(self.h_profile)


        self.verticalLayout.addWidget(self.header)

        self.stackedWidget = QStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageStack = QWidget()
        self.pageStack.setObjectName(u"pageStack")
        self.gridLayout_4 = QGridLayout(self.pageStack)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = EStackedWidgetSliding(self.pageStack)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.pageStorage = QWidget()
        self.pageStorage.setObjectName(u"pageStorage")
        self.gridLayout_2 = QGridLayout(self.pageStorage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.uploadsettings = QWidget(self.pageStorage)
        self.uploadsettings.setObjectName(u"uploadsettings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.uploadsettings.sizePolicy().hasHeightForWidth())
        self.uploadsettings.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.uploadsettings)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_upsettings = QLabel(self.uploadsettings)
        self.label_upsettings.setObjectName(u"label_upsettings")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_upsettings.setFont(font5)

        self.gridLayout_7.addWidget(self.label_upsettings, 1, 0, 1, 1)

        self.s_location = QWidget(self.uploadsettings)
        self.s_location.setObjectName(u"s_location")
        self.verticalLayout_6 = QVBoxLayout(self.s_location)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 10, 10, 20)
        self.label_blocation = QLabel(self.s_location)
        self.label_blocation.setObjectName(u"label_blocation")
        self.label_blocation.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_blocation)

        self.btnSelectLocation = QPushButton(self.s_location)
        self.btnSelectLocation.setObjectName(u"btnSelectLocation")
        self.btnSelectLocation.setMinimumSize(QSize(150, 50))
        self.btnSelectLocation.setMaximumSize(QSize(150, 50))
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.btnSelectLocation.setFont(font6)
        self.btnSelectLocation.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btnSelectLocation)

        self.label_3 = QLabel(self.s_location)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 1))
        self.label_3.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_6.addWidget(self.label_3)


        self.gridLayout_7.addWidget(self.s_location, 3, 0, 1, 1)

        self.s_backupType = QWidget(self.uploadsettings)
        self.s_backupType.setObjectName(u"s_backupType")
        self.gridLayout = QGridLayout(self.s_backupType)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, -1, -1, -1)
        self.btnBackupNow = QPushButton(self.s_backupType)
        self.btnBackupNow.setObjectName(u"btnBackupNow")
        self.btnBackupNow.setMinimumSize(QSize(120, 120))
        self.btnBackupNow.setMaximumSize(QSize(120, 16777215))
        self.btnBackupNow.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btnBackupNow, 8, 1, 1, 2)

        self.chkAutoBackup = QCheckBox(self.s_backupType)
        self.chkAutoBackup.setObjectName(u"chkAutoBackup")
        self.chkAutoBackup.setFont(font2)

        self.gridLayout.addWidget(self.chkAutoBackup, 0, 0, 1, 1)

        self.radiosetting = QWidget(self.s_backupType)
        self.radiosetting.setObjectName(u"radiosetting")
        self.horizontalLayout_7 = QHBoxLayout(self.radiosetting)
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.radiosetting, 7, 1, 1, 1)

        self.frame = QFrame(self.s_backupType)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.cmbBackupPeriod = QComboBox(self.frame)
        self.cmbBackupPeriod.addItem("")
        self.cmbBackupPeriod.addItem("")
        self.cmbBackupPeriod.addItem("")
        self.cmbBackupPeriod.addItem("")
        self.cmbBackupPeriod.addItem("")
        self.cmbBackupPeriod.addItem("")
        self.cmbBackupPeriod.addItem("")
        self.cmbBackupPeriod.setObjectName(u"cmbBackupPeriod")

        self.horizontalLayout_9.addWidget(self.cmbBackupPeriod)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 8, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 8, 3, 1, 1)


        self.gridLayout_7.addWidget(self.s_backupType, 4, 0, 1, 2)

        self.widget = QWidget(self.uploadsettings)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_4.setFont(font7)

        self.horizontalLayout.addWidget(self.label_4)

        self.txtBackupName = QLineEdit(self.widget)
        self.txtBackupName.setObjectName(u"txtBackupName")
        self.txtBackupName.setMinimumSize(QSize(0, 30))
        self.txtBackupName.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout.addWidget(self.txtBackupName)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)

        self.s_filterfile = QWidget(self.uploadsettings)
        self.s_filterfile.setObjectName(u"s_filterfile")
        self.verticalLayout_5 = QVBoxLayout(self.s_filterfile)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, 10, 0, 10)
        self.label_filterfiles = QLabel(self.s_filterfile)
        self.label_filterfiles.setObjectName(u"label_filterfiles")
        font8 = QFont()
        font8.setPointSize(12)
        self.label_filterfiles.setFont(font8)

        self.verticalLayout_5.addWidget(self.label_filterfiles)

        self.lineEdit_filetype = QLineEdit(self.s_filterfile)
        self.lineEdit_filetype.setObjectName(u"lineEdit_filetype")
        self.lineEdit_filetype.setMinimumSize(QSize(250, 30))
        self.lineEdit_filetype.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_5.addWidget(self.lineEdit_filetype)


        self.gridLayout_7.addWidget(self.s_filterfile, 2, 0, 1, 2)

        self.lblStatus = QLabel(self.uploadsettings)
        self.lblStatus.setObjectName(u"lblStatus")
        font9 = QFont()
        font9.setPointSize(11)
        self.lblStatus.setFont(font9)

        self.gridLayout_7.addWidget(self.lblStatus, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.uploadsettings, 1, 0, 1, 1)

        self.uploadfiles = QWidget(self.pageStorage)
        self.uploadfiles.setObjectName(u"uploadfiles")
        sizePolicy.setHeightForWidth(self.uploadfiles.sizePolicy().hasHeightForWidth())
        self.uploadfiles.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.uploadfiles)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.label_upfiles = QLabel(self.uploadfiles)
        self.label_upfiles.setObjectName(u"label_upfiles")
        self.label_upfiles.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_upfiles.sizePolicy().hasHeightForWidth())
        self.label_upfiles.setSizePolicy(sizePolicy4)
        self.label_upfiles.setFont(font5)

        self.verticalLayout_2.addWidget(self.label_upfiles)

        self.frame_upload = QFrame(self.uploadfiles)
        self.frame_upload.setObjectName(u"frame_upload")
        sizePolicy2.setHeightForWidth(self.frame_upload.sizePolicy().hasHeightForWidth())
        self.frame_upload.setSizePolicy(sizePolicy2)
        self.frame_upload.setMinimumSize(QSize(160, 0))
        self.frame_upload.setAcceptDrops(True)
        self.frame_upload.setStyleSheet(u"")
        self.frame_upload.setFrameShape(QFrame.StyledPanel)
        self.frame_upload.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_upload)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.label_upicon = QLabel(self.frame_upload)
        self.label_upicon.setObjectName(u"label_upicon")
        self.label_upicon.setMinimumSize(QSize(40, 40))
        self.label_upicon.setMaximumSize(QSize(40, 40))
        self.label_upicon.setPixmap(QPixmap(u":/nightblueIcons/assets/icons/nightblue/upload.svg"))
        self.label_upicon.setScaledContents(True)
        self.label_upicon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_upicon, 0, Qt.AlignHCenter)

        self.label_browsefile = QLabel(self.frame_upload)
        self.label_browsefile.setObjectName(u"label_browsefile")
        self.label_browsefile.setMinimumSize(QSize(160, 0))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setItalic(True)
        font10.setUnderline(False)
        font10.setWeight(50)
        font10.setStrikeOut(False)
        font10.setKerning(True)
        self.label_browsefile.setFont(font10)

        self.verticalLayout_3.addWidget(self.label_browsefile, 0, Qt.AlignHCenter)

        self.pushButton_selectfile = QPushButton(self.frame_upload)
        self.pushButton_selectfile.setObjectName(u"pushButton_selectfile")
        self.pushButton_selectfile.setMinimumSize(QSize(150, 50))
        self.pushButton_selectfile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_selectfile.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton_selectfile, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_upload)


        self.gridLayout_2.addWidget(self.uploadfiles, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageStorage)
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.gridLayout_3 = QGridLayout(self.pageDashboard)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.tableWidget = QTableWidget(self.pageDashboard)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.pageDashboard)

        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageStack)
        self.page_Dashboard22222 = QWidget()
        self.page_Dashboard22222.setObjectName(u"page_Dashboard22222")
        self.stackedWidget.addWidget(self.page_Dashboard22222)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout_6.addWidget(self.mainBody, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EB File Backup Automation", None))
        self.pushButton.setText("")
        self.label_brand.setText(QCoreApplication.translate("MainWindow", u"EB File Backup Automation", None))
        self.pushButton_Storage.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.pushButton_2_Dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label.setText("")
        self.btnGitBerk.setText(QCoreApplication.translate("MainWindow", u"BerkKilicoglu", None))
        self.btnGitEmre.setText(QCoreApplication.translate("MainWindow", u"Emrecpp", None))
        self.menuBtn.setText("")
        self.label_menuname.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_searchicon.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btnProfile.setText("")
        self.label_upsettings.setText(QCoreApplication.translate("MainWindow", u"Backup Settings", None))
        self.label_blocation.setText(QCoreApplication.translate("MainWindow", u"Backup Location", None))
        self.btnSelectLocation.setText(QCoreApplication.translate("MainWindow", u"Select Location", None))
        self.label_3.setText("")
        self.btnBackupNow.setText(QCoreApplication.translate("MainWindow", u"BACKUP FILE !", None))
        self.chkAutoBackup.setText(QCoreApplication.translate("MainWindow", u"Automatic Backup", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Backup period:", None))
        self.cmbBackupPeriod.setItemText(0, QCoreApplication.translate("MainWindow", u"1 min", None))
        self.cmbBackupPeriod.setItemText(1, QCoreApplication.translate("MainWindow", u"5 min", None))
        self.cmbBackupPeriod.setItemText(2, QCoreApplication.translate("MainWindow", u"1 hour", None))
        self.cmbBackupPeriod.setItemText(3, QCoreApplication.translate("MainWindow", u"12 hours", None))
        self.cmbBackupPeriod.setItemText(4, QCoreApplication.translate("MainWindow", u"1 day", None))
        self.cmbBackupPeriod.setItemText(5, QCoreApplication.translate("MainWindow", u"1 week", None))
        self.cmbBackupPeriod.setItemText(6, QCoreApplication.translate("MainWindow", u"1 month", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Backup name:", None))
        self.txtBackupName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please Enter Backup Name", None))
        self.label_filterfiles.setText(QCoreApplication.translate("MainWindow", u"Filter your files type", None))
        self.lineEdit_filetype.setText("")
        self.lineEdit_filetype.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the file name. Ex: .txt / myFiles.png", None))
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"Status: Waiting...", None))
        self.label_upfiles.setText(QCoreApplication.translate("MainWindow", u"Backup Files", None))
        self.label_upicon.setText("")
        self.label_browsefile.setText(QCoreApplication.translate("MainWindow", u"Drag and Drop files, or Browse", None))
        self.pushButton_selectfile.setText(QCoreApplication.translate("MainWindow", u"Select Directory", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total files count", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Process", None));
    # retranslateUi

