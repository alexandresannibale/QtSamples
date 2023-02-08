# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:56:58 2023

@author: Alexandre
"""

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
import numpy as np

class FileLocationDialog(QMainWindow):

    def __init__(self):

        super(FileLocationDialog,self).__init__()

        uic.loadUi("pyqt_GraphTest.ui", self)

        
        self.button =  self.findChild(QPushButton,"pushButton")

        self.show()

        self.button.clicked.connect(self.selectFileLocationLoadData)

    def plotgraph(self, hour, temperature):
        
            self.graphWidget.plot(hour, temperature)
            
    def loaddata(self,file_location):
        
        M = np.loadtxt(file_location, skiprows=1)
        x = M[:,0]
        y = M[:,1]
        
        return x,y
         
        
            
    def selectFileLocationLoadData(self):

        file_location = QFileDialog.getOpenFileName(self, "Data File Location Selection")
        
        print(file_location)
        
        if file_location == ('',''):
            print("No data selected")
            return
        hour, temperature = self.loaddata(file_location[0])
        
        self.plotgraph(hour,temperature)

        print(file_location)


app = QApplication([])

ui = FileLocationDialog()

app.exec()