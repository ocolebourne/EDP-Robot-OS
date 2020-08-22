# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 321, 481))
        self.stackedWidget.setStyleSheet("background-color: #ffffff\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(25, 25))
        self.label_2.setMaximumSize(QtCore.QSize(25, 25))
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Product GUI/Initial .ui/Images/wifi.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.button_power0 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_power0.sizePolicy().hasHeightForWidth())
        self.button_power0.setSizePolicy(sizePolicy)
        self.button_power0.setMinimumSize(QtCore.QSize(40, 40))
        self.button_power0.setMaximumSize(QtCore.QSize(40, 40))
        self.button_power0.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_power0.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_power0.setIcon(icon)
        self.button_power0.setIconSize(QtCore.QSize(28, 28))
        self.button_power0.setObjectName("button_power0")
        self.horizontalLayout.addWidget(self.button_power0)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setIndent(20)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_name0 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(18)
        self.label_name0.setFont(font)
        self.label_name0.setTextFormat(QtCore.Qt.PlainText)
        self.label_name0.setIndent(20)
        self.label_name0.setObjectName("label_name0")
        self.verticalLayout.addWidget(self.label_name0)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, -1)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_logout0 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_logout0.sizePolicy().hasHeightForWidth())
        self.button_logout0.setSizePolicy(sizePolicy)
        self.button_logout0.setMinimumSize(QtCore.QSize(50, 50))
        self.button_logout0.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_logout0.setFont(font)
        self.button_logout0.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 10px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #e0e0e0\n"
"        \n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_logout0.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_logout0.setIcon(icon1)
        self.button_logout0.setIconSize(QtCore.QSize(30, 30))
        self.button_logout0.setObjectName("button_logout0")
        self.horizontalLayout_2.addWidget(self.button_logout0)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.button_start0 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start0.sizePolicy().hasHeightForWidth())
        self.button_start0.setSizePolicy(sizePolicy)
        self.button_start0.setMinimumSize(QtCore.QSize(100, 50))
        self.button_start0.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_start0.setFont(font)
        self.button_start0.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 10px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"        color: #5C3e91;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_start0.setIconSize(QtCore.QSize(40, 40))
        self.button_start0.setObjectName("button_start0")
        self.horizontalLayout_2.addWidget(self.button_start0)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 321, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_back1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back1.sizePolicy().hasHeightForWidth())
        self.button_back1.setSizePolicy(sizePolicy)
        self.button_back1.setMinimumSize(QtCore.QSize(40, 40))
        self.button_back1.setMaximumSize(QtCore.QSize(40, 40))
        self.button_back1.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_back1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back1.setIcon(icon2)
        self.button_back1.setIconSize(QtCore.QSize(30, 30))
        self.button_back1.setObjectName("button_back1")
        self.horizontalLayout_3.addWidget(self.button_back1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(25, 25))
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Product GUI/Initial .ui/Images/wifi.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignVCenter)
        self.button_power1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_power1.sizePolicy().hasHeightForWidth())
        self.button_power1.setSizePolicy(sizePolicy)
        self.button_power1.setMinimumSize(QtCore.QSize(40, 40))
        self.button_power1.setMaximumSize(QtCore.QSize(40, 40))
        self.button_power1.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_power1.setText("")
        self.button_power1.setIcon(icon)
        self.button_power1.setIconSize(QtCore.QSize(28, 28))
        self.button_power1.setObjectName("button_power1")
        self.horizontalLayout_3.addWidget(self.button_power1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.stackedWidget_home_menu = QtWidgets.QStackedWidget(self.verticalLayoutWidget_2)
        self.stackedWidget_home_menu.setObjectName("stackedWidget_home_menu")
        self.page_project_list = QtWidgets.QWidget()
        self.page_project_list.setObjectName("page_project_list")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_project_list)
        self.gridLayout_3.setContentsMargins(20, 2, 20, 2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_project_list = QtWidgets.QScrollArea(self.page_project_list)
        self.scrollArea_project_list.setStyleSheet("QScrollBar:vertical {\n"
"  background-color: #DBDCE0;\n"
"  width: 12px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 0px solid #ADB0B3;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #DBDCE0;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #423F3F;\n"
"  border: 0px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 0px solid #423F3F;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"background-color: transparent;\n"
"}")
        self.scrollArea_project_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_project_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_project_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_project_list.setWidgetResizable(True)
        self.scrollArea_project_list.setObjectName("scrollArea_project_list")
        self.scrollAreaWidgetContents_project_list = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_project_list.setGeometry(QtCore.QRect(0, 0, 262, 279))
        self.scrollAreaWidgetContents_project_list.setObjectName("scrollAreaWidgetContents_project_list")
        self.verticalLayout_project_list = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_project_list)
        self.verticalLayout_project_list.setContentsMargins(8, 5, 7, 5)
        self.verticalLayout_project_list.setObjectName("verticalLayout_project_list")
        self.label_noentries = QtWidgets.QLabel(self.scrollAreaWidgetContents_project_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_noentries.sizePolicy().hasHeightForWidth())
        self.label_noentries.setSizePolicy(sizePolicy)
        self.label_noentries.setMaximumSize(QtCore.QSize(155555, 50))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        self.label_noentries.setFont(font)
        self.label_noentries.setObjectName("label_noentries")
        self.verticalLayout_project_list.addWidget(self.label_noentries)
        self.frame_entry = QtWidgets.QFrame(self.scrollAreaWidgetContents_project_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_entry.sizePolicy().hasHeightForWidth())
        self.frame_entry.setSizePolicy(sizePolicy)
        self.frame_entry.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_entry.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_entry.setStyleSheet("QFrame {\n"
"        \n"
"    background-color: #ffffff;\n"
"    border-radius: 5px;\n"
"\n"
"}")
        self.frame_entry.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_entry.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_entry.setObjectName("frame_entry")
        self.gridLayout_entry = QtWidgets.QGridLayout(self.frame_entry)
        self.gridLayout_entry.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_entry.setVerticalSpacing(0)
        self.gridLayout_entry.setObjectName("gridLayout_entry")
        self.label_entry_title = QtWidgets.QLabel(self.frame_entry)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(7)
        self.label_entry_title.setFont(font)
        self.label_entry_title.setObjectName("label_entry_title")
        self.gridLayout_entry.addWidget(self.label_entry_title, 0, 0, 1, 1)
        self.label_entry_desc = QtWidgets.QLabel(self.frame_entry)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(7)
        self.label_entry_desc.setFont(font)
        self.label_entry_desc.setObjectName("label_entry_desc")
        self.gridLayout_entry.addWidget(self.label_entry_desc, 1, 0, 1, 1)
        self.button_entry = QtWidgets.QPushButton(self.frame_entry)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_entry.sizePolicy().hasHeightForWidth())
        self.button_entry.setSizePolicy(sizePolicy)
        self.button_entry.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_entry.setFont(font)
        self.button_entry.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 10px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #f8f8f8\n"
"        \n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_entry.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Product GUI/Initial .ui/Images/left_arrow1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_entry.setIcon(icon3)
        self.button_entry.setObjectName("button_entry")
        self.gridLayout_entry.addWidget(self.button_entry, 0, 1, 2, 1)
        self.verticalLayout_project_list.addWidget(self.frame_entry)
        self.scrollArea_project_list.setWidget(self.scrollAreaWidgetContents_project_list)
        self.gridLayout_3.addWidget(self.scrollArea_project_list, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(5, 10, 10, 10)
        self.gridLayout_7.setHorizontalSpacing(10)
        self.gridLayout_7.setVerticalSpacing(2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.button_refresh2_1 = QtWidgets.QPushButton(self.page_project_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh2_1.sizePolicy().hasHeightForWidth())
        self.button_refresh2_1.setSizePolicy(sizePolicy)
        self.button_refresh2_1.setMinimumSize(QtCore.QSize(30, 30))
        self.button_refresh2_1.setMaximumSize(QtCore.QSize(20, 20))
        self.button_refresh2_1.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 5px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_refresh2_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_refresh2_1.setIcon(icon4)
        self.button_refresh2_1.setIconSize(QtCore.QSize(25, 25))
        self.button_refresh2_1.setObjectName("button_refresh2_1")
        self.gridLayout_7.addWidget(self.button_refresh2_1, 0, 1, 2, 1, QtCore.Qt.AlignVCenter)
        self.label_title2_1 = QtWidgets.QLabel(self.page_project_list)
        self.label_title2_1.setMaximumSize(QtCore.QSize(155555, 167777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        self.label_title2_1.setFont(font)
        self.label_title2_1.setObjectName("label_title2_1")
        self.gridLayout_7.addWidget(self.label_title2_1, 0, 0, 2, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.stackedWidget_home_menu.addWidget(self.page_project_list)
        self.page_tutorials_list = QtWidgets.QWidget()
        self.page_tutorials_list.setObjectName("page_tutorials_list")
        self.gridLayout = QtWidgets.QGridLayout(self.page_tutorials_list)
        self.gridLayout.setContentsMargins(20, 2, 20, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_tutorials_list = QtWidgets.QScrollArea(self.page_tutorials_list)
        self.scrollArea_tutorials_list.setStyleSheet("QScrollBar:vertical {\n"
"  background-color: #ECF0F3;\n"
"  width: 12px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 0px solid #ADB0B3;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #DBDCE0;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #423F3F;\n"
"  border: 0px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 0px solid #423F3F;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea_tutorials_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_tutorials_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_tutorials_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_tutorials_list.setWidgetResizable(True)
        self.scrollArea_tutorials_list.setObjectName("scrollArea_tutorials_list")
        self.scrollAreaWidgetContents_tutorials_list = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_tutorials_list.setGeometry(QtCore.QRect(0, 0, 43, 16))
        self.scrollAreaWidgetContents_tutorials_list.setObjectName("scrollAreaWidgetContents_tutorials_list")
        self.verticalLayout_tutorials_list = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_tutorials_list)
        self.verticalLayout_tutorials_list.setContentsMargins(8, 0, 7, 0)
        self.verticalLayout_tutorials_list.setObjectName("verticalLayout_tutorials_list")
        self.scrollArea_tutorials_list.setWidget(self.scrollAreaWidgetContents_tutorials_list)
        self.gridLayout.addWidget(self.scrollArea_tutorials_list, 1, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(5, 10, 10, 10)
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.button_refresh2_2 = QtWidgets.QPushButton(self.page_tutorials_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh2_2.sizePolicy().hasHeightForWidth())
        self.button_refresh2_2.setSizePolicy(sizePolicy)
        self.button_refresh2_2.setMinimumSize(QtCore.QSize(30, 30))
        self.button_refresh2_2.setMaximumSize(QtCore.QSize(20, 20))
        self.button_refresh2_2.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 5px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"\n"
"")
        self.button_refresh2_2.setText("")
        self.button_refresh2_2.setIcon(icon4)
        self.button_refresh2_2.setIconSize(QtCore.QSize(25, 25))
        self.button_refresh2_2.setObjectName("button_refresh2_2")
        self.gridLayout_8.addWidget(self.button_refresh2_2, 0, 1, 2, 1, QtCore.Qt.AlignVCenter)
        self.label_title2_2 = QtWidgets.QLabel(self.page_tutorials_list)
        self.label_title2_2.setMaximumSize(QtCore.QSize(155555, 167777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        self.label_title2_2.setFont(font)
        self.label_title2_2.setObjectName("label_title2_2")
        self.gridLayout_8.addWidget(self.label_title2_2, 0, 0, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.stackedWidget_home_menu.addWidget(self.page_tutorials_list)
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setObjectName("page_settings")
        self.stackedWidget_home_menu.addWidget(self.page_settings)
        self.verticalLayout_2.addWidget(self.stackedWidget_home_menu)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setContentsMargins(20, 5, 20, 20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_projects1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_projects1.sizePolicy().hasHeightForWidth())
        self.button_projects1.setSizePolicy(sizePolicy)
        self.button_projects1.setMinimumSize(QtCore.QSize(20, 50))
        self.button_projects1.setMaximumSize(QtCore.QSize(80, 50))
        self.button_projects1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_projects1.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"        border-radius: 10px;\n"
"        border-image: url(\"Images/buttons/project_button.png\");\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"        \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"                        border-image: url(\"Images/buttons/project_button_s.png\");\n"
"}\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_projects1.setText("")
        self.button_projects1.setIconSize(QtCore.QSize(30, 30))
        self.button_projects1.setCheckable(True)
        self.button_projects1.setChecked(True)
        self.button_projects1.setAutoExclusive(True)
        self.button_projects1.setFlat(False)
        self.button_projects1.setObjectName("button_projects1")
        self.horizontalLayout_4.addWidget(self.button_projects1)
        self.button_tutorials1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_tutorials1.sizePolicy().hasHeightForWidth())
        self.button_tutorials1.setSizePolicy(sizePolicy)
        self.button_tutorials1.setMinimumSize(QtCore.QSize(80, 50))
        self.button_tutorials1.setMaximumSize(QtCore.QSize(155555, 50))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_tutorials1.setFont(font)
        self.button_tutorials1.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"        border-radius: 10px;\n"
"        border-image: url(\"Images/buttons/tutorial_button.png\");\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"        \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"                        border-image: url(\"Images/buttons/tutorial_button_s.png\");\n"
"}\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_tutorials1.setText("")
        self.button_tutorials1.setIconSize(QtCore.QSize(30, 30))
        self.button_tutorials1.setCheckable(True)
        self.button_tutorials1.setAutoExclusive(True)
        self.button_tutorials1.setObjectName("button_tutorials1")
        self.horizontalLayout_4.addWidget(self.button_tutorials1)
        self.button_settings1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_settings1.sizePolicy().hasHeightForWidth())
        self.button_settings1.setSizePolicy(sizePolicy)
        self.button_settings1.setMinimumSize(QtCore.QSize(80, 50))
        self.button_settings1.setMaximumSize(QtCore.QSize(155555, 50))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_settings1.setFont(font)
        self.button_settings1.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"        border-radius: 10px;\n"
"        border-image: url(\"Images/buttons/settings_button.png\");\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"        \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"                        border-image: url(\"Images/buttons/settings_button_s.png\");\n"
"}\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_settings1.setText("")
        self.button_settings1.setIconSize(QtCore.QSize(30, 30))
        self.button_settings1.setCheckable(True)
        self.button_settings1.setAutoExclusive(True)
        self.button_settings1.setObjectName("button_settings1")
        self.horizontalLayout_4.addWidget(self.button_settings1)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_back2 = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back2.sizePolicy().hasHeightForWidth())
        self.button_back2.setSizePolicy(sizePolicy)
        self.button_back2.setMinimumSize(QtCore.QSize(40, 40))
        self.button_back2.setMaximumSize(QtCore.QSize(40, 40))
        self.button_back2.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_back2.setText("")
        self.button_back2.setIcon(icon2)
        self.button_back2.setIconSize(QtCore.QSize(30, 30))
        self.button_back2.setObjectName("button_back2")
        self.horizontalLayout_5.addWidget(self.button_back2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label_wifi2 = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wifi2.sizePolicy().hasHeightForWidth())
        self.label_wifi2.setSizePolicy(sizePolicy)
        self.label_wifi2.setMinimumSize(QtCore.QSize(20, 20))
        self.label_wifi2.setMaximumSize(QtCore.QSize(25, 25))
        self.label_wifi2.setText("")
        self.label_wifi2.setPixmap(QtGui.QPixmap("../../Product GUI/Initial .ui/Images/wifi.png"))
        self.label_wifi2.setScaledContents(True)
        self.label_wifi2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_wifi2.setObjectName("label_wifi2")
        self.horizontalLayout_5.addWidget(self.label_wifi2)
        self.button_power2 = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_power2.sizePolicy().hasHeightForWidth())
        self.button_power2.setSizePolicy(sizePolicy)
        self.button_power2.setMinimumSize(QtCore.QSize(40, 40))
        self.button_power2.setMaximumSize(QtCore.QSize(40, 40))
        self.button_power2.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_power2.setText("")
        self.button_power2.setIcon(icon)
        self.button_power2.setIconSize(QtCore.QSize(28, 28))
        self.button_power2.setObjectName("button_power2")
        self.horizontalLayout_5.addWidget(self.button_power2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 10, 10, 10)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_lastupdate2 = QtWidgets.QLabel(self.page_3)
        self.label_lastupdate2.setMaximumSize(QtCore.QSize(16777215, 16777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        self.label_lastupdate2.setFont(font)
        self.label_lastupdate2.setObjectName("label_lastupdate2")
        self.gridLayout_2.addWidget(self.label_lastupdate2, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_title2 = QtWidgets.QLabel(self.page_3)
        self.label_title2.setMaximumSize(QtCore.QSize(155555, 167777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        self.label_title2.setFont(font)
        self.label_title2.setObjectName("label_title2")
        self.gridLayout_2.addWidget(self.label_title2, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.button_refresh2 = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh2.sizePolicy().hasHeightForWidth())
        self.button_refresh2.setSizePolicy(sizePolicy)
        self.button_refresh2.setMinimumSize(QtCore.QSize(40, 40))
        self.button_refresh2.setMaximumSize(QtCore.QSize(40, 40))
        self.button_refresh2.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 10px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_refresh2.setText("")
        self.button_refresh2.setIcon(icon4)
        self.button_refresh2.setIconSize(QtCore.QSize(30, 30))
        self.button_refresh2.setObjectName("button_refresh2")
        self.gridLayout_2.addWidget(self.button_refresh2, 0, 1, 2, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.button_run2 = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_run2.sizePolicy().hasHeightForWidth())
        self.button_run2.setSizePolicy(sizePolicy)
        self.button_run2.setMinimumSize(QtCore.QSize(120, 120))
        self.button_run2.setMaximumSize(QtCore.QSize(120, 120))
        self.button_run2.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 60px;\n"
"\n"
"        background-color: #532B86;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:checked {\n"
"              background-color: #7352A7;\n"
"        \n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_run2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/runblur.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_run2.setIcon(icon5)
        self.button_run2.setIconSize(QtCore.QSize(75, 75))
        self.button_run2.setCheckable(True)
        self.button_run2.setObjectName("button_run2")
        self.verticalLayout_3.addWidget(self.button_run2, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.frame_debug2 = QtWidgets.QFrame(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_debug2.sizePolicy().hasHeightForWidth())
        self.frame_debug2.setSizePolicy(sizePolicy)
        self.frame_debug2.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_debug2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_debug2.setStyleSheet("QFrame {\n"
"        \n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.frame_debug2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_debug2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_debug2.setObjectName("frame_debug2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_debug2)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_debug2 = QtWidgets.QLabel(self.frame_debug2)
        self.label_debug2.setMaximumSize(QtCore.QSize(16777215, 16777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        self.label_debug2.setFont(font)
        self.label_debug2.setStyleSheet("QLabel {\n"
"border: none;\n"
"}")
        self.label_debug2.setObjectName("label_debug2")
        self.verticalLayout_4.addWidget(self.label_debug2)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_debug2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"  background-color: #DBDCE0;\n"
"  width: 12px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 0px solid #ADB0B3;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #DBDCE0;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #423F3F;\n"
"  border: 0px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 0px solid #423F3F;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"background-color: transparent;\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 271, 92))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_debugpanel2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_debugpanel2.sizePolicy().hasHeightForWidth())
        self.label_debugpanel2.setSizePolicy(sizePolicy)
        self.label_debugpanel2.setMaximumSize(QtCore.QSize(270, 16777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        self.label_debugpanel2.setFont(font)
        self.label_debugpanel2.setStyleSheet("QLabel {\n"
"border: none;\n"
"}")
        self.label_debugpanel2.setText("")
        self.label_debugpanel2.setTextFormat(QtCore.Qt.PlainText)
        self.label_debugpanel2.setWordWrap(True)
        self.label_debugpanel2.setObjectName("label_debugpanel2")
        self.verticalLayout_7.addWidget(self.label_debugpanel2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_3.addWidget(self.frame_debug2)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.layoutWidget = QtWidgets.QWidget(self.page_4)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_back3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back3.sizePolicy().hasHeightForWidth())
        self.button_back3.setSizePolicy(sizePolicy)
        self.button_back3.setMinimumSize(QtCore.QSize(40, 40))
        self.button_back3.setMaximumSize(QtCore.QSize(40, 40))
        self.button_back3.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_back3.setText("")
        self.button_back3.setIcon(icon2)
        self.button_back3.setIconSize(QtCore.QSize(30, 30))
        self.button_back3.setObjectName("button_back3")
        self.horizontalLayout_6.addWidget(self.button_back3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.label_wifi3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wifi3.sizePolicy().hasHeightForWidth())
        self.label_wifi3.setSizePolicy(sizePolicy)
        self.label_wifi3.setMinimumSize(QtCore.QSize(25, 25))
        self.label_wifi3.setMaximumSize(QtCore.QSize(25, 25))
        self.label_wifi3.setText("")
        self.label_wifi3.setPixmap(QtGui.QPixmap("../../Product GUI/Initial .ui/Images/wifi.png"))
        self.label_wifi3.setScaledContents(True)
        self.label_wifi3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_wifi3.setObjectName("label_wifi3")
        self.horizontalLayout_6.addWidget(self.label_wifi3)
        self.button_power3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_power3.sizePolicy().hasHeightForWidth())
        self.button_power3.setSizePolicy(sizePolicy)
        self.button_power3.setMinimumSize(QtCore.QSize(40, 40))
        self.button_power3.setMaximumSize(QtCore.QSize(40, 40))
        self.button_power3.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_power3.setText("")
        self.button_power3.setIcon(icon)
        self.button_power3.setIconSize(QtCore.QSize(28, 28))
        self.button_power3.setObjectName("button_power3")
        self.horizontalLayout_6.addWidget(self.button_power3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 10, 10, 10)
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_lastupdate3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_lastupdate3.setMaximumSize(QtCore.QSize(16777215, 16777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        self.label_lastupdate3.setFont(font)
        self.label_lastupdate3.setObjectName("label_lastupdate3")
        self.gridLayout_4.addWidget(self.label_lastupdate3, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_title3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_title3.setMaximumSize(QtCore.QSize(155555, 167777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        self.label_title3.setFont(font)
        self.label_title3.setObjectName("label_title3")
        self.gridLayout_4.addWidget(self.label_title3, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.button_refresh3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh3.sizePolicy().hasHeightForWidth())
        self.button_refresh3.setSizePolicy(sizePolicy)
        self.button_refresh3.setMinimumSize(QtCore.QSize(40, 40))
        self.button_refresh3.setMaximumSize(QtCore.QSize(40, 40))
        self.button_refresh3.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 10px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_refresh3.setText("")
        self.button_refresh3.setIcon(icon4)
        self.button_refresh3.setIconSize(QtCore.QSize(30, 30))
        self.button_refresh3.setObjectName("button_refresh3")
        self.gridLayout_4.addWidget(self.button_refresh3, 0, 1, 2, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.button_run3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_run3.sizePolicy().hasHeightForWidth())
        self.button_run3.setSizePolicy(sizePolicy)
        self.button_run3.setMinimumSize(QtCore.QSize(120, 120))
        self.button_run3.setMaximumSize(QtCore.QSize(120, 120))
        self.button_run3.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 60px;\n"
"\n"
"        background-color: #532B86;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:checked {\n"
"              background-color: #7352A7;\n"
"        \n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_run3.setText("")
        self.button_run3.setIcon(icon5)
        self.button_run3.setIconSize(QtCore.QSize(75, 75))
        self.button_run3.setCheckable(True)
        self.button_run3.setObjectName("button_run3")
        self.verticalLayout_5.addWidget(self.button_run3, 0, QtCore.Qt.AlignHCenter)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.frame_debug3 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_debug3.sizePolicy().hasHeightForWidth())
        self.frame_debug3.setSizePolicy(sizePolicy)
        self.frame_debug3.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_debug3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_debug3.setStyleSheet("QFrame {\n"
"        \n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.frame_debug3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_debug3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_debug3.setObjectName("frame_debug3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_debug3)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_debug3 = QtWidgets.QLabel(self.frame_debug3)
        self.label_debug3.setMaximumSize(QtCore.QSize(16777215, 16777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        self.label_debug3.setFont(font)
        self.label_debug3.setStyleSheet("QLabel {\n"
"border: none;\n"
"}")
        self.label_debug3.setObjectName("label_debug3")
        self.verticalLayout_6.addWidget(self.label_debug3)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_debug3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setStyleSheet("QScrollBar:vertical {\n"
"  background-color: #DBDCE0;\n"
"  width: 12px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 0px solid #ADB0B3;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #DBDCE0;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #423F3F;\n"
"  border: 0px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 0px solid #423F3F;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"background-color: transparent;\n"
"}")
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 271, 92))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_debugpanel3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_debugpanel3.sizePolicy().hasHeightForWidth())
        self.label_debugpanel3.setSizePolicy(sizePolicy)
        self.label_debugpanel3.setMaximumSize(QtCore.QSize(270, 16777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        self.label_debugpanel3.setFont(font)
        self.label_debugpanel3.setStyleSheet("QLabel {\n"
"border: none;\n"
"}")
        self.label_debugpanel3.setText("")
        self.label_debugpanel3.setTextFormat(QtCore.Qt.PlainText)
        self.label_debugpanel3.setWordWrap(True)
        self.label_debugpanel3.setObjectName("label_debugpanel3")
        self.verticalLayout_8.addWidget(self.label_debugpanel3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea_2)
        self.verticalLayout_5.addWidget(self.frame_debug3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.page_5)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 321, 481))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.button_back4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back4.sizePolicy().hasHeightForWidth())
        self.button_back4.setSizePolicy(sizePolicy)
        self.button_back4.setMinimumSize(QtCore.QSize(40, 40))
        self.button_back4.setMaximumSize(QtCore.QSize(40, 40))
        self.button_back4.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_back4.setText("")
        self.button_back4.setIcon(icon2)
        self.button_back4.setIconSize(QtCore.QSize(30, 30))
        self.button_back4.setObjectName("button_back4")
        self.horizontalLayout_13.addWidget(self.button_back4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem10)
        self.label_wifi4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wifi4.sizePolicy().hasHeightForWidth())
        self.label_wifi4.setSizePolicy(sizePolicy)
        self.label_wifi4.setMinimumSize(QtCore.QSize(25, 25))
        self.label_wifi4.setMaximumSize(QtCore.QSize(25, 25))
        self.label_wifi4.setText("")
        self.label_wifi4.setPixmap(QtGui.QPixmap("../../Product GUI/Initial .ui/Images/wifi.png"))
        self.label_wifi4.setScaledContents(True)
        self.label_wifi4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_wifi4.setObjectName("label_wifi4")
        self.horizontalLayout_13.addWidget(self.label_wifi4)
        self.button_power4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_power4.sizePolicy().hasHeightForWidth())
        self.button_power4.setSizePolicy(sizePolicy)
        self.button_power4.setMinimumSize(QtCore.QSize(40, 40))
        self.button_power4.setMaximumSize(QtCore.QSize(40, 40))
        self.button_power4.setStyleSheet("QPushButton:hover{\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 20px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}\n"
"")
        self.button_power4.setText("")
        self.button_power4.setIcon(icon)
        self.button_power4.setIconSize(QtCore.QSize(28, 28))
        self.button_power4.setObjectName("button_power4")
        self.horizontalLayout_13.addWidget(self.button_power4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setContentsMargins(-1, 10, 10, 10)
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setVerticalSpacing(2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_lastupdate4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_lastupdate4.setMaximumSize(QtCore.QSize(16777215, 16777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        self.label_lastupdate4.setFont(font)
        self.label_lastupdate4.setObjectName("label_lastupdate4")
        self.gridLayout_11.addWidget(self.label_lastupdate4, 2, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_title4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_title4.setMaximumSize(QtCore.QSize(155555, 167777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        self.label_title4.setFont(font)
        self.label_title4.setObjectName("label_title4")
        self.gridLayout_11.addWidget(self.label_title4, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.button_refresh4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh4.sizePolicy().hasHeightForWidth())
        self.button_refresh4.setSizePolicy(sizePolicy)
        self.button_refresh4.setMinimumSize(QtCore.QSize(40, 40))
        self.button_refresh4.setMaximumSize(QtCore.QSize(40, 40))
        self.button_refresh4.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 10px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"              background-color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_refresh4.setText("")
        self.button_refresh4.setIcon(icon4)
        self.button_refresh4.setIconSize(QtCore.QSize(30, 30))
        self.button_refresh4.setObjectName("button_refresh4")
        self.gridLayout_11.addWidget(self.button_refresh4, 0, 1, 3, 1)
        self.label_desc4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_desc4.setMaximumSize(QtCore.QSize(155555, 167777))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        self.label_desc4.setFont(font)
        self.label_desc4.setObjectName("label_desc4")
        self.gridLayout_11.addWidget(self.label_desc4, 1, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_11)
        self.scrollArea_step_list = QtWidgets.QScrollArea(self.verticalLayoutWidget_5)
        self.scrollArea_step_list.setStyleSheet("QScrollBar:vertical {\n"
"  background-color: #f8f8f8;\n"
"  width: 12px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 0px solid #ADB0B3;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #D2D6D9;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #ADB0B3;\n"
"  border: 0px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 0px solid #1464A0;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}")
        self.scrollArea_step_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_step_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_step_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_step_list.setWidgetResizable(True)
        self.scrollArea_step_list.setObjectName("scrollArea_step_list")
        self.scrollAreaWidgetContents_step_list = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_step_list.setGeometry(QtCore.QRect(0, 0, 264, 313))
        self.scrollAreaWidgetContents_step_list.setObjectName("scrollAreaWidgetContents_step_list")
        self.verticalLayout_step_list = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_step_list)
        self.verticalLayout_step_list.setContentsMargins(8, 5, 7, 5)
        self.verticalLayout_step_list.setObjectName("verticalLayout_step_list")
        self.frame_tutorialentry = QtWidgets.QFrame(self.scrollAreaWidgetContents_step_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_tutorialentry.sizePolicy().hasHeightForWidth())
        self.frame_tutorialentry.setSizePolicy(sizePolicy)
        self.frame_tutorialentry.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_tutorialentry.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_tutorialentry.setStyleSheet("QFrame {\n"
"        \n"
"    background-color: #ffffff;\n"
"    border-radius: 5px;\n"
"\n"
"}")
        self.frame_tutorialentry.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tutorialentry.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tutorialentry.setObjectName("frame_tutorialentry")
        self.gridLayout_entry_4 = QtWidgets.QGridLayout(self.frame_tutorialentry)
        self.gridLayout_entry_4.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_entry_4.setObjectName("gridLayout_entry_4")
        self.button_tutorialentry = QtWidgets.QPushButton(self.frame_tutorialentry)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_tutorialentry.sizePolicy().hasHeightForWidth())
        self.button_tutorialentry.setSizePolicy(sizePolicy)
        self.button_tutorialentry.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_tutorialentry.setFont(font)
        self.button_tutorialentry.setStyleSheet("QPushButton:hover{\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"        border-radius: 10px;\n"
"\n"
"        background-color: #ffffff;\n"
"        font: regular large \"Raleway\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"                background-color: #f8f8f8\n"
"        \n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"       \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"}")
        self.button_tutorialentry.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../Product GUI/Initial .ui/Images/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_tutorialentry.setIcon(icon6)
        self.button_tutorialentry.setIconSize(QtCore.QSize(30, 30))
        self.button_tutorialentry.setObjectName("button_tutorialentry")
        self.gridLayout_entry_4.addWidget(self.button_tutorialentry, 0, 1, 2, 1)
        self.label_tutorialentry_title = QtWidgets.QLabel(self.frame_tutorialentry)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(7)
        self.label_tutorialentry_title.setFont(font)
        self.label_tutorialentry_title.setObjectName("label_tutorialentry_title")
        self.gridLayout_entry_4.addWidget(self.label_tutorialentry_title, 0, 0, 2, 1)
        self.verticalLayout_step_list.addWidget(self.frame_tutorialentry)
        self.scrollArea_step_list.setWidget(self.scrollAreaWidgetContents_step_list)
        self.verticalLayout_13.addWidget(self.scrollArea_step_list)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_2 = QtWidgets.QFrame(self.page_6)
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.button_wakeup = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_wakeup.sizePolicy().hasHeightForWidth())
        self.button_wakeup.setSizePolicy(sizePolicy)
        self.button_wakeup.setText("")
        self.button_wakeup.setObjectName("button_wakeup")
        self.gridLayout_10.addWidget(self.button_wakeup, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_home_menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">Hello</span></p></body></html>"))
        self.label_name0.setText(_translate("Form", "John"))
        self.button_start0.setText(_translate("Form", "Start"))
        self.label_noentries.setText(_translate("Form", "Title"))
        self.label_entry_title.setText(_translate("Form", "Title"))
        self.label_entry_desc.setText(_translate("Form", "Description"))
        self.label_title2_1.setText(_translate("Form", "Personal Projects"))
        self.label_title2_2.setText(_translate("Form", "Structured Tutorials"))
        self.label_lastupdate2.setText(_translate("Form", "Last Updated: xxx"))
        self.label_title2.setText(_translate("Form", "Title"))
        self.label_debug2.setText(_translate("Form", "Debug:"))
        self.label_lastupdate3.setText(_translate("Form", "Last Updated: xxx"))
        self.label_title3.setText(_translate("Form", "Tutorial name - Step 1"))
        self.label_debug3.setText(_translate("Form", "Debug:"))
        self.label_lastupdate4.setText(_translate("Form", "Last Updated: xxx"))
        self.label_title4.setText(_translate("Form", "Tutorial name:"))
        self.label_desc4.setText(_translate("Form", "Tutorial Description"))
        self.label_tutorialentry_title.setText(_translate("Form", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
