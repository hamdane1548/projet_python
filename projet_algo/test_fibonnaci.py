import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtCore import QTimer, QTime
from Dashbord import Dashbord
from home_pages import home_pages
from tas_fibonacci_composant.tas_fibonacci_widget import TasFibonacciWidget

class TestTasFibonacci(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tas_fibo_widget = None
        self.init_interface_principal()
        self.init_tas_fibonacci_inputs()

    def init_interface_principal(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())
        self.setWindowTitle("Projet Algorithme - Tas de Fibonacci")
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
        self.mon_dashbord.radio3_DIJIKSTRA.toggled.connect(self.learn_dijkstra)
        self.mon_dashbord.radio2_B_arbre.toggled.connect(self.learn_b_arbre)
        self.mon_dashbord.radio1_tas_fibo.toggled.connect(self.learn_tas)
        self.mon_dashbord.button_about.clicked.connect(self.about)

    def init_tas_fibonacci_inputs(self):
        self.insert_label = QLabel("Insert a key into Tas de Fibonacci:", self)
        self.insert_label.setGeometry(260, 180, 300, 30)
        self.insert_label.setStyleSheet("color:black; font-size:15px;")

        self.insert_input = QLineEdit(self)
        self.insert_input.setGeometry(560, 185, 200, 20)
        self.insert_input.setPlaceholderText("Enter a key to insert")

        self.insert_button = QPushButton("Insert", self)
        self.insert_button.setGeometry(770, 183, 80, 24)
        self.insert_button.setStyleSheet("background:black; color:white; border-radius:10px; font-size:14px;")
        self.insert_button.clicked.connect(self.insert_key)

    def insert_key(self):
        key_text = self.insert_input.text()

        try:
            key = int(key_text)

            if self.tas_fibo_widget is None:
                self.tas_fibo_widget = TasFibonacciWidget()
                self.tas_fibo_widget.setParent(self)
                self.tas_fibo_widget.setGeometry(700, 100, 800, 400)
                self.tas_fibo_widget.show()

            self.tas_fibo_widget.insert_key(key)
            print(f"Key {key} inserted into Tas de Fibonacci.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    def update_time(self):
        current_time = QTime.currentTime().toString("hh : mm : ss")
        self.time_label.setText(current_time)

    def return_accueil(self):
        from home_pages import home_pages
        self.homepages = home_pages()
        self.homepages.showMaximized()
        self.close()

    def learn_dijkstra(self):
        from learn_dijikstra import learn_dijikstra
        self.dijkstra_window = learn_dijikstra()
        self.dijkstra_window.showMaximized()
        self.close()

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

    def learn_b_arbre(self):
        from learn_barbre import learn_barbre
        self.barbre_learn = learn_barbre()
        self.barbre_learn.showMaximized()
        self.close()

def main():
    app = QApplication(sys.argv)
    window = TestTasFibonacci()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
