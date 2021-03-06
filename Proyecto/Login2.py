# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(323, 120)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usuario_texto = QtWidgets.QLabel(self.centralwidget)
        self.usuario_texto.setGeometry(QtCore.QRect(40, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.usuario_texto.setFont(font)
        self.usuario_texto.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.usuario_texto.setObjectName("usuario_texto")
        self.pass_texto = QtWidgets.QLabel(self.centralwidget)
        self.pass_texto.setGeometry(QtCore.QRect(210, 10, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pass_texto.setFont(font)
        self.pass_texto.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pass_texto.setObjectName("pass_texto")
        self.usuario_datos = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario_datos.setGeometry(QtCore.QRect(0, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.usuario_datos.setFont(font)
        self.usuario_datos.setObjectName("usuario_datos")
        self.pass_datos = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_datos.setGeometry(QtCore.QRect(160, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pass_datos.setFont(font)
        self.pass_datos.setObjectName("pass_datos")
        self.registrar = QtWidgets.QPushButton(self.centralwidget)
        self.registrar.setGeometry(QtCore.QRect(90, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.registrar.setFont(font)
        self.registrar.setObjectName("registrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usuario_texto.setText(_translate("MainWindow", "USUARIO"))
        self.pass_texto.setText(_translate("MainWindow", "PASS"))
        self.registrar.setText(_translate("MainWindow", "INGRESAR"))
