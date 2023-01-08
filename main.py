"""
from PyQt5 import uic, QtWidgets
#from PyQt6.uic.properties import QtWidgets

app = QtWidgets.QApplication([])
ui = uic.loadUi("parsing_vk.ui")

ui.show()
app.exec()
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import numpy as np
import networkx as nx
#import matplotlib.pyplot as plt
import pandas as pd
import requests
import time
import scipy as sp
import json
from networkx.drawing.nx_agraph import graphviz_layout
from bs4 import BeautifulSoup as BS


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 156)
        MainWindow.setMinimumSize(QtCore.QSize(559, 156))
        MainWindow.setMaximumSize(QtCore.QSize(559, 156))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.label.setObjectName("label")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(450, 120, 101, 31))
        self.btn.setObjectName("btn")

        self.edit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit2.setGeometry(QtCore.QRect(10, 90, 541, 20))
        self.edit2.setObjectName("edit2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_2.setObjectName("label_2")

        self.edit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit1.setGeometry(QtCore.QRect(10, 30, 541, 20))
        self.edit1.setObjectName("edit1")

        self.spbox1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spbox1.setGeometry(QtCore.QRect(10, 120, 61, 22))
        self.spbox1.setMouseTracking(False)
        self.spbox1.setMinimum(1)
        self.spbox1.setMaximum(20)
        self.spbox1.setObjectName("spbox1")

        self.btn.clicked.connect(self.add_label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parsing from SM"))
        self.label.setText(_translate("MainWindow", "Token"))
        self.btn.setText(_translate("MainWindow", "start downloading"))
        self.label_2.setText(_translate("MainWindow", "Path to file"))


        
    def add_label(self):
        token = self.edit1.text()
       # ya = \
           # requests.get(
           #     f'https://api.vk.com/method/users.get?fields=education,city&v=5.131&access_token={token}').json()[
            #    "response"][0]

        new_token = ''
        count = 0
        for i in token:
            count += 1
            if count <= 45 or count >= 244:
                continue

            else:
                new_token = new_token + i
        
        return self.edit2.setText(new_token);

      
        


        html = BS(self.ya.content, 'html.parser')
       # for el in html.select(".vkuiSplitLayout__inner > .vkuiSpacing"):
          #  title = el.select(('.caption > a'))
          #  print(title[0].text)

        #self.edit2.setText(self.edit1.text())
        #print(self.edit1.text())
        #self.new_text.setText(self.ntxt.text())
        #self.ntxt.setText("Salom")

        #self.new_text.move(100, 50)
        #self.new_text.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


