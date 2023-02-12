import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("//Users//choiwoojin//Desktop//PythonPractice//untitled.ui")[0] # ui 파일 경로

class WindowClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

       
        self.pushButton.clicked.connect(self.buttonFunction)

    def buttonFunction(self) :
        print("황제성스미쑤")
        print(os.uname())
        





if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()