from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget, QScrollArea, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor

class squre(QWidget):
    def __init__(self,texte):
        super().__init__()
        self.texte_entre=texte
        self.setMaximumSize(10,10)
    def paintsqure(self,event):
        painter=QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawRect(0,0,self.width(),self.height())
        painter.setpen(Qt.GlobalColor.black)
        painter.drawText(self.rect(),Qt.AlignmentFlag.AlignCenter,self.texte)