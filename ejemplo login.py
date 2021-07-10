from PyQt5 import QtWidgets, uic
import sys
app= QtWidgets.QApplication([])

ventana = uic.loadUi(".\Interfacez\Login.ui")
ventana.show()
sys.exit(app.exec())