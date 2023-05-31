import mysql.connector
import sys
import pandas as pd
import numpy as np
import pandas as pdpi
import tensorflow as tf
import matplotlib.pyplot as plt
from PyQt6.QtCore import Qt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from sklearn import metrics
from sklearn.metrics import recall_score, f1_score, accuracy_score
from prettytable import PrettyTable
from tensorflow import keras
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from dnn import dn


class Ui_MainWindow(object):
    file_path = ""
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.close.setText(_translate("MainWindow", "..."))
        self.mmenu.setText(_translate("MainWindow", "   Menu"))
        self.mhome.setText(_translate("MainWindow", "   Home"))
        self.mtest.setText(_translate("MainWindow", "   Test"))
        self.mdatabase.setText(_translate("MainWindow", "   Database"))
        self.mgraphique.setText(_translate("MainWindow", "   Graphique"))
        self.mstring.setText(_translate("MainWindow", "    Stings"))
        self.mdonation.setText(_translate("MainWindow", "   Donation"))
        self.label.setText(_translate("MainWindow", "welcome !"))
        self.label_2.setText(_translate("MainWindow", "We love givin new vistors that chance to Test our app , Enter you email to try ! Then Test your data base ."))
        self.pushButton_9.setText(_translate("MainWindow", "Try "))
        self.pushButton_11.setText(_translate("MainWindow", "Chosse csv file "))
        self.pushButton_12.setText(_translate("MainWindow", "Test"))
        self.row_2.setPlaceholderText(_translate("MainWindow", "Enter nember of row"))
        self.toolButton_8.setText(_translate("MainWindow", "..."))
        self.pushButton.clicked.connect(self.annule)




    # loade data
    def load_csv(self):

            file_dialog = QtWidgets.QFileDialog()
            file_dialog.exec()
            Ui_MainWindow.file_path = file_dialog.selectedFiles()[0]
            print(Ui_MainWindow.file_path)
            self.df = pd.read_csv(Ui_MainWindow.file_path , nrows=50)
            self.datatable_2.setRowCount(self.df.shape[0])
            self.datatable_2.setColumnCount(self.df.shape[1])

            # Add the data to the table widget
            for i in range(self.df.shape[0]):
                    for j in range(self.df.shape[1]):
                            item = QtWidgets.QTableWidgetItem(str(self.df.iat[i, j]))
                            self.datatable_2.setItem(i, j, item)

            # Set the column headers in the table widget
            self.datatable_2.setHorizontalHeaderLabels(list(self.df.columns))
            del self.df


    def value(self):
            print(f"path is " + Ui_MainWindow.file_path)
            dn(self.label_5, self.frame_28,self.tableWidget,  Ui_MainWindow.file_path)
    # ddn clasifier
    def annule(self):
            Ui_MainWindow.file_path = ""
            self.label_5.setText("")
            Ui_MainWindow.value = 0
    # silde menu funtion
    def slidmenu(self):
            if self.menuvalue == 0:
                    self.ani = QtCore.QPropertyAnimation(self.menu, b"maximumWidth")
                    self.ani.setStartValue(47)
                    self.ani.setEndValue(125)
                    self.ani.start()
                    self.menuvalue = 1

            else:
                    self.ani = QtCore.QPropertyAnimation(self.menu, b"maximumWidth")
                    self.ani.setStartValue(125)
                    self.ani.setEndValue(47)
                    self.ani.start()
                    self.menuvalue = 0
   
    def htest (self):
            self.mtest.setStyleSheet('background-color:rgb(30,144,255);'
                                     'padding:3px 3px;')
            self.mhome.setStyleSheet('background-color:	rgb(40,40,40)'
                                     'padding:3px 3px;')
            self.mdatabase.setStyleSheet('background-color:	rgb(40,40,40)'
                                         'padding:3px 3px;')
            self.mgraphique.setStyleSheet('background-color:	rgb(40,40,40);'
                                          'padding:3px 3px;')
    def hhome (self):
            self.mhome.setStyleSheet('background-color:rgb(30,144,255);'
                                     'padding:3px 3px;')
            self.mtest.setStyleSheet('background-color:	rgb(40,40,40)'
                                     'padding:3px 3px;')
            self.mdatabase.setStyleSheet('background-color:	rgb(40,40,40)'
                                         'padding:3px 3px;')
            self.mgraphique.setStyleSheet('background-color:	rgb(40,40,40)'
                                          'padding:3px 3px;')
    def hgr(self):
            self.mgraphique.setStyleSheet('background-color:rgb(30,144,255);'
                                     'padding:3px 3px;')
            self.mtest.setStyleSheet('background-color:	rgb(40,40,40)''padding:3px 3px;')
            self.mdatabase.setStyleSheet('background-color:	rgb(40,40,40)''padding:3px 3px;')
            self.mhome.setStyleSheet('background-color:	rgb(40,40,40)''padding:3px 3px;')
    def hdata(self):
            self.mdatabase.setStyleSheet('background-color:rgb(30,144,255);'
                                     'padding:3px 3px;')
            self.mtest.setStyleSheet('background-color:	rgb(40,40,40)''padding:3px 3px;')
            self.mhome.setStyleSheet('background-color:	rgb(40,40,40)''padding:3px 3px;')
            self.mgraphique.setStyleSheet('background-color:	rgb(40,40,40)''padding:3px 3px;')
    def close_application():
    # Custom close function
       sys.exit()
    def toggle_fullscreen():
    # Custom resize function to toggle full screen
        if window.isFullScreen():
                window.showNormal()
        else:
                window.showFullScreen()

    
    def set_row_count(self):

            nb = int(self.row_2.text())
            self.datatable_2.clearContents()

            self.datatable_2.setRowCount(0)
            self.df = pd.read_csv(self.file_path, nrows=nb)

            self.datatable_2.setRowCount(self.df.shape[0])
            self.datatable_2.setColumnCount(self.df.shape[1])

            # Add the data to the table widget
            for i in range(self.df.shape[0]):
                    for j in range(self.df.shape[1]):
                            item = QtWidgets.QTableWidgetItem(str(self.df.iat[i, j]))
                            self.datatable_2.setItem(i, j, item)

            # Set the column headers in the table widget
            self.datatable_2.setHorizontalHeaderLabels(list(self.df.columns))

    def setupUi(self, MainWindow):

            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(850, 450)
            MainWindow.setMinimumSize(QtCore.QSize(850, 450))
            


            MainWindow.setStyleSheet("QToolButton{\n"
                                     "border:none;\n"
                                     "background-color:transparent;}\n"
                                     "#mhome:hover{\n"
                                     "padding:1px solid red;}\n"
                                     "\n"
                                     "\n"
                                     "")
            self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
          
      




            font = QtGui.QFont()
            font.setPointSize(1)
            MainWindow.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.FramelessWindowHint)
            self.centralwidget.setFont(font)
            self.centralwidget.setStyleSheet("background-color: rgb(40,40,40)")
            self.centralwidget.setObjectName("centralwidget")
            self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setSpacing(0)
            self.verticalLayout.setObjectName("verticalLayout")
            self.nav = QtWidgets.QFrame(parent=self.centralwidget)
            self.nav.setMaximumSize(QtCore.QSize(16777215, 33))
            self.nav.setStyleSheet('background-color:    rgb(40,40,40)')
            self.nav.setStyleSheet("border-bottom: 1px solid white;")
            self.nav.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.nav.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.nav.setObjectName("nav")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.nav)
            self.horizontalLayout_2.setContentsMargins(16, 0, 0, 0)
            self.horizontalLayout_2.setSpacing(0)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.frame_5 = QtWidgets.QFrame(parent=self.nav)
            self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_5.setObjectName("frame_5")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
            self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_4.setSpacing(0)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.toolButton = QtWidgets.QToolButton(parent=self.frame_5)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/profile-user.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.toolButton.setIcon(icon)
            self.toolButton.setIconSize(QtCore.QSize(21, 21))
            self.toolButton.setObjectName("toolButton")
            self.toolButton.setStyleSheet("border:none;")
            self.horizontalLayout_4.addWidget(self.toolButton)
            self.horizontalLayout_2.addWidget(self.frame_5, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
            self.frame_2 = QtWidgets.QFrame(parent=self.nav)
            self.frame_2.setStyleSheet("#close:hover{\n"
                                       "background-color:red;\n"
                                       "}\n"
                                       "QToolButton{\n"
                                       "margin-left:10px;}")
            self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_2.setObjectName("frame_2")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setSpacing(0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.toolButton_2 = QtWidgets.QToolButton(parent=self.frame_2)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/minus (1).png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.toolButton_2.setIcon(icon1)
            self.toolButton_2.setStyleSheet("border:none;")
            self.toolButton_2.setObjectName("toolButton_2")
            self.horizontalLayout_3.addWidget(self.toolButton_2)
            self.toolButton_3 = QtWidgets.QToolButton(parent=self.frame_2)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/expand.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.toolButton_3.setIcon(icon2)
            self.toolButton_3.clicked.connect(self.toggle_fullscreen)
            self.toolButton_3.setStyleSheet("border:none;")
            self.toolButton_3.setIconSize(QtCore.QSize(12, 12))
            self.toolButton_3.setObjectName("toolButton_3")
            self.horizontalLayout_3.addWidget(self.toolButton_3)
            self.close = QtWidgets.QToolButton(parent=self.frame_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                               QtWidgets.QSizePolicy.Policy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
            self.close.setSizePolicy(sizePolicy)
            self.close.setStyleSheet('padding: 0px 4px;')
            self.close.setStyleSheet("border:none;")
            self.close.clicked.connect(self.close_application)
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/cancel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.close.setIcon(icon3)
            self.close.setObjectName("close")
            self.horizontalLayout_3.addWidget(self.close)
            self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            self.verticalLayout.addWidget(self.nav)
            self.center = QtWidgets.QFrame(parent=self.centralwidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.center.sizePolicy().hasHeightForWidth())
            self.center.setSizePolicy(sizePolicy)
            self.center.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.center.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.center.setObjectName("center")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.center)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setSpacing(0)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.center_2 = QtWidgets.QFrame(parent=self.center)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.center_2.sizePolicy().hasHeightForWidth())
            self.center_2.setSizePolicy(sizePolicy)
            self.center_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.center_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.center_2.setObjectName("center_2")
            self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.center_2)
            self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_12.setSpacing(0)
            self.horizontalLayout_12.setObjectName("horizontalLayout_12")
            self.menu = QtWidgets.QFrame(parent=self.center_2)
            self.menu.setMinimumSize(QtCore.QSize(52, 0))
            self.menu.setMaximumSize(QtCore.QSize(44, 16777215))
            self.menu.setStyleSheet("QToolButton:hover{\n"
                                    "border:none\n"
                                    "background-color:    rgb(64,64,64);}")
            self.menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.menu.setObjectName("menu")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu)
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_2.setSpacing(0)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.frme_6 = QtWidgets.QFrame(parent=self.menu)
            self.frme_6.setMinimumSize(QtCore.QSize(51, 0))
            self.frme_6.setMaximumSize(QtCore.QSize(125, 16777215))
            self.frme_6.setStyleSheet("background-color:    rgb(40,40,40);\n"
                                      "border-right: 1px solid white;\n"
                                      "color:white;\n"
                                      "border-radius:2px")
            self.frme_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frme_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frme_6.setObjectName("frme_6")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frme_6)
            self.verticalLayout_3.setContentsMargins(6, -1, -1, 10)
            self.verticalLayout_3.setSpacing(5)
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.mmenu = QtWidgets.QToolButton(parent=self.frme_6)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.mmenu.setFont(font)
            self.mmenu.setStyleSheet("\n"
                                     "padding:3px 3px;\n"
                                     "border:none\n"
                                     "")
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/menu-button-of-three-horizontal-lines.png"),
                            QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.mmenu.setIcon(icon4)
            self.mmenu.setIconSize(QtCore.QSize(25, 25))
            self.mmenu.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.mmenu.setObjectName("mmenu")
            self.verticalLayout_3.addWidget(self.mmenu)
            self.mhome = QtWidgets.QToolButton(parent=self.frme_6)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.mhome.setFont(font)
            self.mhome.setStyleSheet("background-color:rgb(30,144,255);\n"
                                     "\n"
                                     "padding:3px 3px;\n"
                                     "border:none\n"
                                     "\n"
                                     "")
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/home (1).png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.mhome.setIcon(icon5)
            self.mhome.setIconSize(QtCore.QSize(25, 25))
            self.mhome.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.mhome.setObjectName("mhome")
            self.verticalLayout_3.addWidget(self.mhome)
            self.mtest = QtWidgets.QToolButton(parent=self.frme_6)
            self.mtest.setEnabled(False)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.mtest.setFont(font)
            self.mtest.setStyleSheet("\n"
                                     "padding:3px 3px;\n"
                                     "border:none\n"
                                     "")
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/approval.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.mtest.setIcon(icon6)
            self.mtest.setIconSize(QtCore.QSize(25, 25))
            self.mtest.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.mtest.setObjectName("mtest")
            self.verticalLayout_3.addWidget(self.mtest)
            self.mdatabase = QtWidgets.QToolButton(parent=self.frme_6)
            self.mdatabase.setEnabled(False)
            self.mdatabase.setStyleSheet("\n"
                                
                                     "border:none\n"
                                     "")
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.mdatabase.setFont(font)
            self.mdatabase.setStyleSheet("padding:3px 3px;""border:none")
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/database (1).png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.mdatabase.setIcon(icon7)
            self.mdatabase.setIconSize(QtCore.QSize(25, 25))
            self.mdatabase.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.mdatabase.setObjectName("mdatabase")
            self.verticalLayout_3.addWidget(self.mdatabase)
            self.mgraphique = QtWidgets.QToolButton(parent=self.frme_6)
            self.mgraphique.setEnabled(False)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.mgraphique.setFont(font)
            self.mgraphique.setStyleSheet("padding:3px 3px\n;"
                                          "border:none\n")
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/pie-graph.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.mgraphique.setIcon(icon8)
            self.mgraphique.setIconSize(QtCore.QSize(25, 25))
            self.mgraphique.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.mgraphique.setObjectName("mgraphique")
            self.verticalLayout_3.addWidget(self.mgraphique)
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                               QtWidgets.QSizePolicy.Policy.Expanding)
            self.verticalLayout_3.addItem(spacerItem)
            self.mstring = QtWidgets.QToolButton(parent=self.frme_6)
            self.mstring.setEnabled(False)
            self.mstring.setStyleSheet("\n"
                                
                                     "border:none\n"
                                     "")
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.mstring.setFont(font)
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/settings.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.mstring.setIcon(icon9)
            self.mstring.setIconSize(QtCore.QSize(25, 25))
            self.mstring.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.mstring.setObjectName("mstring")
            self.verticalLayout_3.addWidget(self.mstring)
            self.mdonation = QtWidgets.QToolButton(parent=self.frme_6)
            self.mdonation.setEnabled(False)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.mdonation.setFont(font)
            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("C:/Users/najme/Downloads/donation.png"), QtGui.QIcon.Mode.Normal,
                             QtGui.QIcon.State.Off)
            self.mdonation.setIcon(icon10)
            self.mdonation.setStyleSheet("\n"
                                
                                     "border:none\n"
                                     "")
            self.mdonation.setIconSize(QtCore.QSize(25, 25))
            self.mdonation.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.mdonation.setObjectName("mdonation")
            self.verticalLayout_3.addWidget(self.mdonation)
            self.verticalLayout_2.addWidget(self.frme_6)
            self.horizontalLayout_12.addWidget(self.menu, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
            self.frame_3 = QtWidgets.QFrame(parent=self.center_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
            self.frame_3.setSizePolicy(sizePolicy)
            self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
            self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.frame_3.setStyleSheet("color:white")
            self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_3.setObjectName("frame_3")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_4.setSpacing(0)
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame_3)
            self.stackedWidget.setStyleSheet("border-radius:5px;")
            self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
            self.stackedWidget.setLineWidth(0)
            self.stackedWidget.setObjectName("stackedWidget")
            self.pagehome_2 = QtWidgets.QWidget()
            self.pagehome_2.setObjectName("pagehome_2")
            self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.pagehome_2)
            self.verticalLayout_18.setContentsMargins(2, 0, 0, 0)
            self.verticalLayout_18.setSpacing(0)
            self.verticalLayout_18.setObjectName("verticalLayout_18")
            self.frame = QtWidgets.QFrame(parent=self.pagehome_2)
            self.frame.setStyleSheet("background-color:    rgb(40,40,40)")
            self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.frame_4 = QtWidgets.QFrame(parent=self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
            self.frame_4.setSizePolicy(sizePolicy)
            self.frame_4.setMinimumSize(QtCore.QSize(400, 400))
            self.frame_4.setStyleSheet("")
            self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_4.setObjectName("frame_4")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                                QtWidgets.QSizePolicy.Policy.Expanding)
            self.verticalLayout_6.addItem(spacerItem1)
            self.label = QtWidgets.QLabel(parent=self.frame_4)
            font = QtGui.QFont()
            font.setPointSize(40)
            font.setBold(True)
            font.setUnderline(False)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setStyleSheet("color:white;\n"
                                     "margin:10px 10px 0px 10px;\n"
                                     "")
            self.label.setObjectName("label")
            self.verticalLayout_6.addWidget(self.label)
            self.line_2 = QtWidgets.QFrame(parent=self.frame_4)
            self.line_2.setMaximumSize(QtCore.QSize(226, 1))
            self.line_2.setSizeIncrement(QtCore.QSize(1, 1))
            self.line_2.setStyleSheet("background-color:white;\n"
                                      "border-raduis:1px;\n"
                                      "margin: 0px 0px 0px 20px")
            self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
            self.line_2.setObjectName("line_2")
            self.verticalLayout_6.addWidget(self.line_2)
            self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("color:white;\n"
                                       "margin:10px;")
            self.label_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
            self.label_2.setWordWrap(True)
            self.label_2.setObjectName("label_2")
            self.verticalLayout_6.addWidget(self.label_2)
            self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_4)
            self.pushButton_9.setMinimumSize(QtCore.QSize(0, 29))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.pushButton_9.setFont(font)
            self.pushButton_9.setStyleSheet("background-color:rgb(30,144,255);\n"
                                            "\n"
                                            "\n"
                                            "border-radius: 8px;\n"
                                            "")
            self.pushButton_9.setObjectName("pushButton_9")
            self.verticalLayout_6.addWidget(self.pushButton_9)
            spacerItem2 = QtWidgets.QSpacerItem(8, 21, QtWidgets.QSizePolicy.Policy.Minimum,
                                                QtWidgets.QSizePolicy.Policy.Expanding)
            self.verticalLayout_6.addItem(spacerItem2)
            self.horizontalLayout_5.addWidget(self.frame_4, 0,
                                              QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.verticalLayout_18.addWidget(self.frame)
            self.stackedWidget.addWidget(self.pagehome_2)
            self.pagegraphique_2 = QtWidgets.QWidget()
            self.pagegraphique_2.setObjectName("pagegraphique_2")
            self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.pagegraphique_2)
            self.verticalLayout_22.setContentsMargins(2, 0, 0, 0)
            self.verticalLayout_22.setSpacing(0)
            self.verticalLayout_22.setObjectName("verticalLayout_22")
            self.frame_24 = QtWidgets.QFrame(parent=self.pagegraphique_2)
            self.frame_24.setStyleSheet("")
            self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_24.setObjectName("frame_24")
            self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_24)
            self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_23.setObjectName("verticalLayout_23")
            self.frame1 = QtWidgets.QFrame(parent=self.frame_24)
            self.frame1.setObjectName("frame1")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame1)
            self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_5.setSpacing(0)
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            self.frame_28 = QtWidgets.QFrame(parent=self.frame1)
            self.frame_28.setStyleSheet("background-color:    rgb(40,40,40);\n"
                                        "\n"
                                        "")
            self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_28.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_28.setObjectName("frame_28")
            self.verticalLayout_5.addWidget(self.frame_28)
            self.verticalLayout_23.addWidget(self.frame1)
            self.verticalLayout_22.addWidget(self.frame_24)
            self.stackedWidget.addWidget(self.pagegraphique_2)
            self.pagetest_2 = QtWidgets.QWidget()
            self.pagetest_2.setObjectName("pagetest_2")
            self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.pagetest_2)
            self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_24.setSpacing(0)
            self.verticalLayout_24.setObjectName("verticalLayout_24")
            self.frame_29 = QtWidgets.QFrame(parent=self.pagetest_2)
            self.frame_29.setStyleSheet("border-radius:5px;")
            self.frame_29.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_29.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_29.setObjectName("frame_29")
            self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_29)
            self.verticalLayout_25.setContentsMargins(2, 0, 0, 0)
            self.verticalLayout_25.setSpacing(0)
            self.verticalLayout_25.setObjectName("verticalLayout_25")
            self.frame_30 = QtWidgets.QFrame(parent=self.frame_29)
            self.frame_30.setStyleSheet("background-color:    rgb(40,40,40)")
            self.frame_30.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_30.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_30.setObjectName("frame_30")
            self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_30)
            self.verticalLayout_26.setContentsMargins(-1, -1, -1, 6)
            self.verticalLayout_26.setObjectName("verticalLayout_26")
            self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame_30)
            self.pushButton_11.setMinimumSize(QtCore.QSize(0, 32))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pushButton_11.setFont(font)
            self.pushButton_11.setStyleSheet("background-color:rgb(30,144,255);\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "border-radius: 8px;\n"
                                             "")
            self.pushButton_11.setObjectName("pushButton_11")
            self.verticalLayout_26.addWidget(self.pushButton_11)
            self.pushButton_12 = QtWidgets.QPushButton(parent=self.frame_30)
            self.pushButton_12.setMinimumSize(QtCore.QSize(0, 32))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pushButton_12.setFont(font)
            self.pushButton_12.setStyleSheet("background-color:rgb(0,255,0);\n"
                                             "\n"
                                             "\n"
                                             "border-radius: 8px;\n"
                                             "")
            self.pushButton_12.setObjectName("pushButton_12")
            self.verticalLayout_26.addWidget(self.pushButton_12)
            self.pushButton = QtWidgets.QPushButton(parent=self.frame_30)
            self.pushButton.setMinimumSize(QtCore.QSize(0, 32))
            self.pushButton.setText("Anuller")
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pushButton.setFont(font)
            self.pushButton.setStyleSheet("background-color:red;\n"
                                          "\n"
                                          "border-radius: 8px;\n"
                                          "")
            self.pushButton.setObjectName("pushButton")
            self.verticalLayout_26.addWidget(self.pushButton)
            self.verticalLayout_25.addWidget(self.frame_30, 0, QtCore.Qt.AlignmentFlag.AlignTop)
            self.frame_31 = QtWidgets.QFrame(parent=self.frame_29)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
            self.frame_31.setSizePolicy(sizePolicy)
            self.frame_31.setStyleSheet("background-color:    rgb(40,40,40);\n"
                                        "margin-top:3px;")
            self.frame_31.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_31.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_31.setObjectName("frame_31")
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_31)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.frame_6 = QtWidgets.QFrame(parent=self.frame_31)
            self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_6.setObjectName("frame_6")
            self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
            self.verticalLayout_9.setObjectName("verticalLayout_9")

            
            self.label_3 = QtWidgets.QLabel(parent=self.frame_6)
            self.label_3.setObjectName("label_3")
            self.label_3.setText("table of result")
            self.verticalLayout_9.addWidget(self.label_3)


            self.tableWidget =QtWidgets.QTableWidget(parent=self.frame_6)
            self.tableWidget.setRowCount(3)
            self.tableWidget.setColumnCount(3)
            self.verticalLayout_9.addWidget(self.tableWidget)  
            self.verticalLayout_7.addWidget(self.frame_6)
            self.frame_7 = QtWidgets.QFrame(parent=self.frame_31)
            self.frame_7.setMinimumSize(QtCore.QSize(250, 0))
            self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_7.setObjectName("frame_7")
            self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
            self.verticalLayout_8.setObjectName("verticalLayout_8")
            self.label_4 = QtWidgets.QLabel(parent=self.frame_7)
            self.label_4.setObjectName("label_4")
            self.label_4.setText("result:")
            self.verticalLayout_8.addWidget(self.label_4)
            self.label_5 = QtWidgets.QLabel(parent=self.frame_7)
            self.label_5.setText(" ")
            self.label_5.setObjectName("label_5")
            self.verticalLayout_8.addWidget(self.label_5)
            spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                                QtWidgets.QSizePolicy.Policy.Expanding)
            self.verticalLayout_8.addItem(spacerItem3)
            self.verticalLayout_7.addWidget(self.frame_7)
            self.verticalLayout_25.addWidget(self.frame_31)
            self.verticalLayout_24.addWidget(self.frame_29)
            self.stackedWidget.addWidget(self.pagetest_2)

            self.pagedatabase_2 = QtWidgets.QWidget()
            self.pagedatabase_2.setObjectName("pagedatabase_2")
            self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.pagedatabase_2)
            self.verticalLayout_28.setContentsMargins(2, 0, 0, 0)
            self.verticalLayout_28.setSpacing(0)
            self.verticalLayout_28.setObjectName("verticalLayout_28")
            self.frame_32 = QtWidgets.QFrame(parent=self.pagedatabase_2)
            self.frame_32.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_32.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_32.setObjectName("frame_32")
            self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_32)
            self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_29.setSpacing(0)
            self.verticalLayout_29.setObjectName("verticalLayout_29")
            self.frame_33 = QtWidgets.QFrame(parent=self.frame_32)
            self.frame_33.setMinimumSize(QtCore.QSize(0, 0))
            self.frame_33.setStyleSheet("background-color:    rgb(40,40,40);\n"
                                        "margin-bottom:3px;")
            self.frame_33.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_33.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_33.setObjectName("frame_33")
            self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_33)
            self.horizontalLayout_15.setContentsMargins(0, -1, -1, -1)
            self.horizontalLayout_15.setObjectName("horizontalLayout_15")
            self.frame_34 = QtWidgets.QFrame(parent=self.frame_33)
            self.frame_34.setStyleSheet("border:1px solid white ;\n"
                                        "border-radius: 6px ;")
            self.frame_34.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_34.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_34.setObjectName("frame_34")
            self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_34)
            self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_16.setSpacing(0)
            self.horizontalLayout_16.setObjectName("horizontalLayout_16")
            self.row_2 = QtWidgets.QLineEdit(parent=self.frame_34)
            self.row_2.setStyleSheet("border:none")
            self.row_2.setObjectName("row_2")
            self.horizontalLayout_16.addWidget(self.row_2)
            self.toolButton_8 = QtWidgets.QToolButton(parent=self.frame_34)
            self.toolButton_8.setStyleSheet("border:none")
            icon11 = QtGui.QIcon()
            icon11.addPixmap(QtGui.QPixmap("../../Downloads/magnifying-glass (1).png"), QtGui.QIcon.Mode.Normal,
                             QtGui.QIcon.State.Off)
            self.toolButton_8.setIcon(icon11)
            self.toolButton_8.setIconSize(QtCore.QSize(12, 12))
            self.toolButton_8.setObjectName("toolButton_8")
            self.horizontalLayout_16.addWidget(self.toolButton_8)
            self.horizontalLayout_15.addWidget(self.frame_34)
            spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                QtWidgets.QSizePolicy.Policy.Minimum)
            self.horizontalLayout_15.addItem(spacerItem3)
            self.verticalLayout_29.addWidget(self.frame_33)
            self.frame_35 = QtWidgets.QFrame(parent=self.frame_32)
            self.frame_35.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_35.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_35.setObjectName("frame_35")
            self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_35)
            self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_30.setSpacing(0)
            self.verticalLayout_30.setObjectName("verticalLayout_30")
            self.datatable_2 = QtWidgets.QTableWidget(parent=self.frame_35)
            self.datatable_2.setMinimumSize(QtCore.QSize(632, 440))
            self.datatable_2.setStyleSheet("background-color:    rgb(40,40,40)")
            self.datatable_2.setObjectName("datatable_2")
            self.datatable_2.setColumnCount(0)
            self.datatable_2.setRowCount(0)
            self.verticalLayout_30.addWidget(self.datatable_2)
            self.verticalLayout_29.addWidget(self.frame_35)
            self.verticalLayout_28.addWidget(self.frame_32)
            self.stackedWidget.addWidget(self.pagedatabase_2)
            self.verticalLayout_4.addWidget(self.stackedWidget)
            self.horizontalLayout_12.addWidget(self.frame_3)
            self.horizontalLayout.addWidget(self.center_2)
            self.verticalLayout.addWidget(self.center)
            MainWindow.setCentralWidget(self.centralwidget)

            # declation of varbele
            self.menuvalue = 0
            self.dvalue = 0
            
            self.mtest.setEnabled(True)
            self.mdatabase.setEnabled(True)
            self.mgraphique.setEnabled(True)
   
            #  menu sild conection
            self.mmenu.clicked.connect(self.slidmenu)
            self.pushButton_11.clicked.connect(self.load_csv)
            self.pushButton_12.clicked.connect(self.value)
            self.mhome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagehome_2))
            self.mhome.clicked.connect(self.hhome)
            self.mtest.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagetest_2))
            self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagetest_2))
            self.mtest.clicked.connect(self.htest)
            self.mdatabase.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagedatabase_2))
            self.mdatabase.clicked.connect(self.hdata)
            self.mgraphique.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagegraphique_2))
            self.mgraphique.clicked.connect(self.hgr)
            self.row_2.textChanged.connect(self.set_row_count)
            


            self.retranslateUi(MainWindow)
            self.stackedWidget.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)









if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet("QHeaderView::section {background-color: black;}")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())




