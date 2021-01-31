from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyspeedtest
import sys


class Check_Internet_Speed(QtWidgets.QWidget):
 	"""docstring for Check_Internet_Speed"""
 	def __init__(self):
 		super(Check_Internet_Speed, self).__init__()
 		self.setWindowTitle("Python Speed Checker")
 		self.setGeometry(100, 100, 300, 200) 
 		self.UiComponents() 
 		self.show()

 	def UiComponents(self):
 		self.label_1 = QLabel("Enter the Website Url")
 		self.button = QPushButton("Check")
 		self.type_space = QLineEdit()
 		self.label_2 = QLabel("Ping Result : ")
 		self.label_3 = QLabel("Download Result : ")

 		v_box = QVBoxLayout()
 		v_box.addWidget(self.label_1)
 		v_box.addWidget(self.type_space)
 		v_box.addWidget(self.button)
 		v_box.addWidget(self.label_2)
 		v_box.addWidget(self.label_3)
 		self.button.clicked.connect(lambda x :  self.speedtest(self.type_space.text()))
 		self.setLayout(v_box)

 	def speedtest(self,url):
 		res = pyspeedtest.SpeedTest(url)
 		Ping_res = res.ping()
 		Download_res = res.download()
 		self.label_2.setText("Ping Result :" + str(Ping_res))
 		self.label_3.setText("Download Result :" + str(Download_res))



if __name__ == '__main__':
	App = QApplication(sys.argv) 
	window = Check_Internet_Speed()
	sys.exit(App.exec()) 