import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QHBoxLayout,QWidget,QVBoxLayout,QGridLayout,QLineEdit,QPushButton,QScrollArea
from PyQt6.QtGui import QIcon,QPixmap,QMovie
from PyQt6.QtCore import QTimer,QTime,Qt
from Dashbord import Dashbord
from nav_bar import Navbar
from footer import footer
from home_pages import home_pages
class About(QMainWindow):
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
       home_pages.fond(self)
       self.footer=footer()
       self.footer.setParent(self)
       self.footer.setGeometry(260,670,1085,50)
       self.navbar()
       self.dashbord()
       self.images_about_us=QPixmap("projet/About us.png")
       self.images_label_about_us=QLabel(self)
       self.images_label_about_us.setPixmap(self.images_about_us)
       self.images_label_about_us.setGeometry(520,20,600,600)
       self.descirption_aboutus=QLabel("Bienvenue sur AlgoTest, votre application interactive dédiée à l'apprentissage et au test des algorithmes les plus célèbres en informatique ! Conçue pour les étudiants, les enseignants, et les passionnés\n                                                                           d'algorithmes, AlgoTest rend l'exploration des structures de données et des algorithmes à la fois intuitive et engageante.",self)
       self.descirption_aboutus.setStyleSheet("font-size:12px;")
       self.descirption_aboutus.setGeometry(270,460,1200,100)
       self.about_descrption=QLabel("Ce que propose AlgoTest",self)
       self.about_descrption.setStyleSheet("font-size:30px")
       self.about_descrption.setGeometry(620,540,360,40)
       self.dijikstra_des=QMovie("projet/DIJIKSTRA_learn.gif")
       self.dijikstra_des_lable=QLabel(self)
       self.dijikstra_des_lable.setMovie(self.dijikstra_des)
       self.dijikstra_des_lable.setGeometry(580,560,100,100)
       self.dijikstra_des_lable.setScaledContents(True)
       self.dijikstra_des.start()
       self.b_arbre_learngif_des=QMovie("projet/b_arbre_learngif.gif")
       self.b_arbre_learngif_des_des_lable=QLabel(self)
       self.b_arbre_learngif_des_des_lable.setMovie(self.b_arbre_learngif_des)
       self.b_arbre_learngif_des_des_lable.setGeometry(740,560,100,100)
       self.b_arbre_learngif_des_des_lable.setScaledContents(True)
       self.b_arbre_learngif_des.start()
       self.fibonacci_learngif_des=QMovie("projet/fibonacci.gif")
       self.fibo_des_des_lable=QLabel(self)
       self.fibo_des_des_lable.setMovie(self.fibonacci_learngif_des)
       self.fibo_des_des_lable.setGeometry(930,565,100,100)
       self.fibo_des_des_lable.setScaledContents(True)
       self.fibonacci_learngif_des.start()
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
       self.max_repeat=3
       self.count=0
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
            self.count+=1
            if self.count<self.max_repeat:
                self.current_texte=""
                self.index=0
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
        self.mon_dashbord.button_return_accueil.clicked.connect(self.return_accueil)
        self.mon_dashbord.radio3_DIJIKSTRA.toggled.connect(self.ouvriehomepages)
        self.mon_dashbord.radio2_B_arbre.toggled.connect(self.ouvrie_learn_b_arbre)
        self.mon_dashbord.radio1_tas_fibo.toggled.connect(self.learn_tas)
        self.mon_dashbord.button_about.clicked.connect(self.about)
        self.mon_dashbord.radio2_teste_b_arbre.toggled.connect(self.ouvrireteste_barbre)
    def ouvrireteste_barbre(self):
        from teste_b_arbre import test_barbre
        self.teste_barbe=test_barbre()
        self.teste_barbe.showMaximized()
        self.close()
    def about(self):
        from About import About
        self.abouthh=About()
        self.abouthh.showMaximized()
        self.close()
    def learn_tas(self):
        from tas_fibo_learn import learn_tas_fibo
        self.fibo_learn=learn_tas_fibo()
        self.fibo_learn.showMaximized()
        self.close()
    def ouvrie_learn_b_arbre(self):
        from learn_barbre import learn_barbre
        self.barbre_learn=learn_barbre()
        self.barbre_learn.showMaximized()
        self.close()
    def ouvriehomepages(self):
        from learn_dijikstra import learn_dijikstra
        self.dijkstra_window = learn_dijikstra()
        self.dijkstra_window.showMaximized()
        self.close()
    def return_accueil(self):
        from home_pages import home_pages
        self.homepages=home_pages()
        self.homepages.showMaximized()
        self.close()
    def update_time(self):
        current_time=QTime.currentTime().toString("hh : mm : ss ")
        self.time.setText(current_time)
def main():
    app=QApplication(sys.argv)
    window=About()
    window.show()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

        