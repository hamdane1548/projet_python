import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtCore import QTimer, QTime
from Dashbord import Dashbord
from home_pages import home_pages
from dijikstra_composant.dijkistra_widget import DijkstraWidget

class TestDijkstra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dijkstra_window = None
        self.init_interface_principal()
        self.init_dijkstra_inputs()

    def init_interface_principal(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())
        self.setWindowTitle("Dijkstra Algorithm")
        self.setWindowIcon(QIcon("projet/python.png"))
        home_pages.fond(self)

        # Navbar
        self.navbar = QLabel(self)
        self.navbar.setGeometry(270, 10, 1070, 50)
        self.navbar.setStyleSheet("background:#86847e; border-radius:10px;")

        self.label_home = QLabel("Home", self)
        self.label_home.setGeometry(320, 20, 50, 30)
        self.label_home.setStyleSheet("color:white; font-size:15px; font-family:italic;")

        # Time display
        self.time_label = QLabel(self)
        self.time_label.setGeometry(1250, 18, 90, 30)
        self.time_label.setStyleSheet("color:white; font-size:15px;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Time logo
        self.time_logo = QMovie("projet/time.gif")
        self.time_logo_label = QLabel(self)
        self.time_logo_label.setMovie(self.time_logo)
        self.time_logo.start()
        self.time_logo_label.setGeometry(1204, 15, 40, 40)
        self.time_logo_label.setScaledContents(True)

        # Add Dashboard
        self.dashbord()

    def dashbord(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.layout = QVBoxLayout()
        self.mon_dashbord = Dashbord()
        self.layout.addWidget(self.mon_dashbord)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.central.setLayout(self.layout)

        # Connect Dashboard buttons and radios
        self.mon_dashbord.button_return_accueil.clicked.connect(self.return_accueil)
        self.mon_dashbord.radio3_DIJIKSTRA.toggled.connect(self.ouvriehomepages)
        self.mon_dashbord.radio2_B_arbre.toggled.connect(self.ouvrie_learn_b_arbre)
        self.mon_dashbord.radio1_tas_fibo.toggled.connect(self.learn_tas)
        self.mon_dashbord.button_about.clicked.connect(self.about)

    def init_dijkstra_inputs(self):
        self.graph_label = QLabel("Enter graph data (adjacency matrix):", self)
        self.graph_label.setGeometry(260, 180, 300, 30)
        self.graph_label.setStyleSheet("color:black; font-size:15px;")

        self.graph_input = QLineEdit(self)
        self.graph_input.setGeometry(560, 185, 300, 20)
        self.graph_input.setPlaceholderText("Example: [[0,1,4],[1,0,2],[4,2,0]]")

        self.start_node_label = QLabel("Enter start node:", self)
        self.start_node_label.setGeometry(260, 220, 200, 30)
        self.start_node_label.setStyleSheet("color:black; font-size:15px;")

        self.start_node_input = QLineEdit(self)
        self.start_node_input.setGeometry(400, 225, 100, 20)
        self.start_node_input.setPlaceholderText("Start node")

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setGeometry(530, 223, 80, 24)
        self.submit_button.setStyleSheet("background:black; color:white; border-radius:10px; font-size:14px;")
        self.submit_button.clicked.connect(self.run_dijkstra)

    def run_dijkstra(self):
        graph_text = self.graph_input.text()
        start_node_text = self.start_node_input.text()

        try:
            graph = eval(graph_text)  # Be cautious with eval, validate input in production code.
            start_node = int(start_node_text)

            if self.dijkstra_window:
                self.dijkstra_window.close()

            self.dijkstra_window = DijkstraWidget(graph, start_node)
            self.dijkstra_window.setParent(self)
            self.dijkstra_window.setGeometry(700, 100, 800, 400)
            self.dijkstra_window.show()

            print(f"Dijkstra algorithm executed from node {start_node}")
        except Exception as e:
            print(f"Invalid input: {e}")

    def update_time(self):
        current_time = QTime.currentTime().toString("hh : mm : ss")
        self.time_label.setText(current_time)

    def return_accueil(self):
        from home_pages import home_pages
        self.homepages = home_pages()
        self.homepages.showMaximized()
        self.close()

    def ouvriehomepages(self):
        from learn_dijikstra import learn_dijikstra
        if self.dijkstra_window:
            self.dijkstra_window.close()
        self.dijkstra_window = learn_dijikstra()
        self.dijkstra_window.showMaximized()

    def about(self):
        from About import About
        self.abouthh = About()
        self.abouthh.showMaximized()
        self.close()

    def learn_tas(self):
        from tas_fibo_learn import learn_tas_fibo
        self.fibo_learn = learn_tas_fibo()
        self.fibo_learn.showMaximized()
        self.close()

    def ouvrie_learn_b_arbre(self):
        from learn_barbre import learn_barbre
        self.barbre_learn = learn_barbre()
        self.barbre_learn.showMaximized()
        self.close()

def main():
    app = QApplication(sys.argv)
    window = TestDijkstra()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
