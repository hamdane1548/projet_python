from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget
)
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
from PyQt6.QtCore import Qt, QRectF


class BTreeNode:
    def __init__(self, t):
        self.t = t  # Minimum degree
        self.keys = []  # Liste des clés dans le nœud
        self.children = []  # Liste des enfants
        self.leaf = True  # True si le nœud est une feuille

    def is_full(self):
        return len(self.keys) == 2 * self.t - 1

    def split(self, parent, index):
        """Divise le nœud actuel et ajuste le parent."""
        new_node = BTreeNode(self.t)
        mid_index = len(self.keys) // 2
        split_key = self.keys[mid_index]

        # Séparer les clés et les enfants
        new_node.keys = self.keys[mid_index + 1:]
        self.keys = self.keys[:mid_index]

        if not self.leaf:
            new_node.children = self.children[mid_index + 1:]
            self.children = self.children[:mid_index + 1]
            new_node.leaf = False

        # Ajouter la clé médiane au parent
        parent.keys.insert(index, split_key)
        parent.children.insert(index + 1, new_node)

    def insert_non_full(self, key):
        """Insère une clé dans un nœud non plein."""
        if self.leaf:
            # Insérer dans une feuille
            self.keys.append(key)
            self.keys.sort()
        else:
            # Trouver l'enfant approprié
            index = len(self.keys) - 1
            while index >= 0 and key < self.keys[index]:
                index -= 1
            index += 1

            if self.children[index].is_full():
                self.children[index].split(self, index)
                if key > self.keys[index]:
                    index += 1

            self.children[index].insert_non_full(key)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def insert(self, key):
        """Insère une clé dans l'arbre."""
        if self.root.is_full():
            new_root = BTreeNode(self.t)
            new_root.children.append(self.root)
            new_root.leaf = False
            self.root.split(new_root, 0)
            self.root = new_root

        self.root.insert_non_full(key)


class BTreeWidget(QWidget):
    def __init__(self, btree):
        super().__init__()
        self.btree = btree
        self.node_size = 50
        self.level_spacing = 100

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        if self.btree.root:
            self.draw_node(painter, self.btree.root, self.width() // 2, 50, self.width() // 4)

    def draw_node(self, painter, node, x, y, spacing):
        """Dessine un nœud et ses enfants."""
        rect_width = len(node.keys) * self.node_size
        rect_x = x - rect_width // 2
        rect_y = y

        # Dessiner le nœud
        painter.setBrush(QBrush(QColor("lightblue")))
        painter.drawRect(rect_x, rect_y, rect_width, self.node_size)

        # Dessiner les clés
        painter.setPen(Qt.GlobalColor.black)
        for i, key in enumerate(node.keys):
            key_x = rect_x + i * self.node_size
            painter.drawText(
                QRectF(key_x, rect_y, self.node_size, self.node_size),
                Qt.AlignmentFlag.AlignCenter,
                str(key),
            )

        # Dessiner les enfants
        if not node.leaf:
            child_y = y + self.level_spacing
            for i, child in enumerate(node.children):
                child_x = x - spacing + i * (2 * spacing // len(node.children))
                painter.setPen(QPen(Qt.GlobalColor.black, 2))
                painter.drawLine(x, y + self.node_size, child_x, child_y)
                self.draw_node(painter, child, child_x, child_y, spacing // 2)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("B-arbre en PyQt6")

        # Arbre B
        self.btree = BTree(t=2)  # Degré minimum = 2

        # Widgets
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Ajouter")
        self.tree_widget = BTreeWidget(self.btree)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.add_button)
        layout.addWidget(self.tree_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connecter le bouton
        self.add_button.clicked.connect(self.add_key_to_btree)

    def add_key_to_btree(self):
        text = self.input_field.text().strip()
        if text.isdigit():
            self.btree.insert(int(text))
            self.tree_widget.update()
        self.input_field.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
