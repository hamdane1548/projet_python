from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
from PyQt6.QtCore import Qt, QRectF

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
        painter.setBrush(QBrush(QColor("white")))
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

        if not node.leaf:
            child_y = y + self.level_spacing
            for i, child in enumerate(node.children):
                child_x = x - spacing + i * (2 * spacing // len(node.children))
                painter.setPen(QPen(Qt.GlobalColor.black, 2))
                painter.drawLine(x, y + self.node_size, child_x, child_y)
                self.draw_node(painter, child, child_x, child_y, spacing // 2)
