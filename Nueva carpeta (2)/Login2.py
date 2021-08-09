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
        MainWindow.resize(350, 201)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usuario = QtWidgets.QLabel(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(20, 20, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.usuario.setFont(font)
        self.usuario.setStyleSheet("color: rgb(0, 0, 0);\n"
        "background-color: rgb(170, 255, 127);")
        self.usuario.setObjectName("usuario")
        self.pass = QtWidgets.QLabel(self.centralwidget)
        self.pass.setGeometry(QtCore.QRect(20, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.pass.setFont(font)
        self.pass.setStyleSheet("color: rgb(0, 255, 0);\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(85, 255, 255);")
        self.pass.setObjectName("pass")
        self.usuario_datos = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario_datos.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.usuario_datos.setObjectName("usuario_datos")
        self.pass_datos = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_datos.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.pass_datos.setObjectName("pass_datos")
        self.registrar = QtWidgets.QPushButton(self.centralwidget)
        self.registrar.setGeometry(QtCore.QRect(130, 100, 75, 23))
        self.registrar.setObjectName("registrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usuario.setText(_translate("MainWindow", "USUARIO"))
        self.pass.setText(_translate("MainWindow", "PASS"))
        self.registrar.setText(_translate("MainWindow", "registrar"))