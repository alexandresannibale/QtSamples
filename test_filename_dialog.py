# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:07:31 2023

@author: vsanni
"""

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog



class FileLocationDialog(QMainWindow):

    def __init__(self):

        super(FileLocationDialog,self).__init__()

        uic.loadUi("test_filename_dialog.ui", self)

        self.button =  self.findChild(QPushButton,"pushButton")

        self.show()

        self.button.clicked.connect(self.selectFileLocationLoadData)

    def selectFileLocationLoadData(self):

        file_location = QFileDialog.getOpenFileName(self, "Data File Location Selection")

        print(file_location)


app = QApplication([])

ui = FileLocationDialog()

app.exec()
