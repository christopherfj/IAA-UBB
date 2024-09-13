import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtCore import pyqtSlot
import numpy as np
import cv2

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('mainWindow.ui')
        self.ui.setWindowIcon(QtGui.QIcon('ubb.png'))
        self.ui.show()
        
        self.timer = QtCore.QTimer()        
        self.colors = ['RGB', 'Gris', 'Binario']
        self.index = 0

        #signals   
        self.ui.abrir.triggered.connect(self.abrir)
        self.ui.cerrar.triggered.connect(self.cerrar) 
        self.timer.timeout.connect(self.reloj)

    #slots
    @pyqtSlot()
    def abrir(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir archivo', '.') 
        img = cv2.imread(path)
        img = cv2.resize( img, (301,301) )
        self.rgb =  cv2.cvtColor( img, cv2.COLOR_BGR2RGB ) 
        self.gray = cv2.cvtColor(self.rgb, cv2.COLOR_RGB2GRAY)
        th = 100
        ret, self.bw = cv2.threshold(self.gray, th, 255, cv2.THRESH_BINARY)
        self.height, self.width, self.channel = self.rgb.shape
        self.timer.start(1000)
        
    @pyqtSlot()
    def cerrar(self):
        self.timer.stop()
        self.ui.close()
    @pyqtSlot()
    def mostrar(self):
        color = self.colors[self.index]
        if color == 'RGB': 
            qim = QtGui.QImage(self.rgb.data, self.width, self.height, 3*self.width, QtGui.QImage.Format_RGB888)
        elif color == 'Gris': 
            qim = QtGui.QImage(self.gray.data, self.width, self.height, self.width, QtGui.QImage.Format_Indexed8)
        else:
            qim = QtGui.QImage(self.bw.data, self.width, self.height, self.width, QtGui.QImage.Format_Indexed8) 
        pix = QtGui.QPixmap.fromImage(qim)
        self.ui.view.setPixmap(pix)
    @pyqtSlot()
    def reloj(self):    
        self.index+=1
        if self.index>2:
            self.index = 0
        self.mostrar()

app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec())

