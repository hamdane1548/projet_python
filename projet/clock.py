import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QHBoxLayout,QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer,QTime,Qt

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("projet clock")
        self.setGeometry(400,250,600,200)
        self.setWindowIcon(QIcon("projet/clock.png"))
        self.setStyleSheet("background:black;")
        self.InitUi()
    def InitUi(self):
        self.timer=QTimer()
        self.time_label=QLabel(self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("color:green;""font-size:150px")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        vbox=QHBoxLayout()
        vbox.addWidget(self.time_label)
        central_widget.setLayout(vbox)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)
        

def main():
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

        