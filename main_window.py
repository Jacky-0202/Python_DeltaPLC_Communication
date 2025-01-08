# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setMaximumSize(QSize(1000, 900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #363636;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FFFFFF;   /* Pure white background */\n"
"    color: #333333;             /* Dark gray text */\n"
"    border: 2px solid #555555;  /* Medium gray border */\n"
"    border-radius: 8px;         /* Slightly rounded corners */\n"
"    font-size: 16px;            /* Font size */\n"
"    font-weight: bold;          /* Bold text */\n"
"    text-align: left;           /* Align text to the left */\n"
"    padding-left: 10px;         /* Add padding for better spacing */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F0F0F0;  /* Light gray background (hover) */\n"
"    border: 2px solid #777777;  /* Lighter border */\n"
"    color: #000000;             /* Black text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0E0E0;  /* Darker gray background */\n"
"    border: 2px solid #333333;  /* Darker border */\n"
"    color: #000000;             /* Black text */\n"
"}\n"
""
                        "\n"
"QPushButton:disabled {\n"
"    background-color: #CCCCCC;  /* Light gray background (disabled) */\n"
"    color: #AAAAAA;             /* Gray text */\n"
"    border: 2px solid #AAAAAA;  /* Gray border */\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid #555555;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid #555555;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: #AAAAAA;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.frame_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(300, 0))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"    background-color: #F7F7F7;  /* \u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"")
        self.frame_6.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_2.setPixmap(QPixmap(u":/IMAGES/resource/IMAGES/wite_logo_HIPOINT.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setStyleSheet(u"QLabel {\n"
"	font-family: 'Courier New';\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}")
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setMaximumSize(QSize(200, 16777215))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"    background-color: #F7F7F7;  /* \u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"")
        self.frame_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_language = QComboBox(self.frame_5)
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.setObjectName(u"comboBox_language")
        self.comboBox_language.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_4.addWidget(self.comboBox_language)

        self.pushButton_minimizeApp = QPushButton(self.frame_5)
        self.pushButton_minimizeApp.setObjectName(u"pushButton_minimizeApp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minimizeApp.sizePolicy().hasHeightForWidth())
        self.pushButton_minimizeApp.setSizePolicy(sizePolicy)
        self.pushButton_minimizeApp.setMinimumSize(QSize(45, 35))
        self.pushButton_minimizeApp.setMaximumSize(QSize(45, 35))
        self.pushButton_minimizeApp.setStyleSheet(u"")
        self.pushButton_minimizeApp.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon = QIcon()
        icon.addFile(u":/ICONS/resource/ICONS/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_minimizeApp.setIcon(icon)
        self.pushButton_minimizeApp.setIconSize(QSize(20, 20))
        self.pushButton_minimizeApp.setAutoDefault(False)
        self.pushButton_minimizeApp.setFlat(False)

        self.horizontalLayout_4.addWidget(self.pushButton_minimizeApp)

        self.pushButton_closeApp = QPushButton(self.frame_5)
        self.pushButton_closeApp.setObjectName(u"pushButton_closeApp")
        self.pushButton_closeApp.setMinimumSize(QSize(45, 35))
        self.pushButton_closeApp.setMaximumSize(QSize(45, 35))
        self.pushButton_closeApp.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon1 = QIcon()
        icon1.addFile(u":/ICONS/resource/ICONS/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_closeApp.setIcon(icon1)
        self.pushButton_closeApp.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_closeApp)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(0, 16777215))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"    background-color: #F7F7F7;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.frame_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_menu = QPushButton(self.frame_4)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setMinimumSize(QSize(0, 30))
        self.pushButton_menu.setMaximumSize(QSize(16777215, 30))
        self.pushButton_menu.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon2 = QIcon()
        icon2.addFile(u":/ICONS/resource/ICONS/arrow-right-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_menu.setIcon(icon2)
        self.pushButton_menu.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_menu)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: #AAAAAA;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.frame_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame {\n"
"    background-color: #F7F7F7;  /* \u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QLabel {\n"
"	font-family: 'Courier New';\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}")
        self.frame_7.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(315, 102, 122, 161))
        self.layoutWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setSpacing(12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_writeCoilNumber = QLineEdit(self.layoutWidget)
        self.lineEdit_writeCoilNumber.setObjectName(u"lineEdit_writeCoilNumber")
        self.lineEdit_writeCoilNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_writeCoilNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_writeCoilNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_8.addWidget(self.lineEdit_writeCoilNumber)

        self.lineEdit_writeRegisterNumber = QLineEdit(self.layoutWidget)
        self.lineEdit_writeRegisterNumber.setObjectName(u"lineEdit_writeRegisterNumber")
        self.lineEdit_writeRegisterNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_writeRegisterNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_writeRegisterNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_8.addWidget(self.lineEdit_writeRegisterNumber)

        self.lineEdit_readCoilNumber = QLineEdit(self.layoutWidget)
        self.lineEdit_readCoilNumber.setObjectName(u"lineEdit_readCoilNumber")
        self.lineEdit_readCoilNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_readCoilNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_readCoilNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_8.addWidget(self.lineEdit_readCoilNumber)

        self.lineEdit_readRegisterNumber = QLineEdit(self.layoutWidget)
        self.lineEdit_readRegisterNumber.setObjectName(u"lineEdit_readRegisterNumber")
        self.lineEdit_readRegisterNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_readRegisterNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_readRegisterNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_8.addWidget(self.lineEdit_readRegisterNumber)

        self.layoutWidget_2 = QWidget(self.page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(22, 21, 162, 242))
        self.layoutWidget_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 30))
        self.label_3.setMaximumSize(QSize(120, 30))
        self.label_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 30))
        self.label_4.setMaximumSize(QSize(120, 30))
        self.label_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 30))
        self.label_5.setMaximumSize(QSize(120, 30))
        self.label_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(160, 30))
        self.label_6.setMaximumSize(QSize(160, 30))
        self.label_6.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 30))
        self.label_8.setMaximumSize(QSize(120, 30))
        self.label_8.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(160, 30))
        self.label_7.setMaximumSize(QSize(160, 30))
        self.label_7.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.label_7)

        self.textBrowser_singleResponse = QTextBrowser(self.page)
        self.textBrowser_singleResponse.setObjectName(u"textBrowser_singleResponse")
        self.textBrowser_singleResponse.setGeometry(QRect(30, 380, 500, 30))
        self.textBrowser_singleResponse.setMinimumSize(QSize(500, 30))
        self.textBrowser_singleResponse.setMaximumSize(QSize(600, 30))
        self.textBrowser_singleResponse.setStyleSheet(u"QTextBrowser {\n"
"    background-color: #E3E3E3;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.textBrowser_singleResponse.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget_3 = QWidget(self.page)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(198, 21, 102, 242))
        self.layoutWidget_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.comboBox_comport = QComboBox(self.layoutWidget_3)
        self.comboBox_comport.setObjectName(u"comboBox_comport")
        self.comboBox_comport.setMinimumSize(QSize(100, 30))
        self.comboBox_comport.setMaximumSize(QSize(120, 30))
        self.comboBox_comport.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_9.addWidget(self.comboBox_comport)

        self.comboBox_slaveID = QComboBox(self.layoutWidget_3)
        self.comboBox_slaveID.addItem("")
        self.comboBox_slaveID.addItem("")
        self.comboBox_slaveID.addItem("")
        self.comboBox_slaveID.addItem("")
        self.comboBox_slaveID.setObjectName(u"comboBox_slaveID")
        self.comboBox_slaveID.setMinimumSize(QSize(100, 30))
        self.comboBox_slaveID.setMaximumSize(QSize(120, 30))
        self.comboBox_slaveID.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_9.addWidget(self.comboBox_slaveID)

        self.comboBox_writeCoilName = QComboBox(self.layoutWidget_3)
        self.comboBox_writeCoilName.addItem("")
        self.comboBox_writeCoilName.addItem("")
        self.comboBox_writeCoilName.addItem("")
        self.comboBox_writeCoilName.addItem("")
        self.comboBox_writeCoilName.addItem("")
        self.comboBox_writeCoilName.setObjectName(u"comboBox_writeCoilName")
        self.comboBox_writeCoilName.setMinimumSize(QSize(100, 30))
        self.comboBox_writeCoilName.setMaximumSize(QSize(120, 30))
        self.comboBox_writeCoilName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_9.addWidget(self.comboBox_writeCoilName)

        self.comboBox_writeRegisterName = QComboBox(self.layoutWidget_3)
        self.comboBox_writeRegisterName.addItem("")
        self.comboBox_writeRegisterName.addItem("")
        self.comboBox_writeRegisterName.addItem("")
        self.comboBox_writeRegisterName.setObjectName(u"comboBox_writeRegisterName")
        self.comboBox_writeRegisterName.setMinimumSize(QSize(100, 30))
        self.comboBox_writeRegisterName.setMaximumSize(QSize(120, 30))
        self.comboBox_writeRegisterName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_9.addWidget(self.comboBox_writeRegisterName)

        self.comboBox_readCoilName = QComboBox(self.layoutWidget_3)
        self.comboBox_readCoilName.addItem("")
        self.comboBox_readCoilName.addItem("")
        self.comboBox_readCoilName.addItem("")
        self.comboBox_readCoilName.addItem("")
        self.comboBox_readCoilName.addItem("")
        self.comboBox_readCoilName.addItem("")
        self.comboBox_readCoilName.setObjectName(u"comboBox_readCoilName")
        self.comboBox_readCoilName.setMinimumSize(QSize(100, 30))
        self.comboBox_readCoilName.setMaximumSize(QSize(120, 30))
        self.comboBox_readCoilName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_9.addWidget(self.comboBox_readCoilName)

        self.comboBox_readRegisterName = QComboBox(self.layoutWidget_3)
        self.comboBox_readRegisterName.addItem("")
        self.comboBox_readRegisterName.addItem("")
        self.comboBox_readRegisterName.addItem("")
        self.comboBox_readRegisterName.setObjectName(u"comboBox_readRegisterName")
        self.comboBox_readRegisterName.setMinimumSize(QSize(100, 30))
        self.comboBox_readRegisterName.setMaximumSize(QSize(120, 30))
        self.comboBox_readRegisterName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_9.addWidget(self.comboBox_readRegisterName)

        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 420, 100, 30))
        self.label_10.setMinimumSize(QSize(100, 30))
        self.label_10.setMaximumSize(QSize(100, 30))
        self.label_10.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.textBrowser_prase = QTextBrowser(self.page)
        self.textBrowser_prase.setObjectName(u"textBrowser_prase")
        self.textBrowser_prase.setGeometry(QRect(30, 460, 501, 90))
        self.textBrowser_prase.setMinimumSize(QSize(500, 60))
        self.textBrowser_prase.setMaximumSize(QSize(600, 90))
        self.textBrowser_prase.setStyleSheet(u"QTextBrowser {\n"
"    background-color: #E3E3E3;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.textBrowser_prase.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget_4 = QWidget(self.page)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(470, 108, 58, 151))
        self.layoutWidget_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.checkBox_writeCoil = QCheckBox(self.layoutWidget_4)
        self.checkBox_writeCoil.setObjectName(u"checkBox_writeCoil")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_writeCoil.sizePolicy().hasHeightForWidth())
        self.checkBox_writeCoil.setSizePolicy(sizePolicy1)
        self.checkBox_writeCoil.setStyleSheet(u"")
        self.checkBox_writeCoil.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_10.addWidget(self.checkBox_writeCoil)

        self.checkBox_writeRegister = QCheckBox(self.layoutWidget_4)
        self.checkBox_writeRegister.setObjectName(u"checkBox_writeRegister")
        self.checkBox_writeRegister.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_10.addWidget(self.checkBox_writeRegister)

        self.checkBox_readCoil = QCheckBox(self.layoutWidget_4)
        self.checkBox_readCoil.setObjectName(u"checkBox_readCoil")
        self.checkBox_readCoil.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_10.addWidget(self.checkBox_readCoil)

        self.checkBox_readRegister = QCheckBox(self.layoutWidget_4)
        self.checkBox_readRegister.setObjectName(u"checkBox_readRegister")
        self.checkBox_readRegister.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_10.addWidget(self.checkBox_readRegister)

        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 330, 100, 30))
        self.label_9.setMinimumSize(QSize(100, 30))
        self.label_9.setMaximumSize(QSize(100, 30))
        self.label_9.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget_5 = QWidget(self.page)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(200, 300, 332, 32))
        self.layoutWidget_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 30))
        self.label_11.setMaximumSize(QSize(100, 30))
        self.label_11.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_6.addWidget(self.label_11)

        self.lineEdit_singleExcute = QLineEdit(self.layoutWidget_5)
        self.lineEdit_singleExcute.setObjectName(u"lineEdit_singleExcute")
        self.lineEdit_singleExcute.setMinimumSize(QSize(100, 30))
        self.lineEdit_singleExcute.setMaximumSize(QSize(100, 30))
        self.lineEdit_singleExcute.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_6.addWidget(self.lineEdit_singleExcute)

        self.pushButton_excuteSingle = QPushButton(self.layoutWidget_5)
        self.pushButton_excuteSingle.setObjectName(u"pushButton_excuteSingle")
        self.pushButton_excuteSingle.setMinimumSize(QSize(100, 30))
        self.pushButton_excuteSingle.setMaximumSize(QSize(100, 30))
        self.pushButton_excuteSingle.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon3 = QIcon()
        icon3.addFile(u":/ICONS/resource/ICONS/slack.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_excuteSingle.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.pushButton_excuteSingle)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.comboBox_writeMultiCoilName = QComboBox(self.page_2)
        self.comboBox_writeMultiCoilName.addItem("")
        self.comboBox_writeMultiCoilName.addItem("")
        self.comboBox_writeMultiCoilName.addItem("")
        self.comboBox_writeMultiCoilName.addItem("")
        self.comboBox_writeMultiCoilName.addItem("")
        self.comboBox_writeMultiCoilName.setObjectName(u"comboBox_writeMultiCoilName")
        self.comboBox_writeMultiCoilName.setGeometry(QRect(30, 80, 100, 30))
        self.comboBox_writeMultiCoilName.setMinimumSize(QSize(100, 30))
        self.comboBox_writeMultiCoilName.setMaximumSize(QSize(200, 30))
        self.comboBox_writeMultiCoilName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.comboBox_writeMultiRegisterName = QComboBox(self.page_2)
        self.comboBox_writeMultiRegisterName.addItem("")
        self.comboBox_writeMultiRegisterName.addItem("")
        self.comboBox_writeMultiRegisterName.addItem("")
        self.comboBox_writeMultiRegisterName.setObjectName(u"comboBox_writeMultiRegisterName")
        self.comboBox_writeMultiRegisterName.setGeometry(QRect(30, 250, 100, 30))
        self.comboBox_writeMultiRegisterName.setMinimumSize(QSize(100, 30))
        self.comboBox_writeMultiRegisterName.setMaximumSize(QSize(120, 30))
        self.comboBox_writeMultiRegisterName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit_writeMultiCoilNumber = QLineEdit(self.page_2)
        self.lineEdit_writeMultiCoilNumber.setObjectName(u"lineEdit_writeMultiCoilNumber")
        self.lineEdit_writeMultiCoilNumber.setGeometry(QRect(160, 80, 120, 30))
        self.lineEdit_writeMultiCoilNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_writeMultiCoilNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_writeMultiCoilNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit_writeMultiRegisterNumber = QLineEdit(self.page_2)
        self.lineEdit_writeMultiRegisterNumber.setObjectName(u"lineEdit_writeMultiRegisterNumber")
        self.lineEdit_writeMultiRegisterNumber.setGeometry(QRect(160, 250, 120, 30))
        self.lineEdit_writeMultiRegisterNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_writeMultiRegisterNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_writeMultiRegisterNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 30, 200, 30))
        self.label_12.setMinimumSize(QSize(200, 30))
        self.label_12.setMaximumSize(QSize(120, 30))
        self.label_12.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 200, 200, 30))
        self.label_13.setMinimumSize(QSize(200, 30))
        self.label_13.setMaximumSize(QSize(200, 30))
        self.label_13.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget_6 = QWidget(self.page_2)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(30, 140, 382, 32))
        self.layoutWidget_6.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 30))
        self.label_14.setMaximumSize(QSize(100, 30))
        self.label_14.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_7.addWidget(self.label_14)

        self.lineEdit_excuteMultiCoil = QLineEdit(self.layoutWidget_6)
        self.lineEdit_excuteMultiCoil.setObjectName(u"lineEdit_excuteMultiCoil")
        self.lineEdit_excuteMultiCoil.setMinimumSize(QSize(150, 30))
        self.lineEdit_excuteMultiCoil.setMaximumSize(QSize(150, 30))
        self.lineEdit_excuteMultiCoil.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_7.addWidget(self.lineEdit_excuteMultiCoil)

        self.pushButton_excuteMultiCoil = QPushButton(self.layoutWidget_6)
        self.pushButton_excuteMultiCoil.setObjectName(u"pushButton_excuteMultiCoil")
        self.pushButton_excuteMultiCoil.setMinimumSize(QSize(100, 30))
        self.pushButton_excuteMultiCoil.setMaximumSize(QSize(100, 30))
        self.pushButton_excuteMultiCoil.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButton_excuteMultiCoil.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.pushButton_excuteMultiCoil)

        self.layoutWidget_7 = QWidget(self.page_2)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(30, 310, 382, 32))
        self.layoutWidget_7.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 30))
        self.label_15.setMaximumSize(QSize(100, 30))
        self.label_15.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_8.addWidget(self.label_15)

        self.lineEdit_excuteMultiRegister = QLineEdit(self.layoutWidget_7)
        self.lineEdit_excuteMultiRegister.setObjectName(u"lineEdit_excuteMultiRegister")
        self.lineEdit_excuteMultiRegister.setMinimumSize(QSize(150, 30))
        self.lineEdit_excuteMultiRegister.setMaximumSize(QSize(150, 30))
        self.lineEdit_excuteMultiRegister.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_8.addWidget(self.lineEdit_excuteMultiRegister)

        self.pushButton_excuteMultiRegister = QPushButton(self.layoutWidget_7)
        self.pushButton_excuteMultiRegister.setObjectName(u"pushButton_excuteMultiRegister")
        self.pushButton_excuteMultiRegister.setMinimumSize(QSize(100, 30))
        self.pushButton_excuteMultiRegister.setMaximumSize(QSize(100, 30))
        self.pushButton_excuteMultiRegister.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButton_excuteMultiRegister.setIcon(icon3)

        self.horizontalLayout_8.addWidget(self.pushButton_excuteMultiRegister)

        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 380, 100, 30))
        self.label_16.setMinimumSize(QSize(100, 30))
        self.label_16.setMaximumSize(QSize(100, 30))
        self.label_16.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.textBrowser_multiResponse = QTextBrowser(self.page_2)
        self.textBrowser_multiResponse.setObjectName(u"textBrowser_multiResponse")
        self.textBrowser_multiResponse.setGeometry(QRect(30, 430, 500, 60))
        self.textBrowser_multiResponse.setMinimumSize(QSize(500, 60))
        self.textBrowser_multiResponse.setMaximumSize(QSize(600, 60))
        self.textBrowser_multiResponse.setStyleSheet(u"QTextBrowser {\n"
"    background-color: #E3E3E3;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.textBrowser_multiResponse.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 20, 220, 30))
        self.label_17.setMinimumSize(QSize(150, 30))
        self.label_17.setMaximumSize(QSize(250, 30))
        self.label_17.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget_8 = QWidget(self.page_3)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(60, 160, 447, 32))
        self.layoutWidget_8.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(100, 30))
        self.label_18.setMaximumSize(QSize(100, 30))
        self.label_18.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_9.addWidget(self.label_18)

        self.lineEdit_excuteMonitorCoil = QLineEdit(self.layoutWidget_8)
        self.lineEdit_excuteMonitorCoil.setObjectName(u"lineEdit_excuteMonitorCoil")
        self.lineEdit_excuteMonitorCoil.setMinimumSize(QSize(100, 30))
        self.lineEdit_excuteMonitorCoil.setMaximumSize(QSize(100, 30))
        self.lineEdit_excuteMonitorCoil.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_9.addWidget(self.lineEdit_excuteMonitorCoil)

        self.pushButton_excuteMonitorCoil = QPushButton(self.layoutWidget_8)
        self.pushButton_excuteMonitorCoil.setObjectName(u"pushButton_excuteMonitorCoil")
        self.pushButton_excuteMonitorCoil.setMinimumSize(QSize(100, 30))
        self.pushButton_excuteMonitorCoil.setMaximumSize(QSize(100, 30))
        self.pushButton_excuteMonitorCoil.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButton_excuteMonitorCoil.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.pushButton_excuteMonitorCoil)

        self.pushButton_cancelMonitorCoil = QPushButton(self.layoutWidget_8)
        self.pushButton_cancelMonitorCoil.setObjectName(u"pushButton_cancelMonitorCoil")
        self.pushButton_cancelMonitorCoil.setMinimumSize(QSize(100, 30))
        self.pushButton_cancelMonitorCoil.setMaximumSize(QSize(100, 30))
        self.pushButton_cancelMonitorCoil.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon4 = QIcon()
        icon4.addFile(u":/ICONS/resource/ICONS/user-x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_cancelMonitorCoil.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.pushButton_cancelMonitorCoil)

        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(270, 60, 111, 16))
        self.label_20 = QLabel(self.page_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(140, 60, 111, 16))
        self.label_21 = QLabel(self.page_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 60, 111, 16))
        self.label_22 = QLabel(self.page_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 230, 250, 30))
        self.label_22.setMinimumSize(QSize(150, 30))
        self.label_22.setMaximumSize(QSize(250, 30))
        self.label_22.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget_9 = QWidget(self.page_3)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(60, 360, 447, 32))
        self.layoutWidget_9.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.layoutWidget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 30))
        self.label_23.setMaximumSize(QSize(100, 30))
        self.label_23.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_11.addWidget(self.label_23)

        self.lineEdit_excuteMonitorCoilState = QLineEdit(self.layoutWidget_9)
        self.lineEdit_excuteMonitorCoilState.setObjectName(u"lineEdit_excuteMonitorCoilState")
        self.lineEdit_excuteMonitorCoilState.setMinimumSize(QSize(100, 30))
        self.lineEdit_excuteMonitorCoilState.setMaximumSize(QSize(100, 30))
        self.lineEdit_excuteMonitorCoilState.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_11.addWidget(self.lineEdit_excuteMonitorCoilState)

        self.pushButton_excuteMonitorCoilState = QPushButton(self.layoutWidget_9)
        self.pushButton_excuteMonitorCoilState.setObjectName(u"pushButton_excuteMonitorCoilState")
        self.pushButton_excuteMonitorCoilState.setMinimumSize(QSize(100, 30))
        self.pushButton_excuteMonitorCoilState.setMaximumSize(QSize(100, 30))
        self.pushButton_excuteMonitorCoilState.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButton_excuteMonitorCoilState.setIcon(icon3)

        self.horizontalLayout_11.addWidget(self.pushButton_excuteMonitorCoilState)

        self.pushButton_cancelMonitorCoilState = QPushButton(self.layoutWidget_9)
        self.pushButton_cancelMonitorCoilState.setObjectName(u"pushButton_cancelMonitorCoilState")
        self.pushButton_cancelMonitorCoilState.setMinimumSize(QSize(100, 30))
        self.pushButton_cancelMonitorCoilState.setMaximumSize(QSize(100, 30))
        self.pushButton_cancelMonitorCoilState.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButton_cancelMonitorCoilState.setIcon(icon4)

        self.horizontalLayout_11.addWidget(self.pushButton_cancelMonitorCoilState)

        self.textBrowser_monitorResponse = QTextBrowser(self.page_3)
        self.textBrowser_monitorResponse.setObjectName(u"textBrowser_monitorResponse")
        self.textBrowser_monitorResponse.setGeometry(QRect(20, 490, 500, 60))
        self.textBrowser_monitorResponse.setMinimumSize(QSize(500, 60))
        self.textBrowser_monitorResponse.setMaximumSize(QSize(600, 60))
        self.textBrowser_monitorResponse.setStyleSheet(u"QTextBrowser {\n"
"    background-color: #E3E3E3;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.textBrowser_monitorResponse.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_24 = QLabel(self.page_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 440, 100, 30))
        self.label_24.setMinimumSize(QSize(100, 30))
        self.label_24.setMaximumSize(QSize(100, 30))
        self.label_24.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget1 = QWidget(self.page_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 90, 372, 32))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.comboBox_writeMonitorCoilName = QComboBox(self.layoutWidget1)
        self.comboBox_writeMonitorCoilName.addItem("")
        self.comboBox_writeMonitorCoilName.addItem("")
        self.comboBox_writeMonitorCoilName.addItem("")
        self.comboBox_writeMonitorCoilName.addItem("")
        self.comboBox_writeMonitorCoilName.addItem("")
        self.comboBox_writeMonitorCoilName.setObjectName(u"comboBox_writeMonitorCoilName")
        self.comboBox_writeMonitorCoilName.setMinimumSize(QSize(100, 30))
        self.comboBox_writeMonitorCoilName.setMaximumSize(QSize(120, 30))
        self.comboBox_writeMonitorCoilName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_10.addWidget(self.comboBox_writeMonitorCoilName)

        self.lineEdit_writeMonitorCoilNumber = QLineEdit(self.layoutWidget1)
        self.lineEdit_writeMonitorCoilNumber.setObjectName(u"lineEdit_writeMonitorCoilNumber")
        self.lineEdit_writeMonitorCoilNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_writeMonitorCoilNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_writeMonitorCoilNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_10.addWidget(self.lineEdit_writeMonitorCoilNumber)

        self.lineEdit_writeMonitorCoilInterval = QLineEdit(self.layoutWidget1)
        self.lineEdit_writeMonitorCoilInterval.setObjectName(u"lineEdit_writeMonitorCoilInterval")
        self.lineEdit_writeMonitorCoilInterval.setMinimumSize(QSize(120, 30))
        self.lineEdit_writeMonitorCoilInterval.setMaximumSize(QSize(150, 30))
        self.lineEdit_writeMonitorCoilInterval.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_10.addWidget(self.lineEdit_writeMonitorCoilInterval)

        self.layoutWidget2 = QWidget(self.page_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 290, 237, 32))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.comboBox_readMonitorCoilName = QComboBox(self.layoutWidget2)
        self.comboBox_readMonitorCoilName.addItem("")
        self.comboBox_readMonitorCoilName.addItem("")
        self.comboBox_readMonitorCoilName.addItem("")
        self.comboBox_readMonitorCoilName.addItem("")
        self.comboBox_readMonitorCoilName.addItem("")
        self.comboBox_readMonitorCoilName.setObjectName(u"comboBox_readMonitorCoilName")
        self.comboBox_readMonitorCoilName.setMinimumSize(QSize(100, 30))
        self.comboBox_readMonitorCoilName.setMaximumSize(QSize(120, 30))
        self.comboBox_readMonitorCoilName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_12.addWidget(self.comboBox_readMonitorCoilName)

        self.lineEdit_readMonitorCoilNumber = QLineEdit(self.layoutWidget2)
        self.lineEdit_readMonitorCoilNumber.setObjectName(u"lineEdit_readMonitorCoilNumber")
        self.lineEdit_readMonitorCoilNumber.setMinimumSize(QSize(120, 30))
        self.lineEdit_readMonitorCoilNumber.setMaximumSize(QSize(150, 30))
        self.lineEdit_readMonitorCoilNumber.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_12.addWidget(self.lineEdit_readMonitorCoilNumber)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.side_menu = QFrame(self.frame_3)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(160, 0))
        self.side_menu.setMaximumSize(QSize(160, 16777215))
        self.side_menu.setStyleSheet(u"QFrame {\n"
"    background-color: #F7F7F7;  /* \u7070\u8272\u80cc\u666f */\n"
"}")
        self.side_menu.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.side_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.side_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_10 = QFrame(self.side_menu)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_singleTestPage = QPushButton(self.frame_10)
        self.pushButton_singleTestPage.setObjectName(u"pushButton_singleTestPage")
        self.pushButton_singleTestPage.setMinimumSize(QSize(0, 30))
        self.pushButton_singleTestPage.setMaximumSize(QSize(16777215, 30))
        self.pushButton_singleTestPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon5 = QIcon()
        icon5.addFile(u":/ICONS/resource/ICONS/git-commit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_singleTestPage.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.pushButton_singleTestPage)

        self.pushButton_multiTestPage = QPushButton(self.frame_10)
        self.pushButton_multiTestPage.setObjectName(u"pushButton_multiTestPage")
        self.pushButton_multiTestPage.setMinimumSize(QSize(0, 30))
        self.pushButton_multiTestPage.setMaximumSize(QSize(16777215, 30))
        self.pushButton_multiTestPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon6 = QIcon()
        icon6.addFile(u":/ICONS/resource/ICONS/git-merge.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_multiTestPage.setIcon(icon6)

        self.verticalLayout_3.addWidget(self.pushButton_multiTestPage)

        self.pushButton_monitorPage = QPushButton(self.frame_10)
        self.pushButton_monitorPage.setObjectName(u"pushButton_monitorPage")
        self.pushButton_monitorPage.setMinimumSize(QSize(0, 30))
        self.pushButton_monitorPage.setMaximumSize(QSize(16777215, 30))
        self.pushButton_monitorPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon7 = QIcon()
        icon7.addFile(u":/ICONS/resource/ICONS/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_monitorPage.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.pushButton_monitorPage)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.verticalSpacer = QSpacerItem(20, 365, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame_9 = QFrame(self.side_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_infoPage = QPushButton(self.frame_9)
        self.pushButton_infoPage.setObjectName(u"pushButton_infoPage")
        self.pushButton_infoPage.setMinimumSize(QSize(0, 30))
        self.pushButton_infoPage.setMaximumSize(QSize(16777215, 30))
        self.pushButton_infoPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon8 = QIcon()
        icon8.addFile(u":/ICONS/resource/ICONS/twitch.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_infoPage.setIcon(icon8)

        self.verticalLayout_4.addWidget(self.pushButton_infoPage)

        self.pushButton_helpPage = QPushButton(self.frame_9)
        self.pushButton_helpPage.setObjectName(u"pushButton_helpPage")
        self.pushButton_helpPage.setMinimumSize(QSize(0, 30))
        self.pushButton_helpPage.setMaximumSize(QSize(16777215, 30))
        self.pushButton_helpPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon9 = QIcon()
        icon9.addFile(u":/ICONS/resource/ICONS/user-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_helpPage.setIcon(icon9)

        self.verticalLayout_4.addWidget(self.pushButton_helpPage)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout_2.addWidget(self.side_menu)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_minimizeApp.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Delta PLC Modbus-V1.0", None))
        self.comboBox_language.setItemText(0, QCoreApplication.translate("MainWindow", u"ENG", None))
        self.comboBox_language.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7e41\u9ad4", None))

        self.pushButton_minimizeApp.setText("")
        self.pushButton_closeApp.setText("")
        self.pushButton_menu.setText(QCoreApplication.translate("MainWindow", u" MENU", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"COMPORT : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Slave ID : ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Write Coil : ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Write Register :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Read Coil : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Read Register : ", None))
        self.comboBox_slaveID.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_slaveID.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_slaveID.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_slaveID.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.comboBox_writeCoilName.setItemText(0, QCoreApplication.translate("MainWindow", u"S", None))
        self.comboBox_writeCoilName.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_writeCoilName.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_writeCoilName.setItemText(3, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_writeCoilName.setItemText(4, QCoreApplication.translate("MainWindow", u"C", None))

        self.comboBox_writeRegisterName.setItemText(0, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_writeRegisterName.setItemText(1, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox_writeRegisterName.setItemText(2, QCoreApplication.translate("MainWindow", u"D", None))

        self.comboBox_readCoilName.setItemText(0, QCoreApplication.translate("MainWindow", u"S", None))
        self.comboBox_readCoilName.setItemText(1, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox_readCoilName.setItemText(2, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_readCoilName.setItemText(3, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_readCoilName.setItemText(4, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_readCoilName.setItemText(5, QCoreApplication.translate("MainWindow", u"C", None))

        self.comboBox_readRegisterName.setItemText(0, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_readRegisterName.setItemText(1, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox_readRegisterName.setItemText(2, QCoreApplication.translate("MainWindow", u"D", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Prase", None))
        self.checkBox_writeCoil.setText("")
        self.checkBox_writeRegister.setText("")
        self.checkBox_readCoil.setText("")
        self.checkBox_readRegister.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Response", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Input :", None))
        self.pushButton_excuteSingle.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.comboBox_writeMultiCoilName.setItemText(0, QCoreApplication.translate("MainWindow", u"S", None))
        self.comboBox_writeMultiCoilName.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_writeMultiCoilName.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_writeMultiCoilName.setItemText(3, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_writeMultiCoilName.setItemText(4, QCoreApplication.translate("MainWindow", u"C", None))

        self.comboBox_writeMultiRegisterName.setItemText(0, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_writeMultiRegisterName.setItemText(1, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox_writeMultiRegisterName.setItemText(2, QCoreApplication.translate("MainWindow", u"D", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Write  Multi Coil : ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Write Register :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Input :", None))
        self.pushButton_excuteMultiCoil.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Input :", None))
        self.pushButton_excuteMultiRegister.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Response", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Cyclical Write Coil : ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Input :", None))
        self.pushButton_excuteMonitorCoil.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.pushButton_cancelMonitorCoil.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Interval(s)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Monitoring Coil State :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Input :", None))
        self.pushButton_excuteMonitorCoilState.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.pushButton_cancelMonitorCoilState.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Prase", None))
        self.comboBox_writeMonitorCoilName.setItemText(0, QCoreApplication.translate("MainWindow", u"S", None))
        self.comboBox_writeMonitorCoilName.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_writeMonitorCoilName.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_writeMonitorCoilName.setItemText(3, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_writeMonitorCoilName.setItemText(4, QCoreApplication.translate("MainWindow", u"C", None))

        self.comboBox_readMonitorCoilName.setItemText(0, QCoreApplication.translate("MainWindow", u"S", None))
        self.comboBox_readMonitorCoilName.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_readMonitorCoilName.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_readMonitorCoilName.setItemText(3, QCoreApplication.translate("MainWindow", u"T", None))
        self.comboBox_readMonitorCoilName.setItemText(4, QCoreApplication.translate("MainWindow", u"C", None))

        self.pushButton_singleTestPage.setText(QCoreApplication.translate("MainWindow", u" Single Test", None))
        self.pushButton_multiTestPage.setText(QCoreApplication.translate("MainWindow", u" Multi Test", None))
        self.pushButton_monitorPage.setText(QCoreApplication.translate("MainWindow", u"  Monitor", None))
        self.pushButton_infoPage.setText(QCoreApplication.translate("MainWindow", u" Info", None))
        self.pushButton_helpPage.setText(QCoreApplication.translate("MainWindow", u" Help", None))
    # retranslateUi

