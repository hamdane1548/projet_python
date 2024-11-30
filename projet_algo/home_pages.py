import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QHBoxLayout,QWidget,QVBoxLayout,QGridLayout,QLineEdit
from PyQt6.QtGui import QIcon,QPixmap
from PyQt6.QtCore import QTimer,QTime,Qt
from Dashbord import Dashbord
from nav_bar import Navbar

class home_pages(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initalis_interface_principal()
    def initalis_interface_principal(self):
       screen_geomtry=QApplication.primaryScreen().availableGeometry()
       screen_widt=screen_geomtry.width()
       screen_height=screen_geomtry.height()
       self.setGeometry(0,0,screen_widt,screen_height)
       self.setWindowTitle("Projet Alogirthme")
       self.setWindowIcon(QIcon("projet/python.png"))
       self.navbar()
       self.dashbord()
    def navbar(self):
       labe_tite=QLabel(self)
       labe_tite.setGeometry(270,10,1070,50)
       labe_tite.setStyleSheet("background:#86847e;""border:5px #86847e ;"" border-radius:10px;")
       #image logo for projet
       label_logo=QPixmap("projet/home.png")
       self.label_logo=QLabel(self)
       self.label_logo.setPixmap(label_logo)
       self.label_logo.setScaledContents(True)
       self.label_logo.setGeometry(280,20,30,30)
       label_home=QLabel("Home",self)
       label_home.setGeometry(320,20,50,30)
       label_home.setStyleSheet("color:white;""font-size:15px;""font-family:italic")
       label_serch_logo=QPixmap("projet/serch.png")
       self.label_serach=QLabel(self)
       self.label_serach.setPixmap(label_serch_logo)
       self.label_serach.setGeometry(610,20,30,30)
       self.label_serach.setScaledContents(True)
       self.label_line_edit=QLineEdit(self)
       self.label_line_edit.setGeometry(650,17,400,35)
       self.label_line_edit.setPlaceholderText("entre votre serch here")
       self.label_line_edit.setStyleSheet("""QLineEdit{
                                            border:2px solid None;
                                            border-radius:10px;
                                            }
                                          QLineEdit:focus{
                                            color:bleu;
                                          }
                                          
                                          """)
       # about 
       QPixmap_images_about=QPixmap("projet/about.png")
       self.label_image_about=QLabel(self)
       self.label_image_about.setPixmap(QPixmap_images_about)
       self.label_image_about.setGeometry(380,20,30,30)
       self.label_image_about.setScaledContents(True)
       self.about_texte=QLabel("About",self)
       self.about_texte.setGeometry(420,20,100,30)
       self.about_texte.setStyleSheet("color:white;""font-size:15px;""font-family:italic;")
       #pages principal
       self.full_texte="Bienvenu dans AlgoTest : Dijkstra, Tas de Fibonacci et B-Arbres 😊"
       self.current_texte=""
       self.index=0
       self.label_titre=QLabel("",self)
       self.label_titre.setGeometry(410,100,800,40)
       self.label_titre.setStyleSheet("color:black;font-size:26px;font-family:'Roboto';")
       self.timer=QTimer()
       self.timer.timeout.connect(self.updatetexte)
       self.timer.start(110)
       #carte de prsente les algorihtme
       #square
       #carte 1 de Dijisktre
       self.carte=QLabel(self)
       self.carte.setStyleSheet("background:#8f9ed1; border:solid 2px #a5a29a ;border-radius:15px")
       self.carte.setGeometry(400,270,220,220)
       self.image_dijkstra=QPixmap("projet/dijkstra.png")
       self.dijkstra_label=QLabel(self)
       self.dijkstra_label.setPixmap(self.image_dijkstra)
       self.dijkstra_label.setGeometry(477,280,75,75)
       self.dijkstra_label.setScaledContents(True)
       self.titre_dijkstra=QLabel("Algo Dijikstra",self)
       self.titre_dijkstra.setGeometry(458,370,200,30)
       self.titre_dijkstra.setStyleSheet("color:black;font-size:18px;font-family:'Roboto'")
       #---------------------------------------------
       self.carte2=QLabel(self)
       self.carte2.setStyleSheet("background:#a5a29a; border:solid 2px #a5a29a ;border-radius:15px")
       self.carte2.setGeometry(700,270,220,220)
       self.carte3=QLabel(self)
       self.carte3.setStyleSheet("background:#a587c5; border:solid 2px #a5a29a ;border-radius:15px")
       self.carte3.setGeometry(1000,270,220,220)
       qhbox=QHBoxLayout()
       qhbox.addWidget(self.carte)
       qhbox.addWidget(self.carte2)
       qhbox.addWidget(self.carte3)
       self.setLayout(qhbox)
    def updatetexte(self):
        if self.index<len(self.full_texte):
            self.current_texte+=self.full_texte[self.index]
            self.label_titre.setText(self.current_texte)
            self.index+=1
        else:
            self.timer.stop()
        
    def dashbord(self):
        self.central=QWidget()
        self.setCentralWidget(self.central)
        self.layout=QVBoxLayout()
        self.mon_dashbord=Dashbord()
        self.layout.addWidget(self.mon_dashbord)
        self.layout.setContentsMargins(0,0,0,0)
        self.central.setLayout(self.layout)
     
def main():
    app=QApplication(sys.argv)
    window=home_pages()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

        