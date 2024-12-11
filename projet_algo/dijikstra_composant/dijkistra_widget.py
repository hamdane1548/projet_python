from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
import heapq

class DijkstraWidget(QWidget):
    def __init__(self, graph, start_node):
        super().__init__()
        self.graph = graph
        self.start_node = start_node
        self.distances = self.calculate_dijkstra()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel(f"Dijkstra Algorithm Results from Node {self.start_node}")
        title.setStyleSheet("font-size:16px; font-weight:bold; margin:10px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setRowCount(len(self.distances))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Node", "Distance"])
        self.table.horizontalHeader().setStretchLastSection(True)

        for row, (node, distance) in enumerate(self.distances.items()):
            self.table.setItem(row, 0, QTableWidgetItem(str(node)))
            self.table.setItem(row, 1, QTableWidgetItem(str(distance)))

        layout.addWidget(self.table)
        self.setLayout(layout)

    def calculate_dijkstra(self):
        num_nodes = len(self.graph)
        distances = {i: float('inf') for i in range(num_nodes)}
        distances[self.start_node] = 0

        priority_queue = [(0, self.start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in enumerate(self.graph[current_node]):
                if weight > 0:  # There's a connection
                    distance = current_distance + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))

        return distances
