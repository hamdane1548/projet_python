from PyQt6.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel
from PyQt6.QtCore import Qt
class Navbar(QWidget):
    def __init__(self):
        super().__init__()
        self.initalise_navbar()
    def initalise_navbar(self):
        screen_gemotry=QApplication.primaryScreen().availableGeometry()
        
        self.setStyleSheet("background-color: black;")
        self.setMaximumHeight(40) 
        label_teste=QLabel("teste",self)
        label_teste.setStyleSheet("background:black;")
        label_teste.setAlignment(Qt.AlignmentFlag.AlignTop)
        label_teste.setGeometry(20,0,100,100)
        
   