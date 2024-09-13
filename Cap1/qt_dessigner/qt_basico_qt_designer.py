import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('mainWindow.ui')
        self.ui.setWindowIcon(QtGui.QIcon('ubb.png'))
        self.ui.show()
        
        self.l_name = self.ui.lineEdit
        
        b_quit = self.ui.pushButton
        b_quit.clicked.connect(self.click)     
        
    @pyqtSlot()
    def click(self):
        value = self.l_name.text()
        self.l_name.setText( f'Hola {value}' )

app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec())
