import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class testproject (QDialog):
    def __init__(self):
        super(testproject,self).__init__()
        loadUi('testproject.ui',self)
        self.setWindowTitle('testproject GUI')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label.setText('Welcome '+self.lineEdit.text())
        
app=QApplication(sys.argv)
widget=testproject()
widget.show()
sys.exit(app.exec_())
