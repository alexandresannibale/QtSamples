# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 20:01:46 2023

@author: Alexandre
"""

from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def _init_(self):
        super(UI, self).init_()
        
        uic.loadUi("Test.ui", self)
        
        #define widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")
        
        #Click Button Action
        self.button.clicked.connect(self.clicker)
         
        

        self.show()
    def clicker(self):
        self.label.setText("You clicked The Button!")
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_() 