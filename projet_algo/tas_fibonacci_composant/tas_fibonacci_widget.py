from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtGui import QFont

class TasFibonacciWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.tas_fibonacci = []  # Une structure de base pour stocker les clés (vous pouvez utiliser une vraie structure de tas)

    def init_ui(self):
        self.setWindowTitle("Tas de Fibonacci - Visualisation")
        self.layout = QVBoxLayout(self)

        # Titre
        self.title_label = QLabel("Tas de Fibonacci")
        self.title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.layout.addWidget(self.title_label)

        # Zone pour afficher les éléments du tas
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.layout.addWidget(self.text_area)

    def insert_key(self, key):
        """
        Insère une clé dans le tas de Fibonacci.
        """
        self.tas_fibonacci.append(key)
        self.tas_fibonacci.sort()  # Tri pour simuler un tas (remplacez ceci par une vraie implémentation si nécessaire)
        self.update_display()

    def update_display(self):
        """
        Met à jour l'affichage des clés dans le widget.
        """
        self.text_area.clear()
        self.text_area.append("Clés dans le tas :")
        for key in self.tas_fibonacci:
            self.text_area.append(str(key))
