# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI2XBCGXJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import os
global main_link 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        global main_link 
        main_link = MainWindow
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1045, 1000)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(os.getcwd() + "\\" + "icons\\" + "logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(35, 35, 35)")
        MainWindow.setWindowFilePath(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(180, 0))
        self.frame_left_menu.setMaximumSize(QSize(180, 16777215))

        idGotham = QFontDatabase().addApplicationFont(os.getcwd() + "\\" + "fonts\\" + "GothamMedium.ttf")
        familyGotham = QFontDatabase().applicationFontFamilies(idGotham)
        idProximaM = QFontDatabase().addApplicationFont(os.getcwd() + "\\" + "fonts\\" + "Proxima-Nova-Medium.ttf")
        familyProximaM = QFontDatabase().applicationFontFamilies(idProximaM)



        self.frame_left_menu.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.frame_left_menu)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setFrameShape(QFrame.NoFrame)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_2)

        self.Btn_Video = QPushButton(self.frame_top_menu)
        self.Btn_Video.setObjectName(u"Btn_Video")
        self.Btn_Video.setMinimumSize(QSize(0, 40))
        self.Btn_Video.setSizePolicy(sizePolicy)
        self.Btn_Video.setFocusPolicy(Qt.NoFocus)
        self.Btn_Video.setStyleSheet(u"QPushButton {\n"
"	color: rgb(179, 179, 179);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 11pt 'Gotham';\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.Btn_Video.setCheckable(False)

        self.verticalLayout_4.addWidget(self.Btn_Video)

        self.Btn_Import = QPushButton(self.frame_top_menu)
        self.Btn_Import.setObjectName(u"Btn_Import")
        self.Btn_Import.setMinimumSize(QSize(0, 40))
        self.Btn_Import.setSizePolicy(sizePolicy)
        self.Btn_Import.setFocusPolicy(Qt.NoFocus)
        self.Btn_Import.setStyleSheet(u"QPushButton {\n"
"	color: rgb(179, 179, 179);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 11pt 'Gotham';\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(220, 220, 220);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Import)

        self.Btn_Run = QPushButton(self.frame_top_menu)
        self.Btn_Run.setObjectName(u"Btn_Run")
        self.Btn_Run.setSizePolicy(sizePolicy)
        self.Btn_Run.setMinimumSize(QSize(0, 40))
        self.Btn_Run.setFocusPolicy(Qt.NoFocus)
        self.Btn_Run.setStyleSheet(u"QPushButton {\n"
"	color: rgb(179, 179, 179);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 11pt 'Gotham';\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.Btn_Run.setCheckable(True)

        self.verticalLayout_4.addWidget(self.Btn_Run)


        self.Btn_Help = QPushButton(self.frame_top_menu)
        self.Btn_Help.setObjectName(u"Btn_Help")
        self.Btn_Help.setMinimumSize(QSize(0, 40))
        self.Btn_Help.setMaximumSize(QSize(16777215, 40))
        self.Btn_Help.setSizePolicy(sizePolicy)
        self.Btn_Help.setSizeIncrement(QSize(0, 0))
        self.Btn_Help.setFocusPolicy(Qt.NoFocus)
        self.Btn_Video.setSizePolicy(sizePolicy)
        self.Btn_Help.setStyleSheet(u"QPushButton {\n"
"	color: rgb(179, 179, 179);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 11pt 'Gotham';\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.verticalLayout_4.addWidget(self.Btn_Help)

        self.Space_HP = QSpacerItem(40, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(self.Space_HP)
        self.Label_Parameters = QPushButton(self.frame_top_menu)
        self.Label_Parameters.setObjectName(u"Label_Parameters")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Parameters.sizePolicy().hasHeightForWidth())
        self.Label_Parameters.setSizePolicy(sizePolicy)
        self.Label_Parameters.setMinimumSize(QSize(0, 0))
        self.Label_Parameters.setMaximumSize(QSize(16777215, 0))
        self.Label_Parameters.setFocusPolicy(Qt.NoFocus)
        self.Label_Parameters.setAcceptDrops(False)
        self.Label_Parameters.setStyleSheet(u"QPushButton {\n"
"	color: rgb(120, 120, 120);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 10pt 'Proxima Nova Lt';\n"
"}\n"
"")

        self.Label_Parameters.setFlat(False)

        self.verticalLayout_4.addWidget(self.Label_Parameters)

        self.horizontalSpacer_4 = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_4)

        self.Line_Parameters = QFrame(self.frame_top_menu)
        self.Line_Parameters.setObjectName(u"Line_Parameters")
        self.Line_Parameters.setSizePolicy(sizePolicy)
        self.Line_Parameters.setMinimumSize(QSize(0, 3))
        self.Line_Parameters.setMaximumSize(QSize(16777215, 3))
        self.Line_Parameters.setAutoFillBackground(False)
        self.Line_Parameters.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.Line_Parameters.setFrameShape(QFrame.HLine)
        self.Line_Parameters.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.Line_Parameters)


   

        self.Space_PL = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.Space_PL)

        self.Empty = QPushButton(self.frame_top_menu)
        self.Empty.setObjectName(u"Empty")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.Empty.setSizePolicy(sizePolicy2)
        self.Empty.setMinimumSize(QSize(0, 0))
        self.Empty.setMaximumSize(QSize(16777215, 0))
        self.Empty.setStyleSheet(u"QPushButton {\n"
"	color: rgb(120, 120, 120);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 10pt 'ProximaNova-Medium';\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/listItems/greyMarker.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Empty.setIcon(icon1)
        self.Empty.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.Empty)

        self.listWidget = QListWidget(self.frame_top_menu)
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(200, 200, 200, 255))
        brush1.setStyle(Qt.NoBrush)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem.setBackground(brush1);
        __qlistwidgetitem.setForeground(brush);
        brush2 = QBrush(QColor(200, 200, 200, 255))
        brush2.setStyle(Qt.NoBrush)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem1.setForeground(brush2);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.listWidget.setSizePolicy(sizePolicy3)
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(250, 0))
        self.listWidget.setSizeIncrement(QSize(0, 25))
        self.listWidget.setBaseSize(QSize(0, 0))
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.listWidget.setLayoutDirection(Qt.LeftToRight)
        self.listWidget.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-left : 20px solid rgb(30, 30, 30);\n"
"	color: rgb(125, 125, 125);\n"
"	font: 10pt 'ProximaNova-Medium';\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	border-left : 5px solid rgb(30, 30, 30);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(125, 125, 125);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(125, 125, 125);\n"
"}\n"
"\n"
"")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAutoScroll(False)
        self.listWidget.setAutoScrollMargin(1)
        self.listWidget.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setIconSize(QSize(20, 20))
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(0)
        self.listWidget.setGridSize(QSize(0, 25))
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setItemAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.listWidget)

        self.Space_CurrL = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.Space_CurrL)
####################################################
        self.Space_PS = QSpacerItem(40, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(self.Space_PS)
        # self.Space_HP = QSpacerItem(40, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)
        # self.verticalLayout_4.addItem(self.Space_HP)
        self.Label_Settings = QPushButton(self.frame_top_menu)
        self.Label_Settings.setObjectName(u"Label_Settings")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Settings.sizePolicy().hasHeightForWidth())
        self.Label_Settings.setSizePolicy(sizePolicy)
        self.Label_Settings.setMinimumSize(QSize(0, 0))
        self.Label_Settings.setMaximumSize(QSize(16777215, 0))
        self.Label_Settings.setFocusPolicy(Qt.NoFocus)
        self.Label_Settings.setAcceptDrops(False)
        self.Label_Settings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(120, 120, 120);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 10pt 'Proxima Nova Lt';\n"
"}\n"
"")

        self.Label_Settings.setFlat(False)

        self.verticalLayout_4.addWidget(self.Label_Settings)

        self.horizontalSpacer_4 = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_4)

        self.Line_Settings = QFrame(self.frame_top_menu)
        self.Line_Settings.setObjectName(u"Line_Settings")
        self.Line_Settings.setSizePolicy(sizePolicy)
        self.Line_Settings.setMinimumSize(QSize(0, 3))
        self.Line_Settings.setMaximumSize(QSize(16777215, 3))
        self.Line_Settings.setAutoFillBackground(False)
        self.Line_Settings.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.Line_Settings.setFrameShape(QFrame.HLine)
        self.Line_Settings.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.Line_Settings)
        
        self.Space_HL = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(self.Space_PL)
####################################################
        icon1 = QIcon()
        icon1.addFile(u"icons/listItems/greyMarker.png", QSize(), QIcon.Normal, QIcon.Off)
        self.listSettings = QListWidget(self.frame_top_menu)
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(200, 200, 200, 255))
        brush1.setStyle(Qt.NoBrush)
        __qlistwidgetitem = QListWidgetItem(self.listSettings)
        __qlistwidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem.setBackground(brush1);
        __qlistwidgetitem.setForeground(brush);
        brush2 = QBrush(QColor(200, 200, 200, 255))
        brush2.setStyle(Qt.NoBrush)
        __qlistwidgetitem1 = QListWidgetItem(self.listSettings)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem1.setForeground(brush2);
        self.listSettings.setObjectName(u"listWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.listSettings.setSizePolicy(sizePolicy3)
        self.listSettings.setMinimumSize(QSize(0, 0))
        self.listSettings.setMaximumSize(QSize(250, 0))
        self.listSettings.setSizeIncrement(QSize(0, 25))
        self.listSettings.setBaseSize(QSize(0, 0))
        self.listSettings.setFocusPolicy(Qt.NoFocus)
        self.listSettings.setContextMenuPolicy(Qt.NoContextMenu)
        self.listSettings.setLayoutDirection(Qt.LeftToRight)
        self.listSettings.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-left : 20px solid rgb(30, 30, 30);\n"
"	color: rgb(125, 125, 125);\n"
"	font: 10pt 'ProximaNova-Medium';\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	border-left : 5px solid rgb(30, 30, 30);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(125, 125, 125);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(125, 125, 125);\n"
"}\n"
"\n"
"")
        self.listSettings.setFrameShape(QFrame.NoFrame)
        self.listSettings.setMidLineWidth(0)
        self.listSettings.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listSettings.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listSettings.setAutoScroll(False)
        self.listSettings.setAutoScrollMargin(1)
        self.listSettings.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.listSettings.setProperty("showDropIndicator", False)
        self.listSettings.setDragDropMode(QAbstractItemView.InternalMove)
        self.listSettings.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listSettings.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listSettings.setDefaultDropAction(Qt.IgnoreAction)
        self.listSettings.setIconSize(QSize(20, 20))
        self.listSettings.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listSettings.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listSettings.setMovement(QListView.Free)
        self.listSettings.setFlow(QListView.TopToBottom)
        self.listSettings.setResizeMode(QListView.Adjust)
        self.listSettings.setLayoutMode(QListView.SinglePass)
        self.listSettings.setSpacing(0)
        self.listSettings.setGridSize(QSize(0, 25))
        self.listSettings.setUniformItemSizes(False)
        self.listSettings.setItemAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.listSettings)
####################################################
####################################################    
        self.Btn_Playback = QPushButton(self.frame_top_menu)
        self.Btn_Playback.setObjectName(u"Btn_Playback")
        # sizePolicy.setHeightForWidth(self.Btn_Playback.sizePolicy().hasHeightForWidth())
        self.Btn_Playback.setSizePolicy(sizePolicy)
        self.Btn_Playback.setMinimumSize(QSize(0, 0))
        self.Btn_Playback.setMaximumSize(QSize(16777215, 0))
        self.Btn_Playback.setFocusPolicy(Qt.NoFocus)
        self.Btn_Playback.setLayoutDirection(Qt.RightToLeft)
        self.Btn_Playback.setStyleSheet(u"QPushButton {\n"
"	color: rgb(120, 120, 120);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 10pt 'ProximaNova-Medium';\n"
"}")
        self.Btn_Playback.setText(u" Pending                         ")
        self.Btn_Playback.setIconSize(QSize(20, 20))
        self.Btn_Playback.setFlat(True)

        self.verticalLayout_4.addWidget(self.Btn_Playback)

        self.Space_PP = QSpacerItem(40, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(self.Space_PP)

        self.Label_Process = QPushButton(self.frame_top_menu)
        self.Label_Process.setObjectName(u"Label_Process")
        self.Label_Process.setSizePolicy(sizePolicy)
        self.Label_Process.setMinimumSize(QSize(0, 0))
        self.Label_Process.setMaximumSize(QSize(16777215, 0))
        self.Label_Process.setFocusPolicy(Qt.NoFocus)
        self.Label_Process.setStyleSheet(u"QPushButton {\n"
"	color: rgb(179, 179, 179);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px solid;\n"
"	font: 9pt 'Proxima Nova Lt';\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.Label_Process)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_3)

        self.Line_Process = QFrame(self.frame_top_menu)
        self.Line_Process.setObjectName(u"Line_Process")
        self.Line_Process.setSizePolicy(sizePolicy)
        self.Line_Process.setMinimumSize(QSize(0, 0))
        self.Line_Process.setMaximumSize(QSize(16777215, 0))
        self.Line_Process.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.Line_Process.setFrameShape(QFrame.HLine)
        self.Line_Process.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.Line_Process)

        self.Space_PL2 = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.Space_PL2)

        self.listHelpProcess = QListWidget(self.frame_top_menu)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        QListWidgetItem(self.listHelpProcess)
        self.listHelpProcess.setObjectName(u"listHelpProcess")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.listHelpProcess.setSizePolicy(sizePolicy3)
        self.listHelpProcess.setMinimumSize(QSize(0, 0))
        self.listHelpProcess.setMaximumSize(QSize(16777215, 0))
        self.listHelpProcess.setSizeIncrement(QSize(0, 25))
        self.listHelpProcess.setFocusPolicy(Qt.NoFocus)
        self.listHelpProcess.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(155, 155, 155);\n"
"	border : 0px solid #FF7550;\n"
"	font: 10pt 'ProximaNova-Medium';\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(155, 155, 155);	\n"
"}\n"
"")
        self.listHelpProcess.setFrameShape(QFrame.NoFrame)
        self.listHelpProcess.setFrameShadow(QFrame.Plain)
        self.listHelpProcess.setLineWidth(0)
        self.listHelpProcess.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listHelpProcess.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listHelpProcess.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listHelpProcess.setAutoScroll(False)
        self.listHelpProcess.setAutoScrollMargin(5)
        self.listHelpProcess.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listHelpProcess.setProperty("showDropIndicator", False)
        self.listHelpProcess.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listHelpProcess.setDefaultDropAction(Qt.IgnoreAction)
        self.listHelpProcess.setSelectionMode(QAbstractItemView.NoSelection)
        self.listHelpProcess.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listHelpProcess.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listHelpProcess.setMovement(QListView.Free)
        self.listHelpProcess.setResizeMode(QListView.Adjust)
        self.listHelpProcess.setGridSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.listHelpProcess)

        self.Space_PC = QSpacerItem(40, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(self.Space_PC)

        self.Label_Controls = QPushButton(self.frame_top_menu)
        self.Label_Controls.setObjectName(u"Label_Controls")
        sizePolicy.setHeightForWidth(self.Label_Controls.sizePolicy().hasHeightForWidth())
        self.Label_Controls.setSizePolicy(sizePolicy)
        self.Label_Controls.setMinimumSize(QSize(0, 0))
        self.Label_Controls.setMaximumSize(QSize(16777215, 0))
        self.Label_Controls.setFocusPolicy(Qt.NoFocus)
        self.Label_Controls.setStyleSheet(u"QPushButton {\n"
"	color: rgb(179, 179, 179);\n"
"	background-color: rgb(30, 30, 30);\n"
"	font: 9pt 'Proxima Nova Lt';\n"
"	border: 0px solid;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.Label_Controls)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer)

        self.Line_Controls = QFrame(self.frame_top_menu)
        self.Line_Controls.setObjectName(u"Line_Controls")
        self.Line_Controls.setSizePolicy(sizePolicy)
        self.Line_Controls.setMaximumSize(QSize(16777215, 0))
        self.Line_Controls.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.Line_Controls.setFrameShape(QFrame.HLine)
        self.Line_Controls.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.Line_Controls)

        self.Space_CL = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.Space_CL)

        self.listHelpControls = QListWidget(self.frame_top_menu)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        QListWidgetItem(self.listHelpControls)
        self.listHelpControls.setObjectName(u"listHelpControls")
        self.listHelpControls.setSizePolicy(sizePolicy)
        self.listHelpControls.setMinimumSize(QSize(0, 0))
        self.listHelpControls.setMaximumSize(QSize(16777215, 0))
        self.listHelpControls.setSizeIncrement(QSize(0, 25))
        self.listHelpControls.setFocusPolicy(Qt.NoFocus)
        self.listHelpControls.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(155, 155, 155);\n"
"	border : 0px solid #FF7550;\n"
"	font: 10pt 'ProximaNova-Medium';\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(155, 155, 155);	\n"
"}\n"
"")
        self.listHelpControls.setFrameShape(QFrame.NoFrame)
        self.listHelpControls.setFrameShadow(QFrame.Plain)
        self.listHelpControls.setLineWidth(0)
        self.listHelpControls.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listHelpControls.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listHelpControls.setAutoScroll(False)
        self.listHelpControls.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listHelpControls.setProperty("showDropIndicator", False)
        self.listHelpControls.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listHelpControls.setDefaultDropAction(Qt.IgnoreAction)
        self.listHelpControls.setSelectionMode(QAbstractItemView.NoSelection)
        self.listHelpControls.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listHelpControls.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listHelpControls.setMovement(QListView.Free)
        self.listHelpControls.setResizeMode(QListView.Adjust)
        self.listHelpControls.setGridSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.listHelpControls)


        self.verticalLayout_3.addWidget(self.frame_top_menu, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(60, 30, 60, 0) #left, top, right, bottom
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border: 0px solid;")
        self.MplWidget = QWidget()
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setEnabled(True)
        self.stackedWidget.addWidget(self.MplWidget)
        self.VideoWidget = QWidget()
        self.VideoWidget.setObjectName(u"VideoWidget")
        self.stackedWidget.addWidget(self.VideoWidget)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        ''' add icons to the menu bar '''
        pathIcon = os.getcwd() + "\\" + "icons\\"
        self.repaint_button(self.Btn_Video, pathIcon + "importVideo.png")
        self.repaint_button(self.Btn_Import, pathIcon + "importData.png")
        self.repaint_button(self.Btn_Run, pathIcon + "runProgram.png")
        self.repaint_button(self.Btn_Help, pathIcon + "help.png")

        QMetaObject.connectSlotsByName(MainWindow)

    def repaint_button(self, button, image):
        Icon = QIcon()
        Icon.addFile(image, QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(Icon)
        button.repaint()

    def resizeWindow(self, width, height):
        main_link.setMaximumSize(QSize(width, height))
        main_link.setMinimumSize(QSize(int(width), int(height*.9)))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RMC Video Sync", None))
        self.Btn_Video.setText(QCoreApplication.translate("MainWindow", u"   Import Video   ", None))
        self.Btn_Import.setText(QCoreApplication.translate("MainWindow", u"   Import Data     ", None))
        self.Btn_Run.setText(QCoreApplication.translate("MainWindow", u"   Run Program   ", None))
        self.Btn_Help.setText(QCoreApplication.translate("MainWindow", u"   Help                   ", None))
        self.Label_Parameters.setText(QCoreApplication.translate("MainWindow", u"PARAMETERS                        ", None))
        self.Label_Settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS                              ", None))
        self.Empty.setText(QCoreApplication.translate("MainWindow", u"   Empty                               ", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.Label_Process.setText(QCoreApplication.translate("MainWindow", u"PROCESS                                ", None))

        __sortingEnabled1 = self.listHelpProcess.isSortingEnabled()
        self.listHelpProcess.setSortingEnabled(False)
        ___qlistwidgetitem = self.listHelpProcess.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"        1. Import the video file", None));
        ___qlistwidgetitem1 = self.listHelpProcess.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"            and the RMCTool's", None));
        ___qlistwidgetitem2 = self.listHelpProcess.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"            plot file (syncronized)", None));
        ___qlistwidgetitem3 = self.listHelpProcess.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"        2. Select between one ", None));
        ___qlistwidgetitem4 = self.listHelpProcess.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"            and three parameters ", None));
        ___qlistwidgetitem5 = self.listHelpProcess.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"             to be displayed", None));

        ___qlistwidgetitem6 = self.listHelpProcess.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"        3. Choose to enable or", None));
        ___qlistwidgetitem7 = self.listHelpProcess.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"            disable plot scrolling", None));
        ___qlistwidgetitem8 = self.listHelpProcess.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"        4. Choose to enable or", None));
        ___qlistwidgetitem9 = self.listHelpProcess.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"            disable progress bar", None));

        ___qlistwidgetitem10 = self.listHelpProcess.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"        5. Run the program and ", None));
        ___qlistwidgetitem11 = self.listHelpProcess.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"            wait for the video to ", None));
        ___qlistwidgetitem12 = self.listHelpProcess.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"            upload and convert", None));

        ___qlistwidgetitem13 = self.listHelpProcess.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"        6. Control the program", None));
        ___qlistwidgetitem14 = self.listHelpProcess.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"            using the arrow keys ", None));
        ___qlistwidgetitem15 = self.listHelpProcess.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"            and the spacebar", None));
        self.listHelpProcess.setSortingEnabled(__sortingEnabled1)

        self.Label_Controls.setText(QCoreApplication.translate("MainWindow", u"CONTROLS                              ", None))

        __sortingEnabled2 = self.listHelpControls.isSortingEnabled()
        self.listHelpControls.setSortingEnabled(False)
        ___qlistwidgetitem12 = self.listHelpControls.item(0)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"       play/pause: spacebar", None));
        ___qlistwidgetitem13 = self.listHelpControls.item(1)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"       slowmo: down arrow", None));
        ___qlistwidgetitem14 = self.listHelpControls.item(2)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"       fast forward: up arrow", None));
        ___qlistwidgetitem15 = self.listHelpControls.item(3)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"       step up: right arrow", None));
        ___qlistwidgetitem16 = self.listHelpControls.item(4)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"       step down: left arrow", None));
        ___qlistwidgetitem17 = self.listHelpControls.item(5)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"       hide labels: left click on", None));
        ___qlistwidgetitem18 = self.listHelpControls.item(6)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"       the left half of the plot", None));
        ___qlistwidgetitem19 = self.listHelpControls.item(7)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"       zoom in/out: left click on", None));
        ___qlistwidgetitem20 = self.listHelpControls.item(8)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"       the right half of the plot", None));
        self.listHelpControls.setSortingEnabled(__sortingEnabled2)



    # retranslateUi

