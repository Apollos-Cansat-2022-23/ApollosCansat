# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSlider, QStatusBar,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CustomParameters = QWidget(self.centralwidget)
        self.CustomParameters.setObjectName(u"CustomParameters")
        self.CustomParameters.setGeometry(QRect(0, 0, 181, 651))
        self.CustomParameters.setAutoFillBackground(True)
        self.radiusSlider = QSlider(self.CustomParameters)
        self.radiusSlider.setObjectName(u"radiusSlider")
        self.radiusSlider.setGeometry(QRect(10, 30, 160, 16))
        self.radiusSlider.setMaximum(100)
        self.radiusSlider.setValue(33)
        self.radiusSlider.setOrientation(Qt.Horizontal)
        self.CDSlider = QSlider(self.CustomParameters)
        self.CDSlider.setObjectName(u"CDSlider")
        self.CDSlider.setGeometry(QRect(10, 90, 160, 16))
        self.CDSlider.setMaximum(200)
        self.CDSlider.setSingleStep(1)
        self.CDSlider.setValue(33)
        self.CDSlider.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.CustomParameters)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 71, 16))
        self.label_2 = QLabel(self.CustomParameters)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 121, 20))
        self.label_3 = QLabel(self.CustomParameters)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 111, 16))
        self.DSlider = QSlider(self.CustomParameters)
        self.DSlider.setObjectName(u"DSlider")
        self.DSlider.setGeometry(QRect(10, 140, 160, 16))
        self.DSlider.setMinimum(1000)
        self.DSlider.setMaximum(2000)
        self.DSlider.setValue(1204)
        self.DSlider.setOrientation(Qt.Horizontal)
        self.graph = PlotWidget(self.centralwidget)
        self.graph.setObjectName(u"graph")
        self.graph.setGeometry(QRect(190, 0, 440, 325))
        self.graph.setAutoFillBackground(True)
        self.graph_2 = PlotWidget(self.centralwidget)
        self.graph_2.setObjectName(u"graph_2")
        self.graph_2.setGeometry(QRect(640, 0, 440, 325))
        self.graph_2.setAutoFillBackground(True)
        self.graph_3 = PlotWidget(self.centralwidget)
        self.graph_3.setObjectName(u"graph_3")
        self.graph_3.setGeometry(QRect(190, 330, 440, 325))
        self.graph_3.setAutoFillBackground(True)
        self.graph_4 = PlotWidget(self.centralwidget)
        self.graph_4.setObjectName(u"graph_4")
        self.graph_4.setGeometry(QRect(640, 330, 440, 325))
        self.graph_4.setAutoFillBackground(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 21))
        self.menuAir_Resistance = QMenu(self.menubar)
        self.menuAir_Resistance.setObjectName(u"menuAir_Resistance")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAir_Resistance.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Radius (mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Drag Coefficient (/100)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Air Density (kg/m^3)", None))
        self.menuAir_Resistance.setTitle(QCoreApplication.translate("MainWindow", u"Air Resistance", None))
    # retranslateUi

