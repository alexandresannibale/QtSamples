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
        
            self.graphWidget.plot(hour, temperature,pen=pg.mkPen('r', width=3))
            self.graphWidget.setLabel("bottom", "Time")
            self.graphWidget.setTitle( "Values")
            self.graphWidget.setLabel("left", "Points")
            self.graphWidget.showGrid(x = True, y = True, alpha = 0.7)
            
            
    def loaddata(self,file_location):
        M = np.array(readFilterLinesData(file_location), dtype = float) 
      
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

#%%
def readFilterLinesData(filename):
    with open(filename, "r") as fi:   
        n = 1
        S = []
        while n >0:
            s = fi.readline()
            n =  len(s)
            s = s.split()
            
            if arenumbers(s) == True:
                S.append(s)
                print(s)
    return S
    
#%%
def arenumbers(s):
    if s == []:
        return False
    else:
        for b in s:
          try:
              float(b)
          except:
              return False
      
        return True
#%%
app = QApplication([])

ui = FileLocationDialog()

app.exec()