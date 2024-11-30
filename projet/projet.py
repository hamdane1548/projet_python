import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QWidget,QLineEdit,QPushButton,QHBoxLayout
from PyQt6.QtGui import QIcon,QFont,QPixmap
from PyQt6.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setWindowTitle("oussama hamdne")
      self.setGeometry(100,100,700,700)
      self.setWindowIcon(QIcon("projet/icon.png"))
     
      self.initUi()
   
    def initUi(self):
       self.button1=QPushButton("#1")
       self.button2=QPushButton("#2")
       self.button3=QPushButton("#3")
       central_Widget=QWidget()
       self.setCentralWidget(central_Widget)
       hbox=QHBoxLayout()
       hbox.addWidget(self.button1)
       hbox.addWidget(self.button2)
       hbox.addWidget(self.button3)
       central_Widget.setLayout(hbox)

class main():
   app=QApplication(sys.argv)
   window=Mainwindow()
   window.show()
   sys.exit(app.exec())

if __name__ == "__main__":
    main()
