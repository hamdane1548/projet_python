import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QHBoxLayout,QWidget,QVBoxLayout,QGridLayout,QLineEdit,QPushButton,QScrollArea
from PyQt6.QtGui import QIcon,QPixmap,QMovie
from PyQt6.QtCore import QTimer,QTime,Qt
from Dashbord import Dashbord
from nav_bar import Navbar
from teste import ScrollableWidget
from footer import footer
from home_pages import home_pages
class test_barbre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initalis_interface_principal()
        self.b_arbre_entre_user()
        self.initlise_les_parmetre_arbre()
        self.calcul_taille_noude_est_enfant()
    def initalis_interface_principal(self):
       screen_geomtry=QApplication.primaryScreen().availableGeometry()
       screen_widt=screen_geomtry.width()
       screen_height=screen_geomtry.height()
       self.setGeometry(0,0,screen_widt,screen_height)
       self.setWindowTitle("Projet Alogirthme")
       self.setWindowIcon(QIcon("projet/python.png"))
       home_pages.fond(self)
       self.footer=footer()
       self.footer.setParent(self)
       self.footer.setGeometry(260,670,1085,50)
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
       #en ligne
       self.time=QLabel(self)
       self.time.setGeometry(1250,18,90,30)
       self.time.setStyleSheet("color:white;font-size:15px")
       self.timer=QTimer(self)
       self.timer.timeout.connect(self.update_time)
       self.timer.start(100)
       #time logo
       self.time_logo=QMovie("projet/time.gif")
       self.time_logo_label=QLabel(self)
       self.time_logo_label.setMovie(self.time_logo)
       self.time_logo.start()
       self.time_logo_label.setGeometry(1204,15,40,40)
       self.time_logo_label.setScaledContents(True)
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
       # learn dijikstra pages :
       self.leran_movie=QMovie("projet/learn.gif")
       self.lable_movie=QLabel(self)
       self.lable_movie.setMovie(self.leran_movie)
       self.leran_movie.start()
       self.lable_movie.setGeometry(290,50,150,150)
    def updatetexte(self):
        if self.index<len(self.full_texte):
            self.current_texte+=self.full_texte[self.index]
            self.label_titre.setText(self.current_texte)
            self.index+=1
        else:
            self.timer.stop()
    def b_arbre_entre_user(self):
        #taille de noued
        self.taille_noued=QLabel("Entre la taille de noeud:",self)
        self.taille_noued.setGeometry(260,180,180,30)  
        self.taille_noued.setStyleSheet("color:black;font-size:15px;") 
        self.tailleentre_line_edit=QLineEdit(self)
        self.tailleentre_line_edit.setGeometry(420,186,100,20)
        self.tailleentre_line_edit.setPlaceholderText("entre")
        #element a inesere
        self.insere_label=QLabel("Entre le element a insere:",self)
        self.insere_label.setGeometry(260,220,180,30)  
        self.insere_label.setStyleSheet("color:black;font-size:15px;") 
        self.insere_line_edit=QLineEdit(self)
        self.insere_line_edit.setGeometry(429,225,100,20)
        self.insere_line_edit.setPlaceholderText("entre")
        #le element a supprimer
        self.supprimer_label=QLabel("Entre le element a supprimer:",self)
        self.supprimer_label.setGeometry(260,260,200,30)  
        self.supprimer_label.setStyleSheet("color:black;font-size:15px;") 
        self.supprimer_line_edit=QLineEdit(self)
        self.supprimer_line_edit.setGeometry(460,265,100,20)
        self.supprimer_line_edit.setPlaceholderText("entre")
    def dashbord(self):
        self.central=QWidget()
        self.setCentralWidget(self.central)
        self.layout=QVBoxLayout()
        self.mon_dashbord=Dashbord()
        self.layout.addWidget(self.mon_dashbord)
        self.layout.setContentsMargins(0,0,0,0)
        self.central.setLayout(self.layout)
    def initlise_les_parmetre_arbre(self):
        liste_entreuser=[]   
    def calcul_taille_noude_est_enfant(self,ordre):
        self.max_noued=ordre-1
        self.nb_enfant=ordre
    def update_time(self):
        current_time=QTime.currentTime().toString("hh : mm : ss ")
        self.time.setText(current_time)
def main():
    app=QApplication(sys.argv)
    window=test_barbre()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

        