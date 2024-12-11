from PyQt6.QtWidgets import QWidget, QScrollArea, QLabel,QVBoxLayout,QFrame,QPushButton,QFileDialog
from PyQt6.QtGui import QPixmap
import shutil
import os
class footer(QWidget):
    def __init__(self):
        super().__init__()
        label=QLabel("@Oussama Hamdane @Aymen Benbouhia                                             @Encadré par MR.k.OQAIDI",self)
        label.setStyleSheet("color:black")
        label.setGeometry(0,0,1200,30)
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)
   